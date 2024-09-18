import os
import sys
import time

from mathstropy.ml import load_model, model_predict
from libs.preprocessing import data_prep, feature_extraction
from mathstrovehiclesim import TrafficSignInterpretionSimulator

# load trained model
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = script_dir + "/model/model.pkl"
model = load_model(model_path)

d_mode = False  # dev mode not working
simulator = TrafficSignInterpretionSimulator(
    development_mode=d_mode,
    model=model,
    size="small",
    background_address="assets/images/simulator/default.jpg")
required_action = ""
predicted_type = ""
running = True
while running:
  vehicle_state, data = simulator.step(action=required_action,
                                       user_type=predicted_type)
  if data is not None:

    # extract perception data
    host_speed = vehicle_state.host_speed
    host_lane = vehicle_state.host_lane

    # TODO: predict traffic sign type
    image = data_prep(data)
    features = feature_extraction(image)
    predicted_type = model_predict(model, features)

    # TODO: control host vehicle base on traffic sign
    """
      school-zone --> speed 20
      keep-right --> travel in the right lane
      keep-left --> travel in the left lane
      stop --> speed 0
      headlights-on --> headlights-on
      headlights-off --> headlights-off
    """
    requied_action = ""

    if predicted_type == "school-zone":
      if host_speed > 20:
        required_action = "speed-down"
      elif host_speed < 20:
        required_action = "speed-up"
      else:
        required_action = ""

    elif predicted_type == "keep-right":
      if host_lane == 0:
        required_action = "shift-right"
      else:
        required_action = ""

    elif predicted_type == "keep-left":
      if host_lane == 1:
        required_action = "shift-left"
      else:
        required_action = ""

    elif predicted_type == "stop":
      required_action = "stop"

    elif predicted_type == "headlights-on":
      required_action = "headlights-on"

    elif predicted_type == "headlights-off":
      required_action = "headlights-off"

    elif predicted_type == "speed-limit":
      if host_speed > 40:

        required_action = "speed-down"
      elif host_speed < 40:

        required_action = "speed-up"
      else:
        required_action = ""

    else:
      required_action = ""

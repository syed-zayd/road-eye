import os

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score

from mathstropy.ml import (
    get_label_from_filename,
    load_model,
    model_predict,
)
from mathstropy.image_processing import load_image
from libs.preprocessing import data_prep, feature_extraction

# Get the path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
training_image_dir = script_dir + "/assets/images/test"
images_files = os.listdir(training_image_dir)

# load model
model = load_model(script_dir + "/model/model.pkl")

gnd_truths = []
predictions = []
# iterate through each test image
for image_filename in images_files:
  raw_image = load_image(training_image_dir + "/" + image_filename)

  image = data_prep(raw_image)

  feature = feature_extraction(image)

  label = get_label_from_filename(image_filename)

  prediction = model_predict(model, feature)

  gnd_truths.append(label["label"])
  predictions.append(prediction)

# Create confusion matrix
fig, ax = plt.subplots(tight_layout=True)
conf_matrix = ConfusionMatrixDisplay.from_predictions(
    gnd_truths, predictions, xticks_rotation="vertical", ax=ax)

print(f"Accuracy Score: {accuracy_score(gnd_truths, predictions)}")
plt.show()

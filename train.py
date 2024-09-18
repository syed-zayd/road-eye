import os

import pandas as pd
from libs.preprocessing import data_prep, feature_extraction
from mathstropy import add_row, merge_dictionaries
from mathstropy.image_processing import load_image
from mathstropy.ml import (
    decision_tree_model_training,
    get_label_from_filename,
    save_model,
)

# get the path of the training image directory and file names
script_dir = os.path.dirname(os.path.abspath(__file__))
training_image_dir = script_dir + "/assets/images/train"
images_files = os.listdir(training_image_dir)


# ---------------------Preprocessing loop-----------------#
# initialize feature_i dict
features = {}
# initialize training data table
training_data = pd.DataFrame()

print("INFO: Running model training...")
for image_file in images_files:
    # load image
    raw_image = load_image(training_image_dir + "/" + image_file)

    # TODO: prepare data -- define in libs/preprocessing.py)
    resized_image = data_prep(raw_image)
    # TODO: extract features -- define in libs/preprocessing.py
    """REQUIRED: store features in variable 'features' """
    features = feature_extraction(resized_image)
      
    # get labels and add to features
    label = get_label_from_filename(image_file)
    row_data = merge_dictionaries(features, label)

    # add features and label to training list
    training_data = add_row(training_data, row_data)
# ------------------------------------------------------------#

# --------------------------Training---------------------------#
# TODO: train model using decision tree algorithm
"""
decision_tree_model_training()
Input:
- training data (table)
- max depth of tree (int)
"""
model = decision_tree_model_training(training_data, 6)

# TODO: save model
"""
save_model()
Input:
- model
- path
Returns:
- model (DecisionTreeClassifer)
"""

model_path = f"{script_dir}" + "/model/model.pkl"
save_model(model, model_path)


# ------------------------------------------------------------#
print("INFO: Model training done!")

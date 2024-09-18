import os

import matplotlib.pyplot as plt
from mathstropy.ml import load_model
from sklearn import tree

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = script_dir + "/model/model.pkl"
model = load_model(model_path)

fig, ax = plt.subplots(tight_layout=True)
tree.plot_tree(model,
               ax=ax,
               feature_names=list(model.feature_names_in_),
               filled=True,
               impurity=False,
               fontsize=6,
               class_names=list(model.classes_))
# plt.tight_layout()
plt.show()

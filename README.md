# 🚗 Traffic Sign Detection and Autonomous Vehicle Control

**STEM Hacks 2023 - First Place Winner!** 🏆

This project is a winning solution from STEM Hacks 2023, where the challenge was to create an autonomous vehicle (AV) system that responds to traffic signs using machine learning (ML) techniques. The project integrates Pygame for simulation and scikit-learn (sklearn) for model training.

## Project Overview

The goal was to build a model that detects traffic signs and integrates with a control algorithm to guide an autonomous vehicle in a simulated environment.

## How It Works

### Traffic Sign Detection

1. **Preprocessing and Feature Extraction**
   - Implemented preprocessing and feature extraction functions to prepare data for the ML model.
   - Trained a decision tree model using scikit-learn with 100% accuracy.

2. **Testing and Visualization**
   - Evaluated model performance using a provided script.
   - Visualization of model decisions can be viewed after running `main.py` in performance mode.

### Autonomous Vehicle Control

- **Integration**: The trained model is used to control the AV based on traffic sign detections.
- **Control Logic**: The vehicle adjusts speed, lane, and other actions according to traffic sign labels.
- **Simulator Actions**: Includes speed adjustments, lane changes, and headlight controls.

## Results

- **Model Accuracy**: 100% 🎯. Our model worked for all 56 test images provided.
- **Performance**: Can be reviewed after running `main.py` in performance mode.

## Run the Project
1. **Run Locally**
   - Install required dependencies: `poetry install`
   - Train the model: `python train.py`
   - Test the model: `python test.py`
   - Run the simulator: `python main.py` (view performance metrics in production mode)
2. **Alternatively, Run on Replit**
   - Project can be demoed on [Replit](https://replit.com/@KingOfCold/STEM-Hacks-2023#main.py)

## Event Page

For more details about STEM Hacks 2023, visit the event's page: [STEM Hacks 2023](https://mathstronauts.ca/stem-hacks-2023/)

## Acknowledgements

- Mathstronauts, and everyone who helped create this event for the challenging and exciting competition.
- Team members: Asad Rizvi, Asghar Rizvi, Hassaan Naz, and Syed Taymoor Ahmad
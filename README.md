# DiabetesPredictor
Diabetes Prediction using Random Forest Classifier.

Hello folks, this is my first project in Machine Learning Using Flask.

The project predicts whether a patient is diabetic or not using Random Forest Classifier which builds multiple decision trees and merges them together to get a more accurate and stable result.

Training Accuracy : 0.9870

Testing Accuracy : 0.7100

The dataset was obtained from Kaggle : https://www.kaggle.com/uciml/pima-indians-diabetes-database

A form was designed to take the inputs from the user which were passed as a parameter to our predict function which uses Random Forest Classifier (Supervised Learning) to classify the patients as diabetic or non-diabetic.The form was designed in HTML/CSS.

Following were the inputs taken from the end user :

1.	Number of Pregnancies
2.	Glucose Level
3.	Blood Pressure Level
4.	Skin Thickness
5.	Insulin
6.	BMI


GUI for end user interaction was developed using Flask Framework and HTML/CSS in the Frontend and Python in the backend for developing the controller files and model files.


Results:

Diabetic if the predicted value is ‘1’.

Non-Diabetic if the predicted value is ‘0’.


Inorder to execute it :

1] Write the following command in cmd : controller.py

2] It will start the server and provide an url i.e. "http://127.0.0.1:5000" copy it in browser and see the magic !


At last, it was totally new experience for me at first sight I find it difficult but with the help of my friends, I was able to complete this so Thanks everyone. Hope you like it as well. 

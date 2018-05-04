import pandas as pd                    # pandas is a dataframe library
import matplotlib.pyplot as plt        # matplotlib.pyplot plot data
import numpy as np                     # numpy provides N-dim object support

df = pd.read_csv("diabetes.csv") # load Pima data. Adjust path as necessary

# print(df.shape)  => (768,9)

# print(df.isnull().values.any()) # Checking for null values => False

# print(df.head())  #Prints first five records


from sklearn.model_selection import train_test_split

feature_col_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
predicted_class_names = ['Outcome']

X = df[feature_col_names].values # predictor feature columns (8 X m)
y = df[predicted_class_names].values # predicted class (1=true, 0=false) column (1 X m)
split_test_size = 0.30

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42)


from sklearn.preprocessing import Imputer

#Impute with mean all 0 readings
fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)

X_train = fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)


from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
rf_model = RandomForestClassifier(random_state = 42) # Create random forest object
rf_model.fit(X_train, y_train.ravel())

rf_predict_train = rf_model.predict(X_train)
# training metrics
#print("Accuracy: {0:.4f}".format(metrics.accuracy_score(y_train, rf_predict_train)))
rf_predict_test = rf_model.predict(X_test)
# training metrics
print("Accuracy: {0:.4f}".format(metrics.accuracy_score(y_test, rf_predict_test)))



def RFPredict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
  X_new = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
  X_new = X_new.reshape(1,8)
  rf_predict = rf_model.predict(X_new)
  # training metrics
  rf_predict = int(rf_predict)
  print(rf_predict)
  return rf_predict;



#RFPredict(6, 148, 72, 35, 0, 33.6, 0.627, 50)


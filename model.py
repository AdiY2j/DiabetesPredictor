from wtforms import Form, FloatField,StringField, validators
from math import pi

class InputForm(Form):
    Pregnancies = FloatField(
        label='Pregnancies',
        validators=[validators.InputRequired()])
    Glucose = FloatField(
        label='Glucose',
        validators=[validators.InputRequired()])
    BloodPressure = FloatField(
        label='BloodPressure', 
        validators=[validators.InputRequired()])
    SkinThickness = FloatField(
        label='SkinThickness', 
        validators=[validators.InputRequired()])
    Insulin = FloatField(
        label='Insulin',
        validators=[validators.InputRequired()])
    BMI = FloatField(
        label='BMI',
        validators=[validators.InputRequired()])
    DiabetesPedigreeFunction = FloatField(
        label='DiabetesPedigreeFunction',
        validators=[validators.InputRequired()])
    Age = FloatField(
        label='Age',
        validators=[validators.InputRequired()])

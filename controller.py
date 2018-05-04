from model import InputForm
from flask import Flask, render_template, request
from app import RFPredict
import sys
global result,resul1

app = Flask(__name__)

try:
    template_name = sys.argv[1]
except IndexError:
    template_name = 'view'

if template_name == 'view_flask_bootstrap':
    from flask_bootstrap import Bootstrap
    Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = RFPredict(form.Pregnancies.data,form.Glucose.data, form.BloodPressure.data,
                         form.SkinThickness.data, form.Insulin.data, form.BMI.data, form.DiabetesPedigreeFunction.data, form.Age.data)
    else:
        result = None
    print (form, dir(form))
    #print form.keys()
    #for f in form:
    #    print (f.id)
    #    print (f.name)
    #    print (f.label)
    if(result == 1):
        result = "Diabetic Patient , Needs A Treatment :("
    if(result == 0):
        result = "Non - Diabetic Patient , But Be Concious :)"
    return render_template(template_name + '.html',form=form,result1 = result)

if __name__ == '__main__':
    app.run(debug=True)
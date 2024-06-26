from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

model=pickle.load(open('/home/sdantre/mysite/trained_model/model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    #int_features = [int_features[0],int_features[1]]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('result.html',pred='You need a treatment.\nProbability of mental illness is {}'.format(output))
    else:
        return render_template('result.html',pred='You do not need treatment.\n Probability of mental illness is {}'.format(output))
@app.route('/next_page')
def next_page():
    # Add any necessary logic here before rendering the template
    return render_template('next_page.html')

if __name__ == '__main__':
    app.run(debug=True)


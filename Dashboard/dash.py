from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd

app = Flask(__name__)

#halaman home
@app.route('/')
def home():
    return render_template('home.html')

#halaman dataset
@app.route('/database', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html')

# #halaman visualisasi
@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

# #halaman input prediksi
@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    return render_template('predict.html')

# #halaman hasil prediksi
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        hr_pred = pd.DataFrame({
            'department': [input['dept']],
            'region': [input['reg']],
            'education': [input['edu']],
            'gender': [input['gender']],
            'recruitment_channel': [input['recch']],
            'no_of_trainings' : [input['nof']],
            'age': [input['age']],
            'previous_year_rating': [input['pyr']],
            'length_of_service': [input['los']],
            'KPIs_met >80%': [input['kpi']],
            'awards_won?': [input['awards']],
            'avg_training_score' : [input['avg']]
        })

        prediksi = model.predict_proba(hr_pred)[0][1]

        if prediksi > 0.8:
            promote = "Promoted"
        else:
            promote = "Not Promoted"

        return render_template('result.html',
            data=input, pred=promote)

if __name__ == '__main__':
    # model = joblib.load('model_joblib')

    filename = '/Users/rezkydwiseptiyan/Documents/Purwadhika Data Science/Final Project/hr-analytic-new.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)
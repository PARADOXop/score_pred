from flask import Flask, render_template, request, jsonify
import pickle
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def index():
    return render_template('index.html')


@app.route('/predictdata', methods = ["POST", "GET"])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == "POST":
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethinicity = request.form.get('ethinicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))    
    )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = predict_pipeline()
        results = predict_pipeline.predict(pred_df)
        print(results)
        return render_template('home.html', results = results[0])
@app.route('/postman', methods=['GET', 'POST']) # To render Homepage
def mathss():
    if request.method != "POST":
        return "no input given so no operation thanks"
    operation = request.json['operation']
    num1 = int(request.json['num1'])
    num2 = int(request.json['num2'])
    if operation == 'multiply':
        r = num1 * num2
        result = f'the product of {num1} and {num2} is {str(r)}'
    elif operation == 'subtract':
        r = num1 - num2
        result = f'the difference of {num1} and {num2} is {str(r)}'
    elif operation == "add":
        r=num1+num2
        result = f'the sum of {num1} and {num2} is {str(r)}'
        r = num1 / num2
        result = f'the quotient when {num1} is divided by {num2} is {str(r)}'
    else:
        r = num1 / num2
        result = f'the quotient when {num1} is divided by {num2} is {str(r)}'
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
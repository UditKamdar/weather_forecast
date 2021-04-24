import pandas as pd
import numpy as np
import pickle
from flask import Flask, jsonify, request ,render_template
# from flask_cors import CORS, cross_origin

#import libraries

#Initialize the flask App
app = Flask(__name__)
# CORS(app)
maxT = pickle.load(open('forecast_model_maxT.pkl', 'rb'))
minT = pickle.load(open('forecast_model_minT.pkl', 'rb'))

print("working")

#default page of our web-app
@app.route('/')
def home():
    print("working good")
    return "<h1>HIIIII</h1>"
#     return render_template('index.html',prediction_text='The second batting team will win the match')

@app.route('/api')
def home1():
    print("working good")
    future2 = maxT.make_future_dataframe(periods=365)
    forecast = maxT.predict(future2)
    df1 = pd.DataFrame(forecast)
    df2 = df1[['ds','yhat']]
    df2['ds'] = df2['ds'].astype(str)
    return "<h3>BYRRRR</h3>"
#     return render_template('index.html',prediction_text='Hello')
@app.route('/hi')
def home12():
    print("working good")
    return "HIIII"
@app.route('/trial')
def trial():
    d={}
    d['Query'] = str(request.args['Query'])
    return jsonify(d)

if __name__ == "__main__":
    app.run()
#To use the predict button in our web-app
# @app.route('/predict',methods=['POST'])
# def predict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     print("Reached")
#     future2 = maxT.make_future_dataframe(periods=365)
#     forecast2 = maxT.predict(future2)
#     # output = round(prediction[0], 2)
    
#     print(output)
#     #  return render_template('index.html', prediction_text='The second batting team will  :{}'.format(output))
    
#     return render_template('index.html', prediction_text='The second batting team will win the match')
   
     

# app = Flask(__name__)
# CORS(app)
# maxT = pickle.load(open('forecast_model_maxT.pkl', 'rb'))
# minT = pickle.load(open('forecast_model_minT.pkl', 'rb'))
# print("working")
# # with open('forecast_model_maxT.pkl', 'rb') as fin:
# #     m2 = pickle.load(fin)
# @app.route("/")
# def predict1():
#     # horizon = int(request.json['horizon'])
    
#     # future2 = maxT.make_future_dataframe(periods=365)
#     # forecast2 = maxT.predict(future2)
    
#     # data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()
    
#     # # data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
#     # ret = data.to_json(orient='records', date_format='iso')
#     # print(ret)
    
#     return ret
# # running REST interface, port=3000 for direct test

# @app.route('/agriculture-assistance.herokuapp.com/api',methods=['GET'])
# def predict():
#     d={}
#     d['Query'] = str(request.args['Query'])
    
#     return jsonify(d)

# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

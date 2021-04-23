import numpy as np
import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
maxT = pickle.load(open('forecast_model_maxT.pkl', 'rb'))
minT = pickle.load(open('forecast_model_minT.pkl', 'rb'))
print("working")
# with open('forecast_model_maxT.pkl', 'rb') as fin:
#     m2 = pickle.load(fin)
@app.route("/")
def predict1():
    # horizon = int(request.json['horizon'])
    
#     future2 = maxT.make_future_dataframe(periods=365)
#     forecast2 = maxT.predict(future2)
    
#     data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()
    
#     # data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
#     ret = data.to_json(orient='records', date_format='iso')
#     print(ret)
    
    return "hey"
# running REST interface, port=3000 for direct test

@app.route('/agriculture-assistance.herokuapp.com/api',methods=['GET'])
def predict():
    d={}
    d['Query'] = str(request.args['Query'])
    
    return jsonify(d)

if __name__ == "__main__":
    app.run(debug=True)

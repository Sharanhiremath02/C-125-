from flask import Flask,jsonify,request
from C_125 import get_prediction
from cv2 import cv2


app=Flask(__name__)
@app.route("/")
def hello():
    return("Hello How Are You")

@app.route("/predict-digit",methods=["POST"])
def predict_data():
    image=request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify({
        "prediction":prediction
    }), 200

if(__name__ == "_main_"):
    app.run(debug=True)


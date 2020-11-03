from flask import Flask, request, jsonify
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from test import plant_prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        #modelPath = 'research/ssd_mobilenet_v1_coco_2017_11_17'
        self.objectDetection = plant_prediction(img_name=self.filename)


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.objectDetection.predict_label()
    return jsonify(result)


port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=7000, debug=True)

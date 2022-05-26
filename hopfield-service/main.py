import helper
from flask import Flask, request, Response, json, render_template
from flask_cors import CORS
import json
import os

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

directorio = os.getcwd()

#Sube la imagen
@app.route('/upload-image', methods=['POST'])
def upload_image():
    res_data = helper.upload_image(request)

    if res_data is None:
        response = Response("{'error': 'Fail to process'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#Procesa la imagen
@app.route('/process', methods=['GET'])
def process():
       

    # Add item to the list
    res_data = helper.process()

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Fail to process'}", status=500 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response


if __name__ == '__main__':
    helper.start()
    app.run(debug=True, use_reloader=True, port=4455)
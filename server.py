from pymongo import MongoClient
import json
from bson import json_util
from flask import Flask, request, jsonify, make_response
from base64 import b64encode
app = Flask(__name__)
client = MongoClient("mongodb+srv://qtma:qtma2019@lucyar-eojj4.mongodb.net/test?retryWrites=true")


def getCollection(db_name, coll_name):
    db = (client[db_name])
    collection = db[coll_name]
    return collection


@app.route('/models/<filename>.gltf', methods=['GET'])
def getGLTF(filename):
    coll = getCollection("models", "gltf")
    filename += ".gltf"
    response = coll.find({"filename": filename})[0]['file']
    j = json.loads(json_util.dumps(response))
    return jsonify(j)


@app.route('/models/<filename>.bin', methods=['GET'])
def getBIN(filename):
    coll = getCollection("models", "gltf")
    filename += ".bin"
    query = coll.find({"filename": filename})[0]['file']
    response = make_response(query)
    response.mimetype = "binary/octet-stream"
    return response


if __name__ == '__main__':
    app.run()







from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import pymongo
from bson.json_util import dumps
from flask_pymongo import PyMongo
import os
from paho.mqtt import client as mqtt_client
from bson import ObjectId
from minio import Minio
from minio.sse import SseCustomerKey
import urllib3
import datetime
import sys
import hashlib
try:
	client = Minio(
		"192.168.56.105:9000",
		access_key = "admin",
		secret_key = "password@31",
		secure = False,
	)
	print("Checking at ", datetime.datetime.now())
	client.bucket_exists("bucket_name")
except Exception as e:
	print(f"Error checking bucket. {e}. Error at ", datetime.datetime.now())
# Download data of an object.

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_URI'] = "mongodb://localhost:27017/admin"
mongo = PyMongo(app)
dbenter = mongo.db.DataGet
dbGet = mongo.db.DataArchive
# broker = 'broker.mqtt-dashboard.com'
# port = 1883
# topic = "testapi/123"
# client = mqtt_client.Client()
# client.connect(broker, port)
# client.loop_start()
@app.route("/dataentry", methods=["POST","GET"])
def submit_data():
    
    if request.method == "POST":

        post_data = request.get_json()
        # data = {
        #     "IP"        : post_data.get('Object'),
        #     "Path"    : post_data.get('Bucket'),
        #     "username"        : post_data.get('Folder')
        # }
        s=json.dumps(data)
        client.fget_object(post_data.get('Bucket'), post_data.get('Object'), post_data.get('Folder'))
        #read metadata
        s=client.stat_object(post_data.get('Bucket'),post_data.get('Object'))
        HashMetadataObject=dict(s.metadata.items())["ETag"]
        # BUF_SIZE is totally arbitrary, change for your app!
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
        #check hash
        md5 = hashlib.md5()
        sFile=post_data.get('Folder')
        with open(sFile, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
        HashCodeDL=md5.hexdigest()
        if HashCodeDL == HashMetadataObject[1:(len(HashMetadataObject)-1)]:
            abc="Backup success"
        else:
            abc="Backup error"
        # client.publish(topic, s)
        response_object = {'status':abc}
        
        return abc
        
    

        
    


@app.route("/view", methods=["POST","GET"])
def view_data():

    data=dumps(dbenter.find())
    return data



if __name__ == '__main__':
    
    app.run(debug=True)
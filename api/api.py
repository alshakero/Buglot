# @Author: Fadi Hanna Al-Kass (ceo@shaykeapp.com)

from flask_restful import Resource, Api
from random import randint
import shortuuid
from web import webApp


api = Api(webApp)

class SubmitHandler(Resource):
    def post(self):
        return {"message" : "Submitted Successfully"}, 201
api.add_resource(SubmitHandler, "/submit/")

class Query(Resource):
    def get(self):
        shortuuid.set_alphabet("1234567890")
        data = {}
        data["data"] = []
        for i in range(200):
            tempData = {}
            tempData["_id"] = shortuuid.uuid()[:10]
            tempData["platform"] = ("Android", "iOS", "Windows Phone")[randint(0, 2)]
            tempData["release"] = ("1.0.0", "1.0.2", "2.1.2", "3.2.6", "4.0.0")[randint(0, 4)]
            tempData["exception_type"] = ("IntentException", "NetworkUnreachableException", "InvalidParameterException", "CameraCrashException")[randint(0, 3)]
            tempData["class"] = ("MainActivity", "CameraLoader", "MediaHandler", "MediaUploader", "Message", "VoiceCallHandler")[randint(0, 5)]
            tempData["function"] = ("onCreate", "onDestroy", "sendText", "sendVideo", "sendVoice", "sendImage", "onResume")[randint(0, 6)]
            tempData["line_num"] = range(100)[randint(0, 99)]
            tempData["num_reports"] = range(100)[randint(1, 99)]
            tempData["status"] = ("Reported", "Resolved", "Reviewed")[randint(0, 2)]
            data["data"].append(tempData)
        return data
api.add_resource(Query, "/query/")

def run(host, port, debug, rdb):
    global db
    db = rdb
    print(" * HOST: %s, PORT: %d, DEBUG: %s" % (host, port, debug))
    webApp.run(host=host, port=port, debug=debug)

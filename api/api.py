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
        dummyJsonList = []
        for i in range(5):
            dummyJson =\
            {
                "_id" : shortuuid.uuid()[0:10],
                "platform" : ("Android", "iOS")[randint(0, 1)],
                "release" : ("1.0.0", "1.7.0", "2.0.2", "3.5.2", "7.1.0")[randint(0, 4)],
                "exception_type" : ("IOException", "NetworkAdapterException", "IntentException", "InvalidParameterException")[randint(0, 3)],
                "class" : ("MainActivity", "MediaHandler", "Camera")[randint(0, 2)],
                "function" : ("onCreate", "onStart", "onPause", "onResume", "onDestroy", "loadFragment", "loadImage", "startCamera", "sendRawRecording")[randint(0, 8)],
                "line_num" : randint(0, 25),
                "num_reports" : randint(0, 100),
                "status" : ("Reported", "Resolved", "Review")[randint(0, 2)]
            }
            dummyJsonList.append(dummyJson)
        return dummyJsonList
api.add_resource(Query, "/query/")

def run(host, port, debug, rdb):
    global db
    db = rdb
    print(" * HOST: %s, PORT: %d, DEBUG: %s" % (host, port, debug))
    webApp.run(host=host, port=port, debug=debug)

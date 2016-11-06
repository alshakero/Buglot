from flask_restful import Resource, Api
from random import randint
from web import webApp, db


api = Api(webApp)

class Query(Resource):
    def get(self):
        dummyJsonList = []
        for i in range(10):
            dummyJson =\
            {
                "_id" : i,
                "platform" : ("Android", "iOS")[randint(0, 1)],
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

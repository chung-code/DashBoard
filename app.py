from flask import Flask, request
from flask_cors import CORS, cross_origin

import pymongo
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import random
import json

def get_documents( 
    connection_string = "mongodb://sdpygl:sdp_ygl@3.36.175.233:27017/admin",
    db_name = "visualization",
    collection_name = "map"
    ) : 
    
    client = pymongo.MongoClient(connection_string)
    visualization = client[db_name]

    collection_map = visualization[collection_name]
    collection_map.create_index([("project_name_wb", pymongo.TEXT)], unique = True)

    return collection_map

class preprocessing():
    def __init__(self, db):        
        self.result = db.find()
        self.df = pd.json_normalize(self.result)
    
        self.pn_col = np.array(self.df['properties.project_name_wb'])
        self.id_col = np.array(self.df['_id'])

        self.data_df = self.df.drop(['_id', 'type', 'geometry.type', 'geometry.coordinates',
               'properties.country', 'properties.project_name_wb',
               'properties.project_name_common',
               'properties.segment', 'properties.crossborder',
               'properties.reason_for_delay', 'properties.investment',
               'properties.project_bank', 'properties.delayed_extent',
               'properties.fc_year',
               'properties.fc_year_reason', 'properties.ppi_status',
               'properties.affected_stage', 'properties.type_of_ppi',
               'properties.urls', 'properties.resumed', 'properties.resume_url',
               'properties.location'], axis=1)
        
docs = get_documents()
data = preprocessing(docs)
df = data.data_df

result = df.to_json(orient="split")


# dash_data = [12, 19, 3, 5, 2, 3]
# M = dict(zip(range(1, len(dash_data) + 1), dash_data))
# json.dumps(M)

M = {"data" : [12, 19, 3, 5, 2, 3]}

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "hello"

@app.route("/get")
def mongo():
    return result

@app.route("/dash")
def dashboard():
    return M

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
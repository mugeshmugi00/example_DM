from pymongo import MongoClient

local = MongoClient("mongodb://localhost:27017/")

db = local.mugesh_database

coll = db.admin_collection

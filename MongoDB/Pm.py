# Python->PyMongo
from pymongo import MongoClient

# Connect to a remote MongoDB 
client = MongoClient("mongodb://jackson:990731@192.168.0.14:27017/Solutions")

solution=client.Solutions.BCPoints
print(solution.find())




# db.createUser({user:"jackson",pwd:"990731",roles:[{role:"dbAdmin",db:"test"}]})
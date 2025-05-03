from flask import Flask,jsonify,request
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
mongo_url = os.getenv("mongo_url")


from pymongo.mongo_client import MongoClient

# Create a new client and connect to the server
client = MongoClient(mongo_url)
db = client.test
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
collection = db['flask-tutorial']
    
app = Flask(__name__)





@app.route('/submit',methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return "The submit of data is confirmed"

    

@app.route('/view')
def view():
    data = collection.find()
    return dict(data)
    

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.json.get('itemName')
    item_description = request.json.get('itemDescription')

    # Store the to-do item in the MongoDB database
    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description,
        "createdAt": datetime.now()
    }
    collection.insert_one(todo_item)

    return jsonify({
        "message": "To-Do item submitted successfully",
        "itemName": item_name,
        "itemDescription": item_description
    })


if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=5000,debug=True)




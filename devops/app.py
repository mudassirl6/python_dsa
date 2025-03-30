from flask import Flask,jsonify,request,render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')

def home():
    day_of_week = datetime.today().strftime('%A')
    return render_template('index.html',day_of_week=day_of_week)

@app.route('/time')
def time():
    return datetime.now().strftime('%H:%M:%S')
@app.route('/about')
def about():
    return jsonify({'info': 'This is a simple Flask app!'})


# @app.route('/api/<name>')
# def name(name):
#     print(name)
#     return jsonify({name: 'This is a name simple Flask app!'})

@app.route('/api')
def name():
    name = request.values.get('name')
    age = request.values.get('age')
    return jsonify({"name":name,"age":age})
    
@app.route('/add/<a>/<b>')
def add(a,b):
    
    res = int(a)+int(b)
    result = {"result":res}
    return jsonify(result)

if __name__ == '__main__':
    
    app.run(debug=True)
    
    
    
# Your app.py file looks fine, but here are some potential enhancements based on what you might need:

# 1. Add CORS Support (For Frontend Integration)

# If you’re planning to call this API from a frontend (React, Vue, etc.), add CORS support:


# from flask import Flask, jsonify
# from flask_cors import CORS  # Import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# @app.route('/')
# def home():
#     day_of_week = datetime.today().strftime('%A')
#     print(day_of_week)
#     return jsonify({'message': 'Hello Guys'})

# if __name__ == '__main__':
#     app.run(debug=True)

# # Why is CORS Important?

# # If your Flask API is hosted on http://localhost:5000, 
# # and your frontend is on http://localhost:3000, the
# # browser will block requests from the frontend due
# # to CORS policy unless explicitly allowed.

import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:hEzsvuNPe20opxCn@cluster0-js43a.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# # -------------------------------------------------------------------------------------------------------------------

@app.route('/')
@app.route('/index')

def index():
    #connect to the Mongo DB
    collection = mongo.db.events
    files = list(collection.find({}))
    print(files)
    return render_template('index.html', files=files)


# ---------------------------------------------------------------------------------------------------------------------

@app.route('/results', methods = ["get", "post"])
def results():

    user_info = dict(request.form)
    print(user_info)


    clientname = user_info["clientname"]
    print("the client name is ", clientname)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    filename = user_info["filename"]
    print("the file name is ", filename)

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    filelocation = user_info["filelocation"]
    print("the file location is ", filelocation)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    filelocation = user_info["filelocation"]
    print("the file location is ", filelocation)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    activity = user_info["activity"]
    print("the clients status is ", activity)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
    creationdate = user_info["creationdate"]
    print("the file was created on ", creationdate)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––



    collection = mongo.db.events

    collection.insert({"clientname": clientname, "filename": filename, "filelocation": filelocation, "activity": activity, "creationdate": creationdate})

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    return redirect('/index')


    collection = mongo.db.events


    return redirect('/index')

# ---------------------------------------------------------------------------------------------------------------------

@app.route('/delete')
def delete():
    collection = mongo.db.events

    collection.delete_many({})

    return redirect('/index')

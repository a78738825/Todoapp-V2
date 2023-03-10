from flask import Flask, render_template, request, url_for, redirect
# from flask_pymongo import PyMongo
from datetime import datetime
import sqlite3
from sql_commander import Commander
import json


app = Flask(__name__)

# Sqllite connection
try:
    sql_db = sqlite3.connect("database.db", check_same_thread=False)
    sql_cursor = sql_db.cursor()
    try:
        commander = Commander(db=sql_db, cursor=sql_cursor)
        commander.createTable()
    except Exception as creatingError:
        print("Error while creating table !!", str(creatingError))
except Exception as err:
    print("Sqllite connection failed Error Occured:", str(err))


# Flask -> MongoDB configuration :--- REMOVED FEATURE
# app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskdb"
# mongo = PyMongo(app)
# collection = mongo.db.collection
# cursor = list(collection.find({}, {"_id": 0}))



@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/create")
def create_user() -> str:
    return render_template("create.html")


@app.route("/post", methods=["GET", "POST"])
def save_form():
    if request.method == "POST":
        try:
            todo_title = request.form["todo_title"]
            todo_desc = request.form["todo_desc"]
            commander.insertData(
                data=(todo_title, todo_desc, datetime.now()),
            )
        except Exception as e:
            print("ERROR : ", str(e))
    # elif request.method == "GET":
    #     print("GET method")
    else:
        print("error")

    return redirect(url_for("show_table"))


@app.route("/show")
def show_table():
    allData = commander.readData()
    json_format = {
        "Title": allData[0],
        "Description": allData[1],
        "Created": allData[2],
    }
    print(json.dumps(json_format, sort_keys=True, indent=4))
    print("\nType = ", type(allData))
    return render_template("show.html", allData=allData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

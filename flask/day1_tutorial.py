# from flask import flask

# app = flask(__name__)

# @app.route("/")

# def helloworld():
#     return  "Hello world"


from flask import Flask, request
from core import utils

app = Flask(__name__)
# users = [{"name":"virendra","salary":40},
#          {"name":"dilip","salary":40},
#          {"name":"bobby","salary":40},]
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getusers", methods=['GET'])
def getusers():
    # to be implemented
    # call mongo method to get all users
    users = utils.read_db_file()
    all_user_names = [i.get("name") for i in users]
    return all_user_names

@app.route("/get_spec_user", methods=['GET'])
def get_specific_user_details():
    args = request.args
    users = utils.read_db_file()
    if "user_name" in args:
        user = args.get("user_name")
        for i in users:
            if i["name"]==user:
                return i      
    return "user not found"

@app.route("/save_user", methods=['POST'])
def saveuser():
    # to be implemented
    # call mongo method to get all users
    user_data = request.json
    users = utils.read_db_file()
    users.append(user_data)
    return utils.write_db_file(users)
    
    return 

if __name__ == "__main__":
    app.run(debug=True)



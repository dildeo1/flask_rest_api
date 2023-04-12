import json
from core.config import DB_FILE

def read_db_file():
    db_data = json.load(open(DB_FILE,"r"))
    return db_data

def write_db_file(inp_dict):
    json.dump(inp_dict,open(DB_FILE,"w"))
    return "Sucessfully updated db"
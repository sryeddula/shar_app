import sqlite3
from datetime import datetime


# create sqlite table
def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS votes (Id INTEGER, PostId INTEGER, UserId INTEGER, VoteTypeId INTEGER, CreationDate DATETIME)")
    conn.commit()
    conn.close()


def insert(Id, PostId, UserId, VoteTypeId, CreationDate):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO votes VALUES (?,?,?,?,?)", (Id, PostId, UserId, VoteTypeId, CreationDate))
    conn.commit()
    conn.close()
    
def read_json():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    i=0
    import json
    with open('votes.jsonl', 'r') as jsonFile:
        for jf in jsonFile:
            jf = jf.replace('\n', '')
            jf = jf.strip()
            data = json.loads(jf)
            Id = int(data['Id'] if 'Id' in data else 0)
            PostId = int(data['PostId'] if 'PostId' in data else 0)
            UserId = int(data['UserId'] if 'UserId' in data else 0)
            VoteTypeId = int(data['VoteTypeId'] if 'VoteTypeId' in data else 0)
            CreationDate = data['CreationDate']
            cur.execute("INSERT INTO votes VALUES (?,?,?,?,?)", (Id, PostId, UserId, VoteTypeId, CreationDate))
            # insert(Id, PostId, UserId, VoteTypeId, CreationDate)
            i+=1
            if(i%1000==0):
                print(i)
                conn.commit()
    conn.commit()
    conn.close()

create_table()        
read_json()
from flaskApp import app
from flask import render_template, send_from_directory, request
import os
import pymysql

TABLE_NAME = "Computers"
ATTRIBUTES = ['computer_name', 'os_type', 'os_version', 'build_number']    

def create_mysql_connection():
    return pymysql.connect(host=os.getenv('MYSQL_URL'),
                                user=os.getenv('MYSQL_USER'),
                                password=os.getenv('MYSQL_PASSWORD'),
                                db=os.getenv('MYSQL_DB'),
                                cursorclass=pymysql.cursors.DictCursor)


# ------------------------------------------------
# render dummy dashboard 
#   > currently only fetches the data from DB.
# ------------------------------------------------
@app.route('/')
def index():
    conn = create_mysql_connection()
    sql = "SELECT * FROM {}".format(TABLE_NAME)
    conn.execute(sql)
    print([computer for computer in conn.fetchall()])
    return "test"
    # return render_template('index.html')

# ------------------------------------------------
# This POST request to be called from scheduled powershell script
# ------------------------------------------------
@app.route('/write',methods=['POST'])
def write():
    conn = create_mysql_connection()
    attributes = ATTRIBUTES
    values = {attributes[index]: request.form[attr] for index, attr in enumerate(attributes)}
    
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO {} 
                ({},{},{},{}) 
            VALUES 
                ("{}","{}","{}","{}")
            ON DUPLICATE KEY UPDATE
                {} = VALUES({}),
                {} = VALUES({}),
                {} = VALUES({});
            """.format(
                TABLE_NAME, attributes[0], attributes[1],attributes[2],
                attributes[3],values[attributes[0]], values[attributes[1]],values[attributes[2]], 
                values[attributes[3]], attributes[1], attributes[1], attributes[2], 
                attributes[2], attributes[3], attributes[3]
            )
            print(sql)
            cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()
        return "Saved successfully."

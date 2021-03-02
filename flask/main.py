from flask import Flask, request, jsonify
import mysql.connector
app = Flask(__name__)

def createConnection():
    con = mysql.connector.connect(
            host="scrap_sql",
            user="root",
            database = "my_db_scrap",
            password="123",
    )
    return con


@app.route('/')
def index():
    return  'hello'

@app.route('/wiki', methods=['GET'])
def articles():
    con=createConnection()
    result_dict = []
    cursor = con.cursor(dictionary=True)
    sql = "SELECT * FROM articles"
    cursor.execute(sql)
    for i in cursor:
        result_dict.append({'id': i['id'],'title': i['title'], 'image': i['image'], 'content':i['content'], 'date': i['date']})
    if 'id' in request.args:
            id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    resp = jsonify(result_dict)

    print(resp)

    
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
from flask import Flask, request, render_template, redirect, url_for
from db import mydb
app = Flask(__name__)

@app.route('/')
def index():
    return  'hello'

@app.route('/wiki')
def articles():
    cursor = mydb.cursor()
    sql = "SELECT * FROM articles"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('article.html', results=results)
    # return 'article'


if __name__ == "__main__":
    app.run(port=3050, debug=True)
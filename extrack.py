from flask import Flask,render_template,redirect,request,g,url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('/home/simeone/Documents/ExTrack/track.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db    

#Clos database connection automatically
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()




@app.route('/', methods=['GET','POST'])
def home():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        
        dt = datetime.strptime(date,'%Y-%m-%d')
        db_date = datetime.strftime(dt,'%Y%m%d')
       
        amount= int(request.form['amount'])
        expense= request.form['expense']

        db.execute('insert into trdate (toddate,Amount,Expense) values(?,?,?)',[db_date,amount,expense])
        db.commit()
        

    return render_template('home.html')

@app.route('/search', methods=['POST','GET'])
def search():
    db = get_db()
    if request.method == 'POST':

        use = request.form['lookup']

    cur = db.execute('select toddate,Amount,Expense from trdate where toddate =?'[request.form['lookup']])
    view_results = cur.fetchall()


    return render_template('search.html', view_results= view_results)

      


 


@app.route('/week')
def week():
    return render_template('week.html')

@app.route('/month')
def month():

    return render_template('month.html')
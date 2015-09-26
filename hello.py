from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def aboutlandingpage():
    return render_template('about.html')


@app.route('/Feed', methods = ['GET', 'POST'])
def getAd():
    if request.method == 'POST':
        selection = request.form['Events']


    #call selection on function that back-end people write and return relevant information

    return render_template("getAd.html", selection=selection)






if __name__ == "__main__":
    app.run()





#@app.route('/results.html', methods=['GET','POST'])
#def results():
#    g.db = connect_db()
#
#    cur = g.db.execute("SELECT * FROM all_items WHERE name = '{}'".format('Red'))
#    posts = [dict(item=row[0], name=row[1]) for row in cur.fetchall()]
#    g.db.close()
#    return render_template('results.html', posts=posts)

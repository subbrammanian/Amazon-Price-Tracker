from flask import Flask,render_template,request,json,jsonify
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('store.db')

conn.execute("create table if not exists MailingList(ID INTEGER PRIMARY KEY AUTOINCREMENT, EMAIL TEXT not NULL, URL TEXT NOT NULL);")


@app.route('/')
def main():
	return render_template("index.html")


@app.route('/submit',methods=['POST'])
def submit():
	_email = request.form['inputEmail'].strip()
	_url = request.form['inputPassword'].strip()

	if _email and _url:
		print _email,_url
		try:
			conn.execute("insert into MailingList(EMAIL,URL) values ('{email}','{url}');".format(email=_email,url=_url))
			conn.commit()
		except:
			return jsonify({"html":"Subscription failed. Please retry!"})
		
		return jsonify({"html":"Subscribed successfully. You will be updated if there is a price drop!"})

	else:
		return jsonify({"html":"Please enter both fields!"})


if __name__=="__main__":
	app.run()






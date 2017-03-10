from flask import Flask, render_template, request, jsonify
#import sqlite3


app = Flask(__name__)
#conn = sqlite3.connect('store.db')

#conn.execute("create table if not exists MailingList(ID INTEGER PRIMARY KEY AUTOINCREMENT, EMAIL TEXT not NULL, URL TEXT NOT NULL);")


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    _email = request.args.get('email', "", type=str)
    _url = request.args.get('url', "", type=str)
    print "email: ", _email
    print "url: ", _url

    return jsonify(result="successful")

    # if _email and _url:
    # print _email,_url
    # return jsonify({"html":"successful"})
    #   try:
    #       conn.execute("insert into MailingList(EMAIL,URL) values ('{email}','{url}');".format(email=_email,url=_url))
    #       conn.commit()
    #   except:
    #       return jsonify({"html":"Subscription failed. Please retry!"})

    # return jsonify({"html":"Subscribed successfully. You will be updated if
    # there is a price drop!"})

    # else:
    #   return jsonify({"html":"Please enter both fields!"})


if __name__ == "__main__":
    app.run()

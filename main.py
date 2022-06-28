from flask import Flask,jasonify,request
import csv


all_articles = []
with open("shared_articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]



liked_articles = []
not_liked_articles = []

app = Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })


@app.route("/liked-articles",methods = ["POST"])
def liked_articles():
 articles = all_articles[0]
 all_articles = all_articles[1:]
 liked_articles.append(articles)
 return jsonify({
  "status":"success"
}),201


@app.route("/not-liked-articles",methods = ["POST"])
def not_liked_movies():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_movies.append(articles)
    return jsonify({
        "status":"success"
    }),201

if (__name__ == "__main__"):
    app.run()    

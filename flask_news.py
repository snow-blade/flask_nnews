from flask import Flask,render_template,url_for
from operator import itemgetter
import requests

app=Flask(__name__)
res1=requests.get("https://newsapi.org/v2/everything?q=android&pageSize=5&apiKey=9656a7dbfd1744f69f74e571c0223d64")
res2=requests.get("https://newsapi.org/v2/everything?q=Open-source&pageSize=5&apiKey=9656a7dbfd1744f69f74e571c0223d64")
res3=requests.get("https://newsapi.org/v2/everything?q=Linux&pageSize=5&apiKey=9656a7dbfd1744f69f74e571c0223d64")

articles=[]
res=res1.json()['articles']
for art in res:
    articles.append(art)
for x in res2.json()['articles']:
	articles.append(x)
for x in res3.json()['articles']:
	articles.append(x)
articles=sorted(articles,key=itemgetter('publishedAt'),reverse=True)
@app.route('/')
def home():
    return render_template('index.html',articles=articles)

if __name__ == '__main__':
    app.run(port=8050,debug=True)


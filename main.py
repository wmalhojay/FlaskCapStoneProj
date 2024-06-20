from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", all_posts=res)

@app.route('/blogPost/<num>')
def blogPost(num):
    res = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    p = Post(res, num)
    return p.getPost()

if __name__ == "__main__":
    app.run(debug=True)

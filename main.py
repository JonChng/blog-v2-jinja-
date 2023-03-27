from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/765925b48d59dda74f32").json()
print(posts)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blog_posts=posts)

@app.route("/post/<id>")
def get_post(id):
    for post in posts:
        if post['id'] == int(id):
            to_upload = post
    return render_template("post.html", data=to_upload)



if __name__ == "__main__":
    app.run(port=8000, debug=True)

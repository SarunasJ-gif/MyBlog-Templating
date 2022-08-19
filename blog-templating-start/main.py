from flask import Flask, render_template
from post import Post
import requests

url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=url)
all_data = response.json()
posts_list = []
for post_data in all_data:
    post = Post(post_data["id"], post_data["title"], post_data["subtitle"], post_data["body"])
    posts_list.append(post)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts_list)


@app.route("/post/<int:num>")
def get_post(num):
    post_param = None
    for post_ob in posts_list:
        if post_ob.title_id == num:
            post_param = post_ob
    return render_template("post.html", post=post_param)


if __name__ == "__main__":
    app.run(debug=True)

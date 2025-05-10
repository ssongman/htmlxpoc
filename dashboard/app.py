
from flask import Flask, render_template, request
from models import get_all_posts, get_post, create_post, update_post, delete_post
from time import sleep  # sleep 함수 임포트

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html", posts=get_all_posts())

@app.route("/health")
def health():
    for i in range(5):
        print(f"Progress: {i + 1} second(s) elapsed")
        sleep(1)  # 1초 대기
    return "health OK!"

@app.route("/posts/fragment")
def list_posts():
    return render_template("post_list_fragment.html", posts=get_all_posts())

@app.route("/posts/new")
def new_post():
    return render_template("post_form_create.html")

@app.route("/posts", methods=["POST"])
def create():
    title = request.form["title"]
    content = request.form["content"]
    create_post(title, content)
    # return render_template("post_list_fragment.html", posts=get_all_posts())
    return render_template("post_list_wrapper.html", posts=get_all_posts())

@app.route("/posts/<int:post_id>/edit")
def edit_post(post_id):
    post = get_post(post_id)
    return render_template("post_form_edit.html", post=post)

@app.route("/posts/<int:post_id>", methods=["POST"])
def update(post_id):
    title = request.form["title"]
    content = request.form["content"]
    update_post(post_id, title, content)
    # return render_template("post_list_fragment.html", posts=get_all_posts())
    return render_template("post_list_wrapper.html", posts=get_all_posts())

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete(post_id):
    delete_post(post_id)
    # return render_template("post_list_fragment.html", posts=get_all_posts())
    return render_template("post_list_wrapper.html", posts=get_all_posts())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)


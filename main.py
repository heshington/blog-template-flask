from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    blogs = requests.get(blog_url)
    blog_data = blogs.json()
    return render_template("index.html", blogs=blog_data)

@app.route('/blog/<int:id>')
def get_blog(id):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    blogs = requests.get(blog_url)
    blog_data = blogs.json()
    for blog in blog_data:
        if blog['id'] == id:
            title = blog['title']
            body = blog['body']
            subtitle = blog['subtitle']

    return render_template("post.html", id=id, title=title, body=body, subtitle=subtitle)
if __name__ == "__main__":
    app.run(debug=True)

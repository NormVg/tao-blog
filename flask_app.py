import os
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import markdown2

app = Flask(__name__)
db = TinyDB('db/blog_db.json')

# Configure the folder where images will be saved
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/write', methods=['GET', 'POST'])
def write_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        content_html = markdown2.markdown(content)
        db.insert({'title': title, 'content': content_html})
        return redirect(url_for('blog_list'))
    return render_template('write.html')

@app.route('/')
def blog_list():
    blogs = db.all()
    return render_template('blog_list.html', blogs=blogs)

# @app.route('/write', methods=['GET', 'POST'])
# def write_blog():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         content_html = markdown2.markdown(content)  # Convert the Markdown to HTML
#         db.insert({'title': title, 'content': content_html})
#         return redirect(url_for('blog_list'))
#     return render_template('write.html')

@app.route('/blog/<int:blog_id>')
def read_blog(blog_id):
    blog = db.get(doc_id=blog_id)
    return render_template('blog.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)

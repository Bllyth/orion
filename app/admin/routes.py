from flask import render_template, redirect, url_for, flash, request
from app import db
from app.admin import admin
from flask_login import login_required
from .forms import PostForm
from app.models import Post


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@admin.route('/admin/add-post', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
    return render_template('admin/add_post.html', form=form)


@admin.route('/admin/posts')
@login_required
def posts():
    return render_template('admin/posts.html')


@admin.route('/admin/post/<int:post_id>')
@login_required
def post(post_id):
    return render_template('admin/post.html')
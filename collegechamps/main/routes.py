# main/routes.py
from flask import render_template, request, Blueprint, redirect
from flask.helpers import make_response
from flask_login import login_required
from werkzeug.wrappers import response
from collegechamps.models import User,Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    feats = Post.query.filter_by(slug='blog',others1='article')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts = Post.query.filter_by(slug = 'index')
    return render_template('index.html',posts = posts ,side_posts = side_posts,feats=feats)

# @main.route('/sidebar_elem/<int:side_id>')
# def sidebar_elem(side_id):
#     side_id = side.
@main.route('/robots.txt',methods=['GET'])
def robots():
    response = make_response(open('robots.txt').read())
    return response



@main.route("/ioe")
def ioe():
    return render_template('ioe.html')

# @main.route('/admin')
# def admin():
#     pass


@main.route("/blog_notes")
def blog_notes():
    return render_template('blog_notes.html')

@main.route('/CollegeChamps/privacy-policy/<parameter>')
def privacy_policy(parameter):
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('privacy_policy.html',side_posts= side_posts, parameters =parameter)
 



from flask import Blueprint, render_template
from collegechamps.models import Post

errors = Blueprint('errors', __name__)



@errors.app_errorhandler(404)
def error_404(error):
    side_posts = Post.query.filter_by(others2 = 'sidebar')
   # message = 'The page you are trying to access does not exist. You better return home'
    return render_template('errors/404.html',heading= 'Opps, Looks Like You are Lost',sub_header='404 Error',side_posts = side_posts),404


@errors.app_errorhandler(403)
def error_403(error):
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('errors/403.html',heading= 'Restricted Page!',sub_header='403 Error',side_posts = side_posts),403



@errors.app_errorhandler(500)
def error_50(error):
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('errors/500.html',heading= 'Sorry, The server is under maintenance',sub_header='Internal Server Error',side_posts = side_posts),500


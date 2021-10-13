import json
import os
import secrets
from datetime import datetime, timezone
from io import TextIOWrapper
from re import sub

from collegechamps import app, db, env_v
from collegechamps.blog.forms import PostForm
from collegechamps.models import Post, Set
from collegechamps.users.forms import RegistrationForm
from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf.recaptcha.widgets import RecaptchaWidget
from PIL import Image
from slugify import slugify
from werkzeug.utils import secure_filename, send_from_directory

creds = env_v()
# db_username = os.environ.get('USERNAME')
# db_pw = os.environ.get('DB_PASSWORD')

# with open('mcq.json', 'r') as c:
#     params = json.load(c)["params"]

blogs = Blueprint('blogs', __name__)



@blogs.route('/blog_page')
def blog_page():
    side_posts = Post.query.filter_by(others2 = 'sidebar')[0:5]
    feats = Post.query.filter_by(featured='featured')
    page = request.args.get('page',1,type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).filter_by(
        slug='blog', others1='article').paginate(page=page,per_page=4)

    notes = Post.query.filter_by(slug='blog', others1='note')

    return render_template('blog_page.html', background="sc-6", heading='CollegeChamps', sub_header='Blog Page',feats = feats, posts=posts, notes=notes, side_posts = side_posts)
@blogs.route('/searched')
def search():
    side_posts = Post.query.filter_by(others2 = 'sidebar')[0:5]
    feats = Post.query.filter_by(featured='featured')
    q = request.args.get('q')
    if q and len(q)>=2:
        flash('Found Something','info')
        posts = Post.query.filter(Post.title.contains(q) | 
        Post.keywords.contains(q))
    else:
        flash('Found Nothing...','info')
        return redirect(url_for('blogs.blog_page'))
    return render_template('search_items.html',posts = posts,heading=f"Search results for '{q}'",feats = feats,notes=notes, side_posts = side_posts)

@blogs.route('/post/<int:post_id>/')
def post(post_id):
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    post = Post.query.get_or_404(post_id)

    return render_template('post.html', title=post.title, post=post, feats=feats, side_posts= side_posts)


@blogs.route('/post_page')
def post_page():
    return render_template('postpage.html')


@blogs.route('/ioe_entrance/ioe-notes')
def notes():
    notes = Post.query.filter_by(others1='note')
    return render_template('post.html', notes=notes)



@blogs.route('/ioe_entrance/ioe-notes/<int:note_id>')
def note_ids(note_id):
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts = Post.query.get_or_404(note_id)
    return render_template('post.html', posts  = posts, feats=feats, side_posts=side_posts)


@blogs.route('/featured')
def featured_posts():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    feats = Post.query.filter_by(featured='featured')
    return render_template('featured.html', feats=feats,side_posts=side_posts)


@blogs.route('/featured/<int:feat_id>/<string:slug>')
def featured_ids(feat_id,slug):
    feat = Post.query.get_or_404(feat_id)
    slug =  Post.query.get_or_404(slug)
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('featured.html',slug = slug, feat=feat, feats=feats,side_posts=side_posts)




@blogs.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    form = RegistrationForm()
    if ('user' in session and session['user'] == creds.db_username):
        posts = Post.query.filter_by(slug='index')
        see_posts = Post.query.filter_by(slug  = 'set_page', subject_title = 'see')
        articles = Post.query.filter_by(slug  = 'blog', others1 = 'article')
        notes = Post.query.filter_by(slug  = 'blog', others1 = 'note')
        class_11_notes = Post.query.filter_by(slug= 'note_topic', grade = '11')
        class_12_notes = Post.query.filter_by(slug= 'note_topic', grade = '12')
        return render_template('dashboard.html', posts=posts,see_posts = see_posts,articles = articles,notes=notes, class_11_notes = class_11_notes,class_12_notes=class_12_notes)

      

    if request.method == "POST":
        username = form.username.data
        userpass = form.password.data
        if username == creds.db_username and userpass == creds.db_pw:
            session['user'] = username
            posts = Post.query.all()
            see_posts = Post.query.filter_by(slug  = 'index')
            flash('Welcome to the dashboard', 'succes')
            return render_template('dashboard.html', posts=posts,see_posts = see_posts)
        else:
            flash('Retype The password or the username ', 'error')
    return render_template('dashboard_sign_in.html', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    basewidth = 250
    # output_size = (200, 200)
    i = Image.open(form_picture)
    wpercent = (basewidth/float(i.size[0]))
    hsize = int((float(i.size[1])*float(wpercent)))
    i = i.resize((basewidth,hsize), Image.ANTIALIAS)
    # i.thumbnail(output_size)
    i.save(picture_path)
   

    return picture_fn

# with parameters post
# with parameters post
# with parameters post
# with parameters post
@blogs.route("/postNew/<string:parameter>", methods=['GET', 'POST'])
def postNew(parameter):

    if ('user' in session and session['user'] == creds.db_username):
        posts = Post.query.all()
        form = PostForm()
        if parameter == 'index':
            form.slug.data = 'index'
            # flash_kw = 'index'
            form.content.data = "_"
        if parameter == 'set_page':
            form.slug.data = 'set_page'
        if parameter == 'note':
            form.slug.data = 'note_topic'
            # flash_kw = 'Sets'

        if form.validate_on_submit():
            title = form.title.data
            slug = form.slug.data
            content = form.content.data
            subtitle = form.subtitle.data
            keywords = form.keywords.data
            price = form.price.data
            subject_title = form.subject_title.data
            pic = request.files['pic']
            others1 = form.others1.data
            note_grade = form.note_grade.data
            others2 = form.others2.data
            topic = form.topic.data
            if pic:
                pic = save_picture(request.files['pic'])
            else:
                pic = 'hello.png'
            to_redirect = form.to_redirect.data
            post = Post(title=title, slug=slug, subtitle=subtitle, img=pic,
                        to_redirect=to_redirect, content=content, price=price, subject_title=subject_title, others1 = others1, others2 = others2, grade = note_grade, topic = topic,keywords=keywords)
            db.session.add(post)
            db.session.commit()
            # {flash_kw}
            flash(f'Your post has been created for  page!', 'succes')
            # if parameter =='continue_editing':
            #     return redirect('blogs.update_post',post_id =post.id)
               
            return redirect('blogs.dashboard')
        return render_template('create_post.html', title='You are posting on the index page',
                               form=form, posts =posts ,parameter=parameter)

    return "please login to the dashboard first. Dont try to enter without logging in!"

@blogs.route("/postNew", methods=['GET', 'POST'])
def post_new_no_param():

    if ('user' in session and session['user'] == creds.db_username):
        posts = Post.query.all()
        form = PostForm()

        if form.validate_on_submit():
            title = form.title.data
            slug = form.slug.data
            content = form.content.data
            subtitle = form.subtitle.data
            price = form.price.data
            keywords = form.keywords.data
            subject_title = form.subject_title.data
            pic = request.files['pic']
            others1 = form.others1.data
            others2 = form.others2.data
            note_grade = form.note_grade.data
            topic = form.topic.data
            if pic:
                pic = save_picture(request.files['pic'])
            else:
                pic = 'hello.png'
            to_redirect = form.to_redirect.data
            post = Post(title=title, slug=slug, subtitle=subtitle, img=pic,
                        to_redirect=to_redirect, content=content, price=price, subject_title=subject_title, others1 = others1, others2 = others2,grade = note_grade,topic=topic,keywords=keywords)
            db.session.add(post)
            db.session.commit()
            # {flash_kw}
            flash(f'Your post has been created for  page!', 'succes')
               
            return redirect('/home')
        return render_template('create_post.html', title='',
                               form=form, posts =posts)

    return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    posts = Post.query.all()
    if ('user' in session and session['user'] == creds.db_username):
        form = PostForm()
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            post.slug = form.slug.data
            post.subtitle = form.subtitle.data
            post.to_redirect = form.to_redirect.data
            post.price = form.price.data
            post.keywords= form.keywords.data
            post.others1 = form.others1.data
            post.others2 = form.others2.data
            post.grade = form.note_grade.data
            post.topic = form.topic.data

            pic = request.files['pic']
            if pic:

                post.img = save_picture(request.files['pic'])
            else:
                pass

            db.session.commit()
            flash('Your post has been updated!', 'succes')
            return redirect(url_for('blogs.dashboard'))
        elif request.method == 'GET':
            form.title.data = post.title
            form.content.data = post.content
            form.slug.data = post.slug
            form.subject_title.data = post.subject_title
            form.subtitle.data = post.subtitle
            form.keywords.data = post.keywords
            form.to_redirect.data = post.to_redirect
            form.price.data = post.price
            form.others1.data = post.others1
            form.others2.data = post.others2
            form.note_grade.data = post.grade
            form.topic.data  = post.topic

        return render_template('create_post.html', title='Update Post',posts=posts,
                               form=form, legend='Update Post')
    return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if ('user' in session and session['user'] == creds.db_username):
     
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'info')
        return redirect(url_for('blogs.dashboard'))

    return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route('/set_page')
@login_required
def set_page():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    sets = Post.query.filter_by(slug='set_page',subject_title = 'see')
    return render_template('sets_page.html', sets=sets, header = '+2 Entrance Preparation',title = '+2 Entrance Preparation',side_posts = side_posts,time_limit = '25 minutes')


@blogs.route('/individual_set/<int:set_id>/')
def individual_set(set_id):
   
    individual_page = Post.query.get_or_404(set_id)
    sets = Post.query.filter_by(time_limit1 = '180')
    
    return render_template('forms_page.html', individual_page=individual_page,sets = sets)















from datetime import time
from operator import pos
from re import sub
from flask import render_template, request, Blueprint
from collegechamps.models import User, Post
from flask_login import login_required
subjects = Blueprint('subjects', __name__)

maths_sub ={
    "header":'Mathematics',
    "sub_header": 'The Heart of All Sciences',
    "topics" : [{'Sets And Functions':'sets_and_functions'},{'Algebra':'algebra'},{'Trigonometry':'trigonometry'},{'Coordinate Geometry':'coordinate_geometry'},{'Claculus':'calculus'},{'Vectors':'vectors'}
    ]
}
physics_sub ={
    "header":'Physcis',
    "sub_header": 'Defines the universe',
        "topics" : [{'Mechanics':'mechanics'}, {'Optics':'optics'},{'Heat':'heat'},{'Atomic Plysics & Electrostats':'electrostatics',},{'Sound':'sound'}]
}
chemistry_sub ={
    "header":'Chemistry',
    "sub_header": 'Defines the universe',
    # {title : route}
    "topics" : [{'Language of Chemistry':'physical_chemistry'}, {'Electronic theory to valency':'electronic_theory_to_valency'},
    # have to replace the _ with space
    {'Oxidation and Reduction':'oxidation_and_reduction'},{'Periodic Table':'periodic_table',},{'Mole Concept':'mole_concept'},{'Non-Metals':'non_metals'},{'Metals':'metals'},{'Organic Chemistry':'organic_chemistry'}]
}
biology_sub ={
    "header":'Biology',
    "sub_header": 'Defines the universe',
    "topics" : ['Mechanics', 'Optics','Thermodynamics','Gas Laws','Electrostats']
}


@subjects.route('/maths')
def maths():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = maths_sub['header'],sub_header = maths_sub['sub_header'], topics = maths_sub['topics'], background = 'sc-4', button = 'sc4-btn', cardBackground = 'backMathCard',side_posts = side_posts)

@subjects.route('/physics')
def physics():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = physics_sub['header'],sub_header = physics_sub['sub_header'],
     topics = physics_sub['topics'], background = 'sc-1',
     button = 'sc1-btn' , cardBackground = 'backPhyCard', side_posts = side_posts)


@subjects.route('/biology')
def biology():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html', heading  = biology_sub['header'],
    sub_header = biology_sub['sub_header'], topics = biology_sub['topics'], 
    background = 'sc-3', button = 'sc3-btn', cardBackground = 'backBioCard',id = len(biology_sub), side_posts= side_posts)


@subjects.route('/chemistry')
def chemistry():
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('subject.html',side_posts=side_posts, heading  = chemistry_sub['header'],
    sub_header = chemistry_sub['sub_header'], topics = chemistry_sub['topics'],
     background = 'sc-2', button = 'sc2-btn' , cardBackground = 'backChemCard')


@subjects.route('/set_prep_page')
def set_prep_page():
    sets = Post.query.filter_by(slug='set_page')

    return render_template('subject_sets.html', sets=sets)


@subjects.route('/individual_set/<int:set_id>')
def individual_set(set_id):

    individual_page = Post.query.get_or_404(set_id)
    return render_template('forms_page.html', individual_page=individual_page,times_limit = 21)

# Physics
# Physics
# Physics

def featured_container(slug):
    return Post.query.filter_by(others2 = slug)

#time limit for sets
time_limit = "21 minutes"
short_questions  = '15 x 1 = 15'
long_questions = '5 x 2 = 10'


@subjects.route('/ioe-mechanics-entrance-questions')
@login_required
def mechanics():
    side_posts  = featured_container('sidebar')
    #for these routes  i will need the to_redirect slug and it will redirect to set page where students will be able to choose different test sets.
    #there will be no individual id link in this route.
    sets = Post.query.filter_by(slug='set_page', subject_title = 'mechanics')
    return render_template('subject_sets.html', sets=sets,
    title = 'IOE Mechanics Pracice Questions' ,time_limit = time_limit,short_questions = short_questions, long_questions=long_questions,
    header='Mechanics Sets',subject_title = 'mechanics',side_posts = side_posts)


@subjects.route('/ioe-physics/ioe-optics-questions')
@login_required

def optics():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'optics')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Optics Pracice Questions' ,time_limit = time_limit,header='Optics Sets',side_posts = side_posts)

@subjects.route('/ioe-physics/ioe-heat-and-thermodynamics')
@login_required

def heat():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'heat')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Heat Pracice Questions' ,time_limit = time_limit,header='Heat Sets',side_posts = side_posts)

@subjects.route('/ioe-physics/ioe-sound')
@login_required

def sound():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'sound')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Sound Pracice Questions' ,time_limit = time_limit,header='Sound Sets',side_posts = side_posts)


@subjects.route('/ioe-physics/ioe-atomic-physics-electrostatics')
@login_required

def electrostatics():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'elect_atom')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Electrostacics And Atom Pracice Questions' ,time_limit = time_limit,header='Electricity and Atom Sets',side_posts = side_posts)


# Chemistry
# Chemistry
# Chemistry
@subjects.route('/ioe-chemistry/ioe-chemistry-language-of-chemistry-&-physical-chemistry')
@login_required

def physical_chemistry():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'phy-chem')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Language of Chemistry & Physical Chemistry' ,time_limit = time_limit,header='Language of Chemistry & Physical Chemistry',side_posts = side_posts)


@subjects.route('/ioe-chemistry/ioe-chemistry-electronics-theory-to-valency')
@login_required

def electronic_theory_to_valency():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'valency')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Electronics Theory to Valency' ,time_limit = time_limit,header='Electronics Theory To Valency',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-oxidation-and-reduction')
@login_required

def oxidation_and_reduction():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'oxidation')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Oxidation And Reduction' ,time_limit = time_limit,header='Oxidation and Reduction',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-periodic-table')
@login_required

def periodic_table():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'periodic_table')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Periodic Table' ,time_limit = time_limit,header='Periodic Table',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-molecular-weight-and-mole')
@login_required

def mole_concept():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'mole')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Molecular Theory And Mole' ,time_limit = time_limit,header='Mole Concept and Molecular Theory',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-metals')
@login_required

def metals():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'metals')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = ' IOE Metals' ,time_limit = time_limit,header='Metals',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-non-metals')
@login_required

def non_metals():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'n-metals')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Non-Metals' ,time_limit = time_limit,header='Non-Metals',side_posts = side_posts)

@subjects.route('/ioe-chemistry/ioe-chemistry-organic-chemistry')
@login_required

def organic_chemistry():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'organic')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Organic Chemitry' ,time_limit = time_limit,header='Organic Chemistry',side_posts = side_posts)

#mathematics
#mathematics
#mathematics
@subjects.route('/ioe-mathematics/ioe-maths-set-and-function')
@login_required

def sets_and_functions():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'set_function')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Sets And Function' ,time_limit = time_limit,header='Sets & Functions',side_posts = side_posts)

@subjects.route('/ioe-mathematics/ioe-algebra')
@login_required

def algebra():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'algebra')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Sets And Function' ,time_limit = time_limit,header='Algebra',side_posts = side_posts)

@subjects.route('/ioe-mathematics/ioe-trigonometry')
@login_required

def trigonometry():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'trigonometry')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Trignonmetry' ,time_limit = time_limit,header='Trigonometry',side_posts = side_posts)

@subjects.route('/ioe-mathematics/ioe-co-ordinate_geometry')
@login_required

def coordinate_geometry():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'coord_geometry')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Co-ordinate Geometry' ,time_limit = time_limit,header='Co-ordinate Geometry',side_posts = side_posts)

@subjects.route('/ioe-mathematics/ioe-calculus-derivatives-and-antiderivatives')
@login_required

def calculus():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'calculus')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Calculus' ,time_limit = time_limit,header='Calculus',side_posts = side_posts)

# @subjects.route('/ioe-mathematics/ioe-calculus-derivatives-and-antiderivatives')
# def calculus():
#     sets = Post.query.filter_by(slug='set_page', subject_title = 'calculus')
#     return render_template('subject_sets.html', sets=sets,title = 'IOE Calculus' ,header='Calculus')

@subjects.route('/ioe-mathematics/ioe-vectors')
@login_required

def vectors():
    side_posts  = featured_container('sidebar')
    sets = Post.query.filter_by(slug='set_page', subject_title = 'vectors')
    return render_template('subject_sets.html',short_questions = short_questions, long_questions=long_questions, sets=sets,title = 'IOE Vectors' ,time_limit = time_limit,header='Vectors',side_posts = side_posts)



# class 11 science
# class 11 science
# class 11 science
# class 11 science
# class 11 science

@subjects.route('/class-11-notes-science')
def notes_page_science_11():
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    maths_sub ={
    "header":'Class 11 Science',
    "sub_header": '',
    "topics" : [{'Physics':'physics_notes_11'},{'Chemistry':'chemistry_notes_11'},{'Mathematics':'mathematics_notes_11'},{'Computer':'computer_notes_11'},{'English':'english_notes_11'},{'Nepali':'nepali_notes_11'}
    ]
}   
    return render_template('subject.html', heading  = maths_sub['header'],sub_header = maths_sub['sub_header'], topics = maths_sub['topics'], background = 'sc-4', button = 'sc4-btn', cardBackground = 'backMathCard',side_posts = side_posts,feats  = feats)

def note_slug(slug):
    note  = Post.query.filter_by(slug ='note', others2 = slug)
    return note

@subjects.route('/class-11/class-11-physics-complete-notes')
def physics_notes_11():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'physics_note_topic_11')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'Pysics Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats =feats)

@subjects.route('/class-11/class-11-chemistry-complete-notes')
def chemistry_notes_11():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'chemistry_note_topic_11')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('chemistry_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'Chemistry Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-11/class-11-mathematics-complete-notes')
def mathematics_notes_11():
    feats = Post.query.filter_by(featured='featured')
    posts_notes = note_slug('maths_note')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'mathematics_note_topic1_11')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'Maths Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats = feats)

@subjects.route('/class-11/class-11-english-complete-notes')
def english_notes_11():
    posts_notes = note_slug('english_note')
    feats = Post.query.filter_by(featured='featured')   
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'english_note_topic_11')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'English Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-11/class-11-comptuer-science-complete-notes')
def computer_notes_11():
    posts_notes = note_slug('computer_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'computer_note_topic_11')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'Computer Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-11/class-11-nepali-complete-notes')
def nepali_notes_11():
    posts_notes = note_slug('nepali_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'nepali_note_topic_11')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 11' ,title = 'Nepali Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)


# pending process
# def render_template_function(page_to_render,subtitle,post_title,slug_of_note,identifier_of_post):
#     post_notes = note_slug(slug_of_note)
#     return render_template(page_to_render, sub_title = subtitle ,title = post_title,posts_notes= post_notes, identifier = identifier_of_post)

# @subjects.route('/class-11/class-11-nepali-complete-notes')
# def nepali_notes():

#     render_template_function('post.html','class 11','Neplai Notes','nepali_note','subject_notes')


# class 12 science
# class 12 science
# class 12 science
# class 12 science
# class 12 science


@subjects.route('/class-12-notes-science')
def notes_page_science_12():
    
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    maths_sub ={
    "header":'Class 12 Science',
    "sub_header": '',
    "topics" : [{'Physics':'physics_notes_12'},{'Chemistry':'chemistry_notes_12'},{'Mathematics':'mathematics_notes_12'},{'Computer':'computer_notes_12'},{'English':'english_notes_12'},{'Nepali':'nepali_notes_12'}
    ]
}   
    return render_template('subject.html', heading  = maths_sub['header'],sub_header = maths_sub['sub_header'], topics = maths_sub['topics'], background = 'sc-4', button = 'sc4-btn', cardBackground = 'backMathCard',side_posts = side_posts,feats=feats)

@subjects.route('/class-12/class-12-physics-complete-notes')
def physics_notes_12():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'physics_note_topic_12')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'Pysics Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats = feats)

@subjects.route('/class-12/class-12-chemistry-complete-notes')
def chemistry_notes_12():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'chemistry_note_topic_12')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('chemistry_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'Chemistry Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-12/class-12-mathematics-complete-notes')
def mathematics_notes_12():
    posts_notes = note_slug('maths_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'mathematics_note_topic_12')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'Maths Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-12/class-12-english-complete-notes')
def english_notes_12():
    posts_notes = note_slug('english_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'english_note_topic_12')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'English Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-12/class-12-comptuer-science-complete-notes')
def computer_notes_12():
    posts_notes = note_slug('computer_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'computer_note_topic_12')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'Computer Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)

@subjects.route('/class-12/class-12-nepali-complete-notes')
def nepali_notes_12():
    posts_notes = note_slug('nepali_note')
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    topic_of_note = Post.query.filter_by(slug = 'note_topic', topic  = 'nepali_note_topic_12')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Class 12' ,title = 'Nepali Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats=feats)














#CLASS 12 FINISHED

# #entrance notes
@subjects.route('/ioe-iom-entrance-notes-science')
def notes_page_entrance():
    feats = Post.query.filter_by(featured='featured')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    ioe_notes ={
    "header":'IOE Entrance Notes',
    "sub_header": 'Notes with most famous questions',
    "topics" : [{'Physics':'physics_entrance_notes'}
    ,{'Chemistry':'chemistry_entrance_notes'},{'Mathematics':'mathematics_entrance_notes'},{'English':'english_entrance_notes'}
    ]
}
    return render_template('subject.html', heading  = ioe_notes['header'],sub_header = ioe_notes['sub_header'], topics = ioe_notes['topics'], background = 'sc-4', button = 'sc4-btn', cardBackground = 'backMathCard',side_posts = side_posts,feats=feats)




# def note_slug(slug):
#     note  = Post.query.filter_by(slug ='entrance_note', others2 = slug)
#     return note

@subjects.route('/ioe-physics-entrance-complete-notes')
def physics_entrance_notes():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'physics_note_topic_entrance')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Entrance Notes' ,title = 'Physics Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats= feats)

@subjects.route('/ioe-chemistry-entrance-complete-notes')
def chemistry_entrance_notes():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'chemistry_note_topic_entrance')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Entrance Notes' ,title = 'Pysics Notes',identifier = 'subject_notes',note_contents = topic_of_note,feats=feats,posts_notes=posts_notes)

@subjects.route('/ioe-mathematics-entrance-complete-notes')
def mathematics_entrance_notes():
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'mathematics_note_topic_entrance')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Entrance Notes' ,title = 'Pysics Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note)

@subjects.route('/ioe-english-entrance-complete-notes')
def english_entrance_notes():
    feats = Post.query.filter_by(featured='featured')
    topic_of_note = Post.query.filter_by(slug = 'note_topic',topic  = 'english_note_topic_entrance')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts_notes = note_slug('physics_note')
    return render_template('post.html',side_posts = side_posts,sub_title = 'Entrance Notes' ,title = 'Pysics Notes',posts_notes= posts_notes,identifier = 'subject_notes',note_contents = topic_of_note,feats= feats)


#full mock tests
#full mock tests
#full mock tests
#full mock tests



@subjects.route('/ioe-entrance-test-full-mock-test')
def full_mock_test():
    feats = Post.query.filter_by(featured='featured')
    sets = Post.query.filter_by(slug  = 'set_page',subject_title = 'mock_test')
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template("subject_sets.html",long_questions = '40 x 2 = 80',short_questions = '60 x 1 = 60'
    ,header = 'Full Mock Test',sub_header  = "140 marks test"
    , sets = sets,side_posts=  side_posts, time_limit='2 hours',feats=feats)
 
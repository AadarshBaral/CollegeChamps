
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators
from wtforms.fields.core import RadioField, SelectField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    slug = SelectField('Slug',choices=[('index','index'),('blog','blog'),('note_topic','note_topic'),('see','see'),('set_page','set_page')])

    subtitle = StringField('Subtitle',validators=[DataRequired()])

    content = TextAreaField('Content', validators=  [DataRequired()])

    price = RadioField('Price',choices=[('free','free'),('paid','paid')],validators=[validators.Optional()])
    keywords = StringField('Keywords',validators=[DataRequired()])
    
    subject_title = SelectField('Choose a subject_title',choices=[('mechanics','Mechanics'),('optics','Optics'),('heat','Heat'),('elect_atom','Electrons and Atomic Theory'),('phy_chem','Physical Chemistry'),('valency','Valency'),('oxidation','Oxidation & Reduction'),('periodic_table','Periodic Table'),('mole','Mole Concept'),('n_metals','Non-Metals'),('metals','Metals'),('organic','Organic Chemistry'),('set_function',
    'Sets & Functions'),('algebra','Algebra'),('coord_geometry','Coordinate_Geometry'),('calculus','Calculus'),('vectors','Vectors For Maths'),('','none')])


    topic = StringField('Topic For Notes Identification',validators=[validators.Optional()])
    note_grade = SelectField('Choose which grade the note belongs to',choices=[('11','11'),('12','12')])
    others1  = RadioField('Article or Note?',choices=[('article','article'),('note','note')],validators=[validators.Optional()])
    

    others2 = StringField("Others",validators=[validators.Optional()])
 
    to_redirect = StringField('Redirect Page',validators=[validators.Optional()])


    submit = SubmitField('Post')
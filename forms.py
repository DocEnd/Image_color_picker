
from flask_wtf.file import FileField, FileRequired, FileAllowed

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class Upload_file(FlaskForm):
    file = FileField('Please choose and upload your Photo to analise',
                     validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    nr_of_top = StringField('Input the nr. of TOP colors needed:', validators=[DataRequired()])
    window_of_colors = StringField('Input the window of colors (the delta):', validators=[DataRequired()])
    submit = SubmitField("Submit File", validators=[DataRequired()])
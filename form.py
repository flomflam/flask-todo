from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    task = StringField('Task name')
    submit = SubmitField('Send')
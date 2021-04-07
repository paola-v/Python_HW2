from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField,SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Name of Dog: ',validators=[DataRequired()])
    breed = StringField('What breed is the dog?')
    age = IntegerField('How old is the dog?')
    sex = RadioField('Is the dog a boy or a girl?',choices=[('girl','Girl'),('boy','Boy')])
    submit = SubmitField('Add Dog')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Dog to Remove:')
    submit = SubmitField('Remove Dog')
class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner:')
    dog_id = IntegerField('Dog ID:')
    submit = SubmitField('Add Owner')

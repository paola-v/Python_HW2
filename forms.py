from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Name of Dog: ',validators=[DataRequired()])
    breed = StringField('What breed is the dog?')
    color = StringField('What color is the dog?')
    age = IntegerField('How old is the dog?')
    mood = RadioField("Pick the dog's typical mood:",choices=[('playful','Playful'),('excited','Excited'),
                    ('relaxed','Relaxed'),('fearful','Fearful')] )
    sex = RadioField('Is the dog a boy or a girl?',choices=[('girl','Girl'),('boy','Boy')])
    submit = SubmitField('Add Dog')

class DelForm(FlaskForm):
    id = IntegerField('Id Number of Dog to Remove:')
    submit = SubmitField('Remove Dog')
class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner:')
    phone = StringField('Phone Number:')
    email = StringField('Email:')
    dog_id = IntegerField('Dog ID:')
    submit = SubmitField('Add Owner')

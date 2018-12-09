from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange
from wtforms import Form

    
class CreateCargoForm(FlaskForm):
    cargo_number = IntegerField('Cargo number', validators=[DataRequired(message='Please input 11 digit number.'), NumberRange(min=10000000000, max=99999999999, message='Cargo number must be 11 digit.')])
    submit = SubmitField('Create')
    

from flask_wtf import FlaskForm

from wtforms import StringField

from wtforms.validators import (

    DataRequired,

    Length

)

class RequestForm(FlaskForm):

    title = StringField(

        validators=[

            DataRequired(),

            Length(

                min=5,

                max=200

            )

        ]

    )
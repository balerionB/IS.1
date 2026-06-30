import requests
from flask import jsonify
from flask_login import login_required

from back_end.app.forms.request_forms import RequestForm
from back_end.app.services.activity_service import ActivityService


@requests.route("/api/<int:id>/timeline")
@login_required
def timeline(id):
    """
    Returns the activity history for a specific request.
    """

    return jsonify(
        ActivityService.request_history(id)
    )
form = RequestForm()

if form.validate_on_submit():

    ...

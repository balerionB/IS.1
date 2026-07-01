from back_end.app.utils.permissions import roles_required
@admin.route("/users")
@login_required
@roles_required(
    "Administrator",
    "System Administrator"
)
def users():

    ...
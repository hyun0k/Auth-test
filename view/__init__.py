from view.user_view import UserView

def create_endpoints(app):
    app.add_url_rule("/users", view_func=UserView.as_view("users"), methods=["POST"])

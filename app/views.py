from app import server


@server.route("/")
def hello():
    return "<h1>Hello there!</h1>"

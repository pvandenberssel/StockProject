from init import db,app
from EndPoint.UserEndPoint import user_api
from flask import blueprints

app.register_blueprint(user_api)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
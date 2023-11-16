# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

# # Create the database tables
# db.create_all()

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         user = User.query.filter_by(username=username).first()

#         if user and check_password_hash(user.password, password):
#             return "Login successful!"
#         else:
#             return "Invalid username or password. Please try again."

#     return render_template('login.html')

# if __name__ == '__main__':
#     app.run(debug=True)

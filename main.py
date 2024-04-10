from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"username": "user1", "email": "user1@gmail.com"},
    {"username": "user2", "email": "user2@gmail.com"},
    {"username": "user3", "email": "user3@gmail.com"}
]

companies = [
    {"company_name": "Google", "creation_date": "2000.20.01"},
    {"company_name": "Microsoft", "creation_date": "2002.22.01"},
    {"company_name": "Blizzard", "creation_date": "2001.21.01"}
]
contacts = [
    {"name": "Test1", "phone": "+1231123"},
    {"name": "Test2", "phone": "+45467345"},
    {"name": "Test3", "phone": "+78978"},
]


@app.route('/home')
def home():
    return render_template('home.html', users=users)


@app.route("/about")
def about():
    return render_template("about.html", companies=companies)


@app.route("/contact")
def contact():
    return render_template("contact.html", contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)

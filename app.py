import os
from flask import Flask
from flask import render_template 
from flask import send_from_directory
from flask import session
from flask import request
from flask import redirect
from flask import url_for
import posts
import contacts

# initialization
USERNAME = 'admin@pepe.com'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'development key',
)

# controllers
#@app.route("/")
#def hello():
#    return "Hello from Python!"


# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('show_entries'))

    return render_template('login.html', error=error)

@app.route("/show_entries")
def show_entries():
    return render_template('show_entries.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('logout.html')

db_posts = posts.Posts()
db_contacts = contacts.Contacts()
@app.route("/clean_blog")
def clean_blog():
    all_posts = db_posts.get_all()
    return render_template('start_boot_strap/clean_blog/index.html', posts=all_posts)

@app.route("/clean_blog_about")
def clean_blog_about():
    session['logged_in'] = False
    return render_template('start_boot_strap/clean_blog/about.html')

@app.route('/clean_blog_post/<int:dbindex>')
def clean_blog_post(dbindex):
    session['logged_in'] = False
    print "dbindex ",dbindex 
    return render_template('start_boot_strap/clean_blog/post.html', register=db_posts.get_one(dbindex))

@app.route("/clean_blog_contact", methods=['GET', 'POST'])
def clean_blog_contact():
    error = None
    if request.method == 'POST':
       name = request.form['c_name']
       phone = request.form['telefono']
       email = request.form['email']
       mensaje = request.form['message']
       db_contacts.add_contact(name, phone, email, mensaje)
       return redirect(url_for('clean_blog_thank', contact_name=name))
    return render_template('start_boot_strap/clean_blog/contact.html')

@app.route('/clean_blog_thank/<contact_name>')
def clean_blog_thank(contact_name):
    return render_template('start_boot_strap/clean_blog/thank.html', contact=contact_name)




# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

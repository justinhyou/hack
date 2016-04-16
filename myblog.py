#########################################################
# All the imports
#
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from contextlib import closing
from message import *  # message.py acts as the database server


#########################################################
# Configuration
#
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


#########################################################
# Create our little application -:)
#
app = Flask(__name__)
app.config.from_object(__name__)


#########################################################
# Database
# 
# messages = []  # messages acts as the database of blog post entries
#
# Initialize the db with a couple of message objects to begin with:
messages = [Message('one', 'uno'),
            Message('hi', 'there')
           ]

# Initialize the database
def init_db():
    global messages
    messages = []
    Message().reset()

#########################################################
# View functions

# When the site is connected, start with the posts in the db so far
@app.route('/')
def show_entries():
    global messages

    # for m in messages:           # Use this for debugging 
    #     flash(m.__str__())

    # Sort messages (the message list) in the order of id values
    messages.sort(key=lambda x: x.id, reverse=True)

    # Access the database (messages acts as a database in our case)
    # and gather the needed data and pass it to a template file
    # (show_entries.html in this case) which actually uses the data
    # to send back to the client.
    entriess = []  # List of dictionaries (each a title-text pair)
    for row in messages:
        entriess.append(dict(title=row.get_title(), text=row.get_text()))
    return render_template('show_entries.html', entries=entriess)


# Add a new blog entry
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    # for m in messages:
    #     flash(m.__str__())
    messages.append(Message(request.form['title'], request.form['text']))
    flash('New entry was successfully posted')
    # Finish up by redirecting it to show_entries
    print(url_for('show_entries'))
    return redirect(url_for('show_entries'))


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            # init_db()  # alee  see clear_db above
            # Finish up by redirecting it to show_entries
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


# Log out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    # Still show_entries even after logged out
    return redirect(url_for('show_entries'))


# Clear the database
@app.route('/clear', methods=['POST'])
def clear_db():
    error = None
    if request.method == 'POST':
        init_db()
    return render_template('show_entries.html', error=error)

#########################################################
# Some request hooks
#
# A request hook function to register a function to run before each request
# It is a placeholder for now.
@app.before_request
def before_request():
    # flash('In before_request.......')
    None


# A request hook function to register a function to run after each request
# It is a placeholder for now.
@app.teardown_request
def teardown_request(exception):
    # flash('In teardown_request.......')
    None



#########################################################
# Start the server

if __name__ == '__main__':
    app.run()


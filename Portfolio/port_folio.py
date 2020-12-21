import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from flaskr.auth import login_required
from Portfolio.db import get_db

bp = Blueprint('port_folio', __name__)
#bp.add_url_rule('/', endpoint='home')

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    error = None
    posts = db.execute(
        'SELECT * FROM details'
        ' ORDER BY time_now DESC'
    ).fetchall()
    if request.method == 'POST':
        username = request.form['contact_name']
        email = request.form['contact_email']
        posted =request.form['contact_message']
        
        error = None
        posts = db.execute(
        'SELECT * FROM details'
        ' ORDER BY time_now DESC'
    ).fetchall()
        if not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not posted:
            error = 'Text is required.'

        if error is None:
            
            
            db.execute(
                'INSERT INTO details (username,email,posted) VALUES (?, ?,?)',
                (username,email,posted)
            )
            db.commit()
            message=("Added to sqlite Database:- Will reply as early as possible")
            flash(message)
            return redirect(url_for('port_folio.index'))

        flash(error)

    
    return render_template('port_folio/home.html',posts=posts)


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, time_now, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

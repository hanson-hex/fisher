
from . import web
from flask_login import login_required, current_user
from flask import current_app, flash, redirect, url_for
from app.models.gift import Gift
from app.models.base import db


@web.route('/my/gifts')
@login_required
def my_gifts():
    return "my_Gift"


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_add_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('已经加入了赠送清单或已经存在与你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))



@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass




from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from .base import db, Base
from flask_login import UserMixin
from app import login_manager

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from .gift import Gift
from .wish import Wish

class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_add_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False

        yushubook = YuShuBook()
        yushubook.search_by_isbn(isbn)
        if yushubook.first:
            return False

        gifting = Gift.query.filter_by(isbn=isbn,uid=self.id,launched=False).first()
        wishing = Wish.query.filter_by(isbn=isbn, uid=self.id, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
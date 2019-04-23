from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web
from app.models.gift import Gift
from app.models.wish import Wish

from app.view_models.tradeInfo import TradeInfo
from flask_login import current_user
import json

from app.view_models.book import BookSingle, BookCollection


@web.route('/book/search')
def search():
    """
    q: 普通关键字 isbn
    page
    :return:
    """
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushubook = YuShuBook()
        if isbn_or_key == 'isbn':
            yushubook.search_by_isbn(q)
        else:
            yushubook.search_by_keyword(q, page)

        books.fill(yushubook, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')

    return render_template('search_result.html', books=books, form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    if current_user.is_authenticated:
        gifts = Gift.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first()
        wishs = Wish.query.filter_by(isbn=isbn, uid=current_user.id, launched=False).first()
        if gifts:
            has_in_gifts = True
        if wishs:
            has_in_wishes = True

    gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    wishs = Wish.query.filter_by(isbn=isbn, launched=False).all()


    viewModelGifts = TradeInfo(gifts)
    viewModelWish = TradeInfo(wishs)

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookSingle(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=viewModelWish, gifts=viewModelGifts, has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
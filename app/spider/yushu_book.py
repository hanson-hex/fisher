from flask import current_app

from app.libs.httper import HTTP


class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_signle(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        res = HTTP.get(url)
        self.__fill_signle(res)
        return res

    def search_by_keyword(self, key_world, page=1):
        url = self.keyword_url.format(key_world, current_app.config['PER_PAGE'], self.calculate_start(page))
        res = HTTP.get(url)
        self.__fill_collection(res)
        return res

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

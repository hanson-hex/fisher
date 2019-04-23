
class BookSingle:
    def __init__(self, data):
        self.title = data['title']
        self.publisher = data['publisher']
        self.pages = data['pages'] or ''
        self.summary = data['summary'] or ''
        self.image =  data['image']
        self.isbn = data['isbn']
        self.author = ','.join(data['author'])
        self.price = data['price']
        self.binding = data['binding']
        self.pubdate = data['pubdate']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return ' / '.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushubook, keyword):
        self.total = yushubook.total
        self.books = [BookSingle(book) for book in yushubook.books]
        self.keyword = keyword


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned


    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'price': data['price'],
            'author': ','.join(data['author']),
            'summary': data['summary'],
            'image': data['image']
        }
        return book

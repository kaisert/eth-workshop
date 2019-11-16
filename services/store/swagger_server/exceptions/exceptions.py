class ArticleOutOfStockException(Exception):
    pass


class ArticleNotFoundException(Exception):
    pass

class ArticleAlreadyExistsException(Exception):
    pass

class UnexpectedStatusCode(Exception):
    def __init__(self, code):
        self.code = 'error', code

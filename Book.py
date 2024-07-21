class Book:
    """
        id (integer, уникальный идентификатор, генерируется автоматически)
        title (string, название книги)
        author (string, автор книги)
        year (integer, год издания)
        status (integer, статус книги: “в наличии”, “выдана”)
    """

    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

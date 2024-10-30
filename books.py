class Book:
    def __init__(self, book_id, book_name, author_name, availability_status, borrowed_by=None):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        self.availability_status = availability_status
        self.borrowed_by = borrowed_by
        self.reservation_heap = []

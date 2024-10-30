from Redblacktree import RedBlackTree
from books import Book
from reservationheap import ReservationHeap

class GatorLibrary:
    def __init__(self):
        self.red_black_tree = RedBlackTree()

    def insert_book(self, book_id, book_name, author_name, availability_status, borrowed_by=None):
        new_book = Book(book_id, book_name, author_name, availability_status, borrowed_by)
        self.red_black_tree.insert(book_id, new_book)
# Other methods for borrowing, returning, printing, deleting, finding closest book, etc.
def main():
    library = GatorLibrary()
    
    # Read input file and perform operations    
if __name__ == "__main__":
    main()

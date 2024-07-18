from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "в наличии"
    BORROWED = "выдана"

class MenuChoice(Enum):
    ADD_BOOK = '1'
    REMOVE_BOOK = '2'
    SEARCH_BOOK = '3'
    LIST_BOOKS = '4'
    UPDATE_STATUS = '5'
    EXIT = '6'
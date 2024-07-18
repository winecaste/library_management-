from dataclasses import dataclass

from enums import BookStatus


@dataclass
class Book:
    """
    Класс, представляющий книгу.

    Attributes:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги (по умолчанию "в наличии").
    """
    id: int
    title: str
    author: str
    year: int
    status: str = BookStatus.AVAILABLE.value

    def __str__(self):
        """
        Возвращает строковое представление книги.

        Returns:
            str: Строка с информацией о книге.
        """
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

    @classmethod
    def from_dict(cls, data):
        """
        Создает объект Book из словаря.

        Args:
            data (dict): Словарь с данными книги.

        Returns:
            Book: Созданный объект книги.
        """
        return cls(**data)

    def to_dict(self):
        """
        Преобразует объект Book в словарь.

        Returns:
            dict: Словарь с данными книги.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

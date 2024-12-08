from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    copy_of_iterable = []
    for elem in obj:
        copy_of_iterable.append(elem)
        yield elem

    while True:
        yield from copy_of_iterable

class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = obj
        self.current_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current_iter:
            self.current_iter = iter(self.obj)
            return next(self.current_iter)
        else:
            try:
                return next(self.current_iter)
            except StopIteration:
                self.current_iter = iter(self.obj)
                return next(self.current_iter)

if __name__ == '__main__':
    for i in Cycle([1, 2, 3, 4]):
        print(i)

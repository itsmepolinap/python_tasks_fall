from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for iterable in iterables:
        yield from iterable

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.obj = iter(iterables)
        self.inner_obj = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.inner_obj:
            try:
                elem = next(self.obj)
            except StopIteration:
                raise
            else:
                if isinstance(elem, Iterable):
                    self.inner_obj = iter(elem)
                    try:
                        return next(self.inner_obj)
                    except StopIteration:
                        self.inner_obj = None
                        return self.__next__()
                else:
                    return elem
        else:
            try:
                return next(self.inner_obj)
            except StopIteration:
                self.inner_obj = None
                return self.__next__()


if __name__ == '__main__':
    it = Chain('1234', 'a', ['10', '15', '20'])
    for i in it:
        print(i)
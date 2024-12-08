from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    if n < 1:
        raise ValueError('n must be at least one')

    obj = iter(obj)
    result = []

    while obj:
        try:
            result.append(next(obj))
        except StopIteration:
            if result:
                yield tuple(result)
            raise
        if len(result) == n:
            yield tuple(result)
            result = []


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        if n < 1:
            raise ValueError('n must be at least one')
        self.obj = iter(obj)
        self.n = n
        self.result = []
        self.marker = True

    def __iter__(self):
        return self

    def __next__(self):
        while self.marker:
            if len(self.result) == self.n:
                result = self.result
                self.result = []
                return tuple(result)
            else:
                try:
                    self.result.append(next(self.obj))
                except StopIteration:
                    self.marker = False
                    return tuple(self.result)
        else:
            raise StopIteration








if __name__ == '__main__':
    gen = (i for i in range(10))
    for i in Batched(gen, 4):
        print(i)
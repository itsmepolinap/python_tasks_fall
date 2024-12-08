import os.path
from datetime import datetime, UTC
from abc import ABC, abstractmethod
from typing import Any


class BaseStorage(ABC):
    def __init__(self, path_to_file: str, buffer_limit: int):
        '''
        Производит инициализацию хранилища метрик и создает файл.
        Args:
            path_to_file - Путь к файлу, в котором будут храниться метрики.
            buffer_limit - Максимальное количество строк до эвакуации их в файл.
        '''
        self.path_to_file = path_to_file
        self._buffer_limit = buffer_limit
        self.buffer: list[Any] = []  # Буфер, куда будут записываться метрики перед отправкой
        self._buffer_length = 0
        self._create_file()

    @abstractmethod
    def _create_file(self):
        '''
        Ваша логика создания файла
        '''

    def is_buffer_overflow(self):
        '''
        Осуществляет проверку буфера на переполнение.
        Raises:
            OverflowError - В случае если буфер переполнен.
        '''

        if self._buffer_length == self._buffer_limit:
            self._buffer_length = 0
            raise OverflowError('Переполнение буфера.')

    def add_data_to_buffer(self, data: Any):
        '''
        Добавляет данные в буфер.
        Args:
            data - Данные, которые будут добавлены в буфер.
        '''

        self._buffer_length += 1
        self.buffer.append(data)

    @abstractmethod
    def _collect_data(self):
        '''
        Ваша реализация сбора данных из буфера для заполнения файла.
        '''

    def evacuate(self):
        '''
        Эвакуирует собранные методом collect_data данные из буфера в файл.
        '''

        data = self._collect_data()
        with open(self.path_to_file, 'a') as f:
            f.write(data)
        self.buffer = []


class StorageTXT(BaseStorage):
    
    def _create_file(self):
        '''
        Создает пустой текстовый файл.
        '''
        with open(self.path_to_file, 'a'):
            pass
    
    def _collect_data(self) -> str:
        '''
        Собирает данные из буфера, соединяя данные из кортежа пробелом.
        Returns:
            Строка с собранными данными.
        '''
        
        result_string = ''
        for tup in self.buffer:
            result_string += ' '.join(tup) + '\n'
            
        return result_string
  
    
class StorageCSV(BaseStorage):
    
    def _create_file(self):
        '''
        Создает файл .csv и вносит заголовки date;metric;value, если такого файла не было.
        '''
        mode = 'a'
        line = 'date;metric;value\n'
        if os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'r') as file:
                if not file.readlines():
                    mode = 'w'
                else:
                    line = ''
        with open(self.path_to_file, mode) as f:
            f.write(line)
    
    def _collect_data(self) -> str:
        '''
        Собирает данные из буфера, соединяя данные из кортежа точкой с запятой.
        Returns:
            Строка с собранными данными.
        '''

        result_string = ''
        for tup in self.buffer:
            result_string += ';'.join(tup) + '\n'

        return result_string


class Statsd:
    def __init__(self, storage: BaseStorage):
        """Реализуйте класс"""
        self.storage = storage

    def _formate_data_and_send_to_buffer(self, message: str, metric: int):
        '''
        Формирует данные для отправки в буфер и отправляет их в буфер.
        Args:
            message - Описание метрики.
            metric - Значение метрики.
        Example:
            Данные в буфер помещаются в виде кортежа ('%Y-%m-%dT%H:%M:%S%z', message, metric), где
            первый элемент - дата и время в формате UTC с указанием временной зоны,
            второй элемент - описание метрики,
            третий элемент - значение метрики.
        '''

        self.storage.add_data_to_buffer(
            (datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%S%z'), message, str(metric))
        )

    def incr(self, message: str):
        '''
        Производит повышение метрики с заданным описанием.
        Args:
            message - Описание метрики
        '''

        self._formate_data_and_send_to_buffer(message, 1)
        try:
            self.storage.is_buffer_overflow()
        except OverflowError:
            self.storage.evacuate()

    def decr(self, message: str):
        '''
        Производит понижение метрики с заданным описанием.
        Args:
            message - Описание метрики
        '''

        self._formate_data_and_send_to_buffer(message, -1)
        try:
            self.storage.is_buffer_overflow()
        except OverflowError:
            self.storage.evacuate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.storage.evacuate()


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для текстового файла"""
    if not path.endswith('txt'):
        raise ValueError
    storage = StorageTXT(path, buffer_limit)
    return Statsd(storage)


def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
    """Реализуйте инициализацию метрик для csv файла"""
    if not path.endswith('csv'):
        raise ValueError
    storage = StorageCSV(path, buffer_limit)
    return Statsd(storage)

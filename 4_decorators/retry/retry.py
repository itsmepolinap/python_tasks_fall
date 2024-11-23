from datetime import timedelta
from time import sleep
# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])

def retry(count: int, delay: timedelta, handled_exceptions: tuple[Exception] = None):
    if count < 1:
        raise ValueError
    if handled_exceptions is None:
        handled_exceptions = (Exception, )
    def decorator(func):
        def wrap(*args,**kwargs):
            for attempt in range(count):
                try:
                    return func(args,kwargs)
                except handled_exceptions:
                    if attempt + 1 == count:
                        raise 
                sleep(delay.total_seconds())
        return wrap     
    return decorator


                

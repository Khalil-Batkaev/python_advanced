import logging
from typing import Callable
from functools import wraps

FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(level=logging.INFO, filename='logs.log', encoding='utf-8', format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'{func.__name__} - {str(args)}, {kwargs} - {result}')
        return result
    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num**2


any_name(10, 42, name='Stanislav', x=3)
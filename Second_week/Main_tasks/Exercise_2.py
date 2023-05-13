import json
from functools import wraps

def to_json(function) :
	'''Декоратор, который переводит вывод функции в json формат '''
    @wraps(function)
    def wrapper(*args, **kwargs) :
        i = function(*args, **kwargs)
        result = json.dumps(i)
        return result
    return wrapper

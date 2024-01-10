from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}  # dict: args -> result

    def wrapper(*args) -> Any:
        if args in cache_dict :
            print("Getting from cache")
            return cache_dict[args]
        else :
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
        return result
    return wrapper

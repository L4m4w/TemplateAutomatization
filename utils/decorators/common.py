import re
import types
from functools import wraps
from allure_commons._core import plugin_manager
from allure_commons.utils import uuid4


def humanify(name: str) -> str:
   return " ".join(re.split('_+',name))

def step(fn=None):
    def _pseudo_step(func=None):
        @wraps(func)
        def fn_with_logging(*args, **kwargs):
            # if callable(fn):
            fn_name = humanify(func.__name__)
            is_method = (
                args
                and isinstance(args[0], object)
                and isinstance(getattr(args[0], func.__name__), types.MethodType)
            )
            args_to_log = args[1:] if is_method else args
            args_and_kwargs_to_log_as_strings = [
                *map(str, args_to_log),
                # *[f"{key}={value}" for key, value in kwargs.items()]
                *map(lambda pair: f'{pair[0]}={pair[1]}' , kwargs.items())
            ]
            print(
                 (f'[{args[0].__class__.__name__}] ' if is_method else '[Function]')
                + fn_name
                + (
                    (
                        (': ' +', '.join(str(arg)
                                         for arg in args_and_kwargs_to_log_as_strings)
                        )
                    if args_and_kwargs_to_log_as_strings else ''
                    )
                )
                 + ('; ' + 'Fixture argument: "' + (str(fn)) + '"' if not callable(fn) else '')
            )

            return func(*args, **kwargs)
        return fn_with_logging
    return _pseudo_step(fn) if callable(fn) else _pseudo_step

def step_for_allure(fn=None):
    def _pseudo_step(func=None):
        @wraps(func)
        def fn_with_logging(*args, **kwargs):
            # if callable(fn):
            fn_name = humanify(func.__name__)
            is_method = (
                args
                and isinstance(args[0], object)
                and isinstance(getattr(args[0], func.__name__), types.MethodType)
            )
            args_to_log = args[1:] if is_method else args
            args_and_kwargs_to_log_as_strings = [
                *map(str, args_to_log),
                # *[f"{key}={value}" for key, value in kwargs.items()]
                *map(lambda pair: f'{pair[0]}={pair[1]}' , kwargs.items())
            ]
            step_info = {
                 "step_info":(f'[{args[0].__class__.__name__}] ' if is_method else '[Function]')
                + fn_name
                + (
                    (
                        (': ' +', '.join(str(arg)
                                         for arg in args_and_kwargs_to_log_as_strings)
                        )
                    if args_and_kwargs_to_log_as_strings else ''
                    )
                )
                + ('; ' + 'Fixture argument: "' + (str(fn)) + '"' if not callable(fn) else '')
            }
            plugin_manager.hook.start_step(uuid=uuid4(), title='',params=dict(step_info))


            return func(*args, **kwargs)
        return fn_with_logging
    return _pseudo_step(fn) if callable(fn) else _pseudo_step
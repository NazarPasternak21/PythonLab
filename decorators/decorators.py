import subprocess
import logging


def method_call_logger(func):
    """Decorator that logs the calling of a method.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """

    def wrapper(*args, **kwargs):
        """Wrapper function that logs the calling of the decorated function."""
        print("Calling method:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


def pylint_checker(func):
    """Decorator that runs pylint on the file containing the decorated function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    executed = False

    def wrapper(*args, **kwargs):
        """Wrapper function that runs pylint on the file."""
        nonlocal executed
        if not executed:
            filename = func.__code__.co_filename
            command = f"pylint {filename}"
            print(f"Running pylint on file: {filename}")
            with subprocess.Popen(command, shell=True) as process:
                process.wait()
            executed = True
        return func(*args, **kwargs)

    return wrapper


def logged(exception, mode):
    """Parameterized decorator that logs exceptions in the specified mode (console or file).

    Args:
        exception (Exception): The exception to catch and log.
        mode (str): The mode to log exceptions, either 'console' or 'file'.

    Returns:
        function: The decorator.

    Raises:
        ValueError: If an invalid mode is provided.
    """

    def decorator(func):
        """Decorator function that wraps the decorated function and logs exceptions."""

        def wrapper(*args, **kwargs):
            """Wrapper function that catches and logs exceptions."""
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger('exception_logger')
                logger.setLevel(logging.DEBUG)
                if mode == 'console':
                    handler = logging.StreamHandler()
                elif mode == 'file':
                    handler = logging.FileHandler('exception.log')
                else:
                    raise ValueError(f"Invalid mode: {mode}. Valid modes are 'console' and 'file'.")
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                logger.exception(str(e))

        return wrapper

    return decorator

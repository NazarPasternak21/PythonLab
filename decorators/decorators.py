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


def logger(exception, mode):
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.ERROR)

    if mode == "console":
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
    elif mode == "file":
        file_handler = logging.FileHandler("logs.log")
        logger.addHandler(file_handler)
    else:
        raise ValueError("No matching mode")

    def decorator(input_func):
        def wrapper(*args, **kwargs):
            try:
                return input_func(*args, **kwargs)
            except exception as e:
                logger.error(str(e))

        return wrapper

    return decorator

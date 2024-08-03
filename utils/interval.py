__version__ = "0.1.0"
__author__ = "redatman"
__date__ = "2024-08-03"

# from threading import Thread
# from typing import Callable


# class ResultExecutorMixin:
#     start: Callable
#     _target: Callable
#     _args: tuple
#     _kwargs: dict
#     _result = None

#     def run(self):
#         try:
#             if self._target is not None:
#                 self._result = self._target(*self._args, **self._kwargs)
#         finally:
#             del self._target, self._args, self._kwargs

#     def join(self, *args):
#         super().join(*args)  # type: ignore
#         # logger.warning(getattr(self, "_result", None))
#         return getattr(self, "_result", None)

#     def get_result(self):
#         self.start()
#         return self.join()


# ResultThread = type("ResultThread", (ResultExecutorMixin, Thread), {})

from threading import Timer


class Interval(Timer):
    """Interval: Schedules a task to be run at an interval

    >>> my_task = lambda a, b: print(a, b)
    >>> scheduler = Interval(2, my_task, ("Hello", " world!"))
    >>> scheduler.start()

    # Let it run for 10 seconds then stop
    >>> time.sleep(10)
    >>> scheduler.cancel()
    """

    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            self.function(*self.args, **self.kwargs)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

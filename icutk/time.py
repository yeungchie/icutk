from __future__ import annotations
from time import perf_counter
from typing import Any, Callable, Optional

from .log import getLogger

__all__ = [
    "MeasureTime",
    "measureTime",
]


class MeasureTime:
    def __init__(self, func: Optional[Callable] = None) -> None:
        self.logger = getLogger()
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        if self.func is None:
            raise ValueError("No function provided")
        start_time = perf_counter()
        error = None
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            error = e
        end_time = perf_counter()
        self.logger.info(
            f"Procedure {self.func.__name__!r} took {end_time - start_time} seconds to run"
        )
        if error:
            raise error
        return result

    def __enter__(self) -> MeasureTime:
        self.start = perf_counter()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.logger.info(f"Program took {perf_counter() - self.start} seconds to run")


measureTime = MeasureTime

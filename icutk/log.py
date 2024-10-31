import logging

try:
    from rich.logging import RichHandler

    format = "%(message)s"
    datefmt = None
    handlers = [
        RichHandler(
            show_level=True,
            show_path=False,
            log_time_format="%H:%M:%S",
            omit_repeated_times=False,
        )
    ]
except ImportError:
    format = "%(asctime)s | %(levelname)s | %(message)s"
    datefmt = "%H:%M:%S"
    handlers = None

__all__ = [
    "logger",
]

logging.basicConfig(
    format=format,
    datefmt=datefmt,
    level=logging.INFO,
    handlers=handlers,
)
logger = logging.getLogger(__name__)

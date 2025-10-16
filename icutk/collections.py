from typing import Any, Iterable, Iterator, Tuple

__all__ = [
    "Pararmeter",
]


class Pararmeter:
    def __init__(self, *args, **kwargs) -> None:
        for k, v in dict(*args, **kwargs).items():
            key = str(k)
            if key.isidentifier():
                self.__dict__[key] = v
            else:
                raise ValueError(f"is not a valid identifier key - {key!r}")

    def __repr__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items()),
        )

    def __getattr__(self, *args, **kwargs) -> None:
        pass

    def __getitem__(self, name: str) -> Any:
        return self.__dict__[name]

    def __iter__(self) -> Iterator[Tuple[str, Any]]:
        return iter(self.__dict__.items())

    def get(self, *args, **kwargs) -> Any:
        return self.__dict__.get(*args, **kwargs)

    def keys(self) -> Iterable[str]:
        return tuple(self.__dict__.keys())

    def values(self) -> Iterable[Any]:
        return tuple(self.__dict__.values())

    def __call__(self, *args, default: Any = None) -> Tuple[Any, ...]:
        return tuple(self.get(k, default) for k in args)

from typing import Iterable, Optional, Union
import ply.lex as lex
import logging


class BaseLexer:
    tokens = [
        "PAREN_OPEN",  # (
        "PAREN_CLOSE",  # )
        "BRACKET_OPEN",  # [
        "BRACKET_CLOSE",  # ]
        "BRACE_OPEN",  # {
        "BRACE_CLOSE",  # }
        "ANGLE_OPEN",  # <
        "ANGLE_CLOSE",  # >
        "PLUS",  # +
        "MINUS",  # -
        "ASTERISK",  # *
        "SLASH",  # /
        "EQUAL",  # =
        "BACKTICK",  # `
        "TILDE",  # ~
        "EXCLAMATION",  # !
        "AT",  # @
        "HASH",  # #
        "DOLLAR",  # $
        "PERCENT",  # %
        "CARET",  # ^
        "AMPERSAND",  # &
        "BACKSLASH",  # \
        "PIPE",  # |
        "SEMICOLON",  # ;
        "COLON",  # :
        "APOSTROPHE",  # '
        "QUOTATION",  # "
        "COMMA",  # ,
        "DOT",  # .
        "QUESTION",  # ?
        "INT",  # 10
        "FLOAT",  # 1.23
        "WORD",  # WORD
    ]

    t_PAREN_OPEN = r"\("
    t_PAREN_CLOSE = r"\)"
    t_BRACKET_OPEN = r"\["
    t_BRACKET_CLOSE = r"\]"
    t_BRACE_OPEN = r"\{"
    t_BRACE_CLOSE = r"\}"
    t_ANGLE_OPEN = r"<"
    t_ANGLE_CLOSE = r">"
    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_ASTERISK = r"\*"
    t_SLASH = r"/"
    t_EQUAL = r"="
    t_BACKTICK = r"`"
    t_TILDE = r"~"
    t_EXCLAMATION = r"!"
    t_AT = r"@"
    t_HASH = r"\#"
    t_DOLLAR = r"\$"
    t_PERCENT = r"%"
    t_CARET = r"\^"
    t_AMPERSAND = r"&"
    t_BACKSLASH = r"\\"
    t_PIPE = r"\|"
    t_SEMICOLON = r";"
    t_COLON = r":"
    t_APOSTROPHE = r"'"
    t_QUOTATION = r'"'
    t_COMMA = r","
    t_DOT = r"\."
    t_QUESTION = r"\?"
    t_WORD = r"\w+"

    t_ignore = " \t"

    def t_INT(self, t):
        r"\d+(?!\.)"
        t.value = int(t.value)
        return t

    def t_FLOAT(self, t):
        r"\d+\.\d+"
        t.value = float(t.value)
        return t

    def t_NEWLINE(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        logging.warning(f"Illegal character {repr(t.value[0])}")
        t.lexer.skip(1)

    def __init__(self, data: Optional[Union[str, Iterable[str]]] = None) -> None:
        self.lexer = lex.lex(module=self)
        if data is not None:
            if isinstance(data, str):
                self.lexer.input(data)
            elif isinstance(data, Iterable):
                self.lexer.input("".join(data))
            else:
                raise TypeError("data must be str or iterable of str")

    def input(self, s: str) -> None:
        self.lexer.input(s)

    def __iter__(self):
        return self.lexer

    def token(self):
        return self.lexer.token()

    def __next__(self):
        t = self.token()
        if t is None:
            raise StopIteration
        return t

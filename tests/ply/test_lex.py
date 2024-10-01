from icutk.ply.lex import BaseLexer


code = """\
1 - .SUBCKT NAND2 A B VDD VSS Y
2 - *.PININFO A:I B:I Y:O VDD:B VSS:B
3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u
4 - XNM2 net0 B VSS VSS nmos m=1 length=600n width=1u
5 - XPM1 Y B VDD VDD VSS pmos m=1 length=600n width=2u
6 - XPM2 Y A VDD VDD VSS pmos m=1 length=600n width=2u
7 - .ENDS
"""


class TestBaseLexer:
    def test_lexer(self):
        lexer = BaseLexer()
        lexer.input(code)
        tokens = list(lexer)
        assert len(tokens) == 112
        assert {t.type for t in tokens} == {
            "DOT",
            "ASTERISK",
            "WORD",
            "MINUS",
            "EQUAL",
            "COLON",
            "INT",
        }

        assert tokens[0].type == "INT"
        assert tokens[0].value == 1

        assert tokens[1].type == "MINUS"
        assert tokens[1].value == "-"

        assert tokens[2].type == "DOT"
        assert tokens[2].value == "."

        assert tokens[3].type == "WORD"
        assert tokens[3].value == "SUBCKT"

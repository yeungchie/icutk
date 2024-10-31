from icutk.lex import BaseLexer


code = """\
1 - .SUBCKT NAND2 A B VDD VSS Y
2 - *.PININFO A:I B:I Y:O VDD:B VSS:B
3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u
4 - XNM2 net0 B VSS VSS nmos m=1 length=600n width=1u
5 - XPM1 Y B VDD VDD VSS pmos m=1 length=600n width=2u
6 - XPM2 Y A VDD VDD VSS pmos m=1 length=600n width=2u
7 - .ENDS
"""

lexer = BaseLexer()
lexer.input(code)
tokens = list(lexer)


class TestBaseLexer:
    def test_token_len(self):
        assert len(tokens) == 112

    def test_token_types(self):
        assert {t.type for t in tokens} == {"*", "-", ".", ":", "=", "ID", "INT"}

    def test_token_values(self):
        assert tokens[0].type == "INT"
        assert tokens[0].value == 1

        assert tokens[1].type == "-"
        assert tokens[1].value == "-"

        assert tokens[2].type == "."
        assert tokens[2].value == "."

        assert tokens[3].type == "ID"
        assert tokens[3].value == "SUBCKT"

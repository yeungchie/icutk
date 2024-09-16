import re

from icutk.string import LineIterator


STRINGS = """\
1 - .SUBCKT NAND2 A B VDD VSS Y
2 - *.PININFO A:I B:I Y:O VDD:B VSS:B
3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u
4 - XNM2 net0 B VSS VSS nmos m=1 length=600n width=1u
5 - XPM1 Y B VDD VDD VSS pmos m=1 length=600n width=2u
6 - XPM2 Y A VDD VDD VSS pmos m=1 length=600n width=2u
7 - .ENDS
""".splitlines(keepends=True)


class TestDataIterator:
    def test_next(self):
        di = LineIterator(STRINGS)
        for s in STRINGS:
            assert di.next == s

    def test_chomp(self):
        di = LineIterator(STRINGS, chomp=True)
        for s in STRINGS:
            assert di.next == re.sub(r"\n$", "", s)

    def test_last(self):
        di = LineIterator(STRINGS, chomp=True)
        next_count = 3
        for _ in range(next_count):
            di.next

        # 第 3 行
        assert di.last1 == "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u"

        # 前 3 行
        assert di.last == [
            "1 - .SUBCKT NAND2 A B VDD VSS Y",
            "2 - *.PININFO A:I B:I Y:O VDD:B VSS:B",
            "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u",
        ]

    def test_revert(self):
        di = LineIterator(STRINGS, chomp=True)
        next_count = 3
        for _ in range(next_count):
            di.next

        # 第 4 行
        assert di.next == "4 - XNM2 net0 B VSS VSS nmos m=1 length=600n width=1u"

        di.revert()  # 回退一行

        # 第 3 行
        assert di.last1 == "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u"

        # 前 3 行
        assert di.last == [
            "1 - .SUBCKT NAND2 A B VDD VSS Y",
            "2 - *.PININFO A:I B:I Y:O VDD:B VSS:B",
            "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u",
        ]

        di.revert()  # 回退一行

        # 第 2 行
        assert di.last1 == "2 - *.PININFO A:I B:I Y:O VDD:B VSS:B"

        # 前 2 行
        assert di.last == [
            "1 - .SUBCKT NAND2 A B VDD VSS Y",
            "2 - *.PININFO A:I B:I Y:O VDD:B VSS:B",
        ]

        # 第 3 行
        assert di.next == "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u"

        di.revert()  # 回退一行

        # 第 2 行
        assert di.last1 == "2 - *.PININFO A:I B:I Y:O VDD:B VSS:B"

        # 偷看下一行
        assert di.peek_next == "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u"

        # 迭代剩下的所有行
        assert di.next == "3 - XNM1 Y A net0 VSS nmos m=1 length=600n width=1u"
        assert di.next == "4 - XNM2 net0 B VSS VSS nmos m=1 length=600n width=1u"
        assert di.next == "5 - XPM1 Y B VDD VDD VSS pmos m=1 length=600n width=2u"
        assert di.next == "6 - XPM2 Y A VDD VDD VSS pmos m=1 length=600n width=2u"
        assert di.next == "7 - .ENDS"

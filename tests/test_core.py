import pytest
from lib.core import basic_interpreter

class Test_basic_functin:

    def test_basic_interpreter_correct_spelling_Short(self):
        fun = basic_interpreter('#add test')
        assert fun == ('#add test')

    def test_basic_interpreter_correct_spelling_Long(self):
        fun = basic_interpreter('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami')
        assert fun == ('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami')

    def test_basic_interpreter_reverst_spelling_order_Long(self):
        fun = basic_interpreter('jakas tresc #add')
        assert fun == ('')

    def test_basic_interpreter_reverst_spelling_order_Short(self):
        fun = basic_interpreter('tresc #add')
        assert fun == ('')

    def test_basic_interpreter_order_orphan_on_the_end(self):
        fun = basic_interpreter('#add jakas forma testci #add')
        assert fun == ('#add jakas forma testci')

    def test_basic_interpreter_some_empty_ORDER(self):
        fun = basic_interpreter('#add #del jakas forma #add #del testci #add #add #del')
        assert fun == ('#del jakas forma #del testci')

    def test_basic_interpreter_only_one_ORDER(self):
        fun = basic_interpreter('#add')
        assert fun == ('')

    def test_basic_interpreter_only_one_CONTENT(self):
        fun = basic_interpreter('jakas tresc')
        assert fun == ('')

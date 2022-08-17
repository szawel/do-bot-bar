import pytest
from lib.basic_interpreter import BasicInterpreter

class Test_basic_functin:

    def test_basic_interpreter_correct_spelling_Short(self):
        fun = BasicInterpreter('#add test')
        assert fun == ('#add test')

    def test_BasicInterpreter_correct_spelling_Long(self):
        fun = BasicInterpreter('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami')
        assert fun == ('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami')

    def test_BasicInterpreter_reverst_spelling_order_Long(self):
        fun = BasicInterpreter('jakas tresc #add')
        assert fun == ('')

    def test_BasicInterpreter_reverst_spelling_order_Short(self):
        fun = BasicInterpreter('tresc #add')
        assert fun == ('')

    def test_BasicInterpreter_order_orphan_on_the_end(self):
        fun = BasicInterpreter('#add jakas forma testci #add')
        assert fun == ('#add jakas forma testci')

    def test_BasicInterpreter_some_empty_ORDER(self):
        fun = BasicInterpreter('#add #del jakas forma #add #del testci #add #add #del')
        assert fun == ('#del jakas forma #del testci')

    def test_BasicInterpreter_only_one_ORDER(self):
        fun = BasicInterpreter('#add')
        assert fun == ('')

    def test_BasicInterpreter_only_one_CONTENT(self):
        fun = BasicInterpreter('jakas tresc')
        assert fun == ('')

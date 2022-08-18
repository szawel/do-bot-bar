import pytest
import json
from lib.basic_interpreter import BasicInterpreter

with open('settings\orders.json') as f:
    data = json.load(f)

# load orders list
for state in data['user_orders']:
    orders_list = state['list_orders']

# load utility list 
for state in data['user_orders']:
    utility_list = state['utility_orders']

user_order_lists = orders_list + utility_list

class Test_basic_functin:


    def test_basic_interpreter_correct_spelling_Short(self):
        fun = BasicInterpreter('#add test',user_order_lists)
        assert fun == ('#add test')

    def test_BasicInterpreter_correct_spelling_Long(self):
        fun = BasicInterpreter('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami',user_order_lists)
        assert fun == ('#add no i tu sie zaczyna wpisywanie w pizdu treść nawet z polskimi znakami')

    def test_BasicInterpreter_reverst_spelling_order_Long(self):
        fun = BasicInterpreter('jakas tresc #add',user_order_lists)
        assert fun == ('')

    def test_BasicInterpreter_reverst_spelling_order_Short(self):
        fun = BasicInterpreter('tresc #add',user_order_lists)
        assert fun == ('')

    def test_BasicInterpreter_order_orphan_on_the_end(self):
        fun = BasicInterpreter('#add jakas forma testci #add',user_order_lists)
        assert fun == ('#add jakas forma testci')

    def test_BasicInterpreter_some_empty_ORDER(self):
        fun = BasicInterpreter('#add #del jakas forma #add #del testci #add #add #del',user_order_lists)
        assert fun == ('#del jakas forma #del testci')

    def test_BasicInterpreter_only_one_ORDER(self):
        fun = BasicInterpreter('#add',user_order_lists)
        assert fun == ('')

    def test_BasicInterpreter_only_one_CONTENT(self):
        fun = BasicInterpreter('jakas tresc',user_order_lists)
        assert fun == ('')

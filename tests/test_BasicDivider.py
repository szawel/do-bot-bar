import pytest
import json
from lib.basic_divider import BasicDivider

with open('settings/orders.json') as f:
    data = json.load(f)

# load orders list
for state in data['user_orders']:
    orders_list = state['list_orders']

# load utility list 
for state in data['user_orders']:
    utility_list = state['utility_orders']

user_order_lists = orders_list + utility_list


class Test_BasicDivider:


    def test_BasicDivider_multi_order_call(self):
        todo = BasicDivider('#add jeden #add dwa #add trzy')
        assert todo == (['#add jeden', '#add dwa', '#add trzy'])

    def test_BasicDivider_dual_order_call(self):
        todo = BasicDivider('#add jeden #del ja')
        assert todo == (['#add jeden', '#del ja'])

    def test_BasicDivider_single_multi_order_call(self):
        todo = BasicDivider('#del jeden')
        assert todo == (['#del jeden'])

    def test_BasicDivider_empty_multi_order_call(self):
        todo = BasicDivider('')
        assert todo == ([])

    def test_BasicDivider_next_multi_order_call(self):
        todo = BasicDivider('#add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen #add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen #add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen #add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen')
        assert todo == (['#add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen', '#add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen', '#add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen', '#add jueden csek c nwe i vnpo iwec jp iecjdfoi nfdoi nidnifen'])
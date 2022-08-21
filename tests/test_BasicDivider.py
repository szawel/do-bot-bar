import pytest
import json
from lib.basic_divider import BasicDivider
from lib.load_orders import LoadOrders

user_order_lists = LoadOrders()


class Test_BasicDivider:


    def test_BasicDivider_multi_order_call(self):
        todo = BasicDivider('#add jeden #add dwa #add trzy', user_order_lists)
        assert todo == (['#add jeden', '#add dwa', '#add trzy'])

    def test_BasicDivider_dual_order_call(self):
        todo = BasicDivider('#add jeden #del ja', user_order_lists)
        assert todo == (['#add jeden', '#del ja'])

    def test_BasicDivider_single_multi_order_call(self):
        todo = BasicDivider('#del jeden', user_order_lists)
        assert todo == (['#del jeden'])

    def test_BasicDivider_empty_multi_order_call(self):
        todo = BasicDivider('', user_order_lists)
        assert todo == ([])

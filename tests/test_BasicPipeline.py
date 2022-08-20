import pytest
import json
from basic_runner import BasicPipeline

with open('settings/orders.json') as f:
    data = json.load(f)

# load orders list
for state in data['user_orders']:
    orders_list = state['orders']

user_order_lists = orders_list

class Test_Pipeline:

    def test_BasicPipeline_single_add_order(self):
        fun = BasicPipeline('#add test',user_order_lists)
        assert fun == (['#add test'])

    def test_BasicPipeline_single_and_longer_add_order(self):
        fun = BasicPipeline('#add test kon ja ty my wy on 1 1 1 1 1 1',user_order_lists)
        assert fun == (['#add test kon ja ty my wy on 1 1 1 1 1 1'])
    
    def test_BasicPipeline_dubel_add_order(self):
        fun = BasicPipeline('#add cos do listy #add cos kolejnego do list',user_order_lists)
        assert fun == (['#add cos do listy','#add cos kolejnego do list'])

    def test_BasicPipeline_triple_add_order(self):
        fun = BasicPipeline('#add cos do listy #add cos kolejnego do list #add wisienke na torcie',user_order_lists)
        assert fun == (['#add cos do listy','#add cos kolejnego do list','#add wisienke na torcie'])

    def test_BasicPipeline_single_del_order(self):
        fun = BasicPipeline('#del test',user_order_lists)
        assert fun == (['#del test'])

    def test_BasicPipeline_single_and_longer_del_order(self):
        fun = BasicPipeline('#del test kon ja ty my wy on 1 1 1 1 1 1',user_order_lists)
        assert fun == (['#del test kon ja ty my wy on 1 1 1 1 1 1'])
    
    def test_BasicPipeline_dubel_del_order(self):
        fun = BasicPipeline('#del cos do listy #del cos kolejnego do list',user_order_lists)
        assert fun == (['#del cos do listy','#del cos kolejnego do list'])

    def test_BasicPipeline_triple_del_order(self):
        fun = BasicPipeline('#del cos do listy #del cos kolejnego do list #del wisienke na torcie',user_order_lists)
        assert fun == (['#del cos do listy','#del cos kolejnego do list','#del wisienke na torcie'])

    def test_BasicPipeline_dubel_add_and_del_order(self):
        fun = BasicPipeline('#add cos do listy #del cos kolejnego do list',user_order_lists)
        assert fun == (['#add cos do listy','#del cos kolejnego do list'])

    def test_BasicPipeline_dubel_del_and_add_order(self):
        fun = BasicPipeline('#del cos do listy #add cos kolejnego do list',user_order_lists)
        assert fun == (['#del cos do listy','#add cos kolejnego do list'])

    def test_BasicPipeline_empty_add_order(self):
        fun = BasicPipeline('',user_order_lists)
        assert fun == ([])

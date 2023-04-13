'''
Created on May 17, 2021

@author: martinyanev
'''

from tasks import Task

def test_task_equility():
    t1 = Task('sit there', 'james')
    t2 = Task('do something', 'smith')
    assert t1 == t2
    

def test_dict_equality():
    t1_dict = Task('make sandwich', 'smith')._asdict()
    t2_dict = Task('make sandwich', 'smit')._asdict()
    assert t1_dict == t2_dict
    
    
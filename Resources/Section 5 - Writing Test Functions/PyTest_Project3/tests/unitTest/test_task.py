'''
Created on May 17, 2021

@author: martinyanev
'''

from tasks import Task

def test_asdict():
    t_task = Task('take action', 'smith', True, 32)
    t_dict = t_task._asdict()
    expected = {'summary': 'take action',
                'owner': 'smith',
                'done': True,
                'id': 32}
    assert t_dict == expected
    
def test_replace():
    t_before = Task('complete course', 'james', False)
    t_after = t_before._replace(id=9, done=True)
    t_expected = Task('complete course', 'james', True, 9)
    assert t_after == t_expected
    

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    t = Task('get cheese', 'james')
    assert t.summary == 'get cheese'
    assert t.owner == 'james'
    assert (t.done, t.id) == (False, None)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
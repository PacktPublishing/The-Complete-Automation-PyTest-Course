'''
Created on May 17, 2021

@author: martinyanev
'''
import pytest
import tasks
from tasks import Task

def test_add_1():
    task = Task('run', 'JAMES', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    
def equivalent(t1, t2):
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))
    

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield 
    tasks.stop_tasks_db()
    
@pytest.mark.parametrize('task',
                         [Task('lift', done=True),
                          Task('swim', 'james'),
                          Task('run', 'JAMES', True),
                          Task('play', 'JaMeS', False)])


def test_add_2(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    
@pytest.mark.parametrize('summary, owner, done',
                         [('lift', None, False),
                          ('swim', 'james', False),
                          ('run', 'JAMES', True),
                          ('exercise', 'JaMeS', False),
                          ])

def test_add_3(summary, owner, done):
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


tasks_to_try = (Task('lift', done=True),
                Task('swim', 'james'),
                Task('swim', 'james'),
                Task('run', 'JAMES', True),
                Task('play', 'JaMeS', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done)
            for t in tasks_to_try]

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task', [
    pytest.param(Task('set'), id='just summary'),
    pytest.param(Task('start', 'Pamela'), id='summary/owner'),
    pytest.param(Task('finish', 'Pamela', True), id='summary/owner/done')])
def test_add_6(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():

    def test_equivalent(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id













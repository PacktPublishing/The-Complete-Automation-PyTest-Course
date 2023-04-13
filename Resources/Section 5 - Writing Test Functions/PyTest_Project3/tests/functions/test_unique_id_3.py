
import pytest
import tasks
from tasks import Task


@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason=' higher version than 0.2.0 required')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task('first')))
    ids.append(tasks.add(Task('second')))
    ids.append(tasks.add(Task('third')))

    uid = tasks.unique_id()
    
    assert uid not in ids


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

    
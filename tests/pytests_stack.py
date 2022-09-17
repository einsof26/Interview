from stack import Stack


data = [1, 2, 3]
data_empty = []
instanse = Stack(data)
instanse_empty = Stack(data_empty)


def test_isEmpty_False():
    result = instanse.isEmpty()
    assert result == False


def test_isEmpty_True():
    result = instanse_empty.isEmpty()
    assert result == True


def test_pop():
    result = instanse.pop()
    assert result == 3


def test_peek():
    result = instanse.peek()
    assert result == 2


def test_size():
    result = instanse.size()
    assert result == 2


def test_push():
    result = instanse.push(5)
    assert result == 5

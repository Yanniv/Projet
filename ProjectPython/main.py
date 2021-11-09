from my_lib_algo.Queue import Queue
from my_lib_algo.Stack import Stack


def test_queue():
    """
    You can use this function to test if the queue you
    implemented is working properly but remember that his
    is far from enough.
    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    tmp = q.dequeue()
    print("Expected 1, got " + tmp)  # Should print 1
    tmp = q.dequeue()
    print("Expected 2, got " + tmp)  # Should print 2


def test_stack():
    """
    You can use this function to test if the stack you
    implemented is working properly but remember that his
    is far from enough.
    """
    q = Stack()
    q.push(1)
    q.push(2)

    tmp = q.pop()
    print("Expected 2, got " + tmp)  # Should print 2
    tmp = q.pop()
    print("Expected 1, got " + tmp)  # Should print 1


test_queue()
test_stack()

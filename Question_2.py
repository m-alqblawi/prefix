from dataStructures import *
from random import randrange, seed


def question_2(Q, n):
    temp = Queue(Q)
    for i in range(temp.size):
        if temp.isEmpty:
            return temp
        else:
            temp = temp.dequeue()
            if temp != n:
                temp.enqueue(temp)
    return temp


pass


def test(n=10, flag=True):
    seed(0)
    Q = Queue()
    for i in range(10):
        Q.enqueue(randrange(50))
    print("Queue before : ", end=" ")
    Q.printQueue()
    print("Queue after : ", end=" ")
    try:
        question_2(Q, 3).printQueue()
    except:
        pass


def checker():
    test()


def main():
    checker()


if __name__ == "__main__":
    main()

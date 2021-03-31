from dataStructures import *
from random import randrange, seed


def question_1(alist1, alist2):

    for i, j in alist1, alist2:
        temp1 = Node(i)
        temp2 = Node(j)

        if temp1.data < temp2.data:
            temp1.



    pass
def test(n=10, flag=True):
    seed(0)
    alist1 = LinkedList()
    alist2 = LinkedList()
    a = sorted([randrange(50) for i in range(n)])[::-1]
    b = sorted([randrange(50) for i in range(n)])[::-1]
    if flag:
        print("first list :", *a)
        print("second list :", *b)
    for i in a:
        alist1.add(i)
    for i in b:
        alist2.add(i)
    o = question_1(alist1, alist2)
    if flag:
        print("out list:", end=" ")
        try:
            o.printList()
        except:
            pass


def checker():
    test(10)


def main():
    checker()


if __name__ == "__main__":
    main()

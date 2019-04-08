class LNode(object):
    """
    定义一个节点类
    """
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next

# llist1 = Node(1)
# head = llist1
#
# #创建链表
# for i in range(2,10):
#     head.next = Node(i)
#     head = head.next
#
# head = llist1#将head指针重新指向链表头
#
# while head != None:
#     print(head.data)
#     head = head.next


class LinkedListUnderflow(ValueError):
    """
    定义一个异常类
    """
    pass

class Llist:
    """
    定义一个链表类
    """
    def __init__(self):
        """
        初始化一个空链表
        """
        self._head = None

    def is_empty(self):
        """
        创建一个空链表
        :return:
        """
        return self._head is None

    def prepend(self,elem):
        """
        在表头插入元素
        :param elem:
        :return:
        """
        self._head = LNode(elem,self._head)

    def pop(self):
        """
        删除表头节点并返回节点里的数据
        :param elem:
        :return:
        """
        if self._head is None:  #无节点，引发异常
            raise LinkedListUnderflow("in pop")

        e = self._head.elem
        self._head = self._head.next

        return e

    def append(self,elem):
        """
        在链表末端插入数据
        :return:
        """
        if self._head is None:
            self._head = LNode(elem)

        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        """
        删除表中最后一个元素
        :return:
        """
        if self._head is None:#空表
            raise LinkedListUnderflow("in pop_last")

        p = self._head
        if p.next is None:#表中只有一个元素
            e = p.elem
            self._head = None
            return e

        while p.next.next != None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self,pred):
        p =self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(", ", end='')
            p = p.next
        print('')

    def for_each(self,proc):
        """
        此函数用于遍历一个元素集传统做法。
        :param proc:次参数是一个函数。
        :return:
        """
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield  p.elem
            p = p.next


    def filter(self,pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next



# mylist1 = Llist()
# for i in range(10):
#     mylist1.prepend(i)
# for i in range(11,20):
#     mylist1.append(i)

class Llist1(Llist):
    """
    链表的改进
    """
    def __init__(self):
        Llist.__init__(self)
        self._rear = None # 尾节点引用域

    def prepend(self,elem):
        self._head = LNode(elem,self._head)
        if self._rear is None:
            self._rear = self._head

    def append(self,elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


class LClist:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p #构建一个节点的循环链表
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self,elem):
        self.prepend(elem)
        self._rear = self._rear.next




















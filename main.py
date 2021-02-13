class BST:
    class Node:
        def __init__(self,value):
            self.value=value
            self.flag=True
            self.children=[None,None]
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=BST.Node(value)
        else:
            temp = self.root
            while self.root:

                if value == temp.value:
                    temp.flag=True
                    return
                elif value > temp.value:
                    if temp.children[1] is None:
                        temp.children[1] = BST.Node(value)
                        return
                    temp = temp.children[1]
                else:
                    if temp.children[0] is None:
                        temp.children[0] = BST.Node(value)
                        return
                    temp = temp.children[0]
    def insert_rec(self,value):
        def __insert_rec(cur,value):
            if value > cur.value:
                if cur.children[1] is None:
                    cur.children[1] = BST.Node(value)
                else:
                    __insert_rec(cur.children[1],value)
            elif value < cur.value:
                if cur.children[0] is None:
                    cur.children[0] = BST.Node(value)
                else:
                    __insert_rec(cur.children[0], value)
            else:
                cur.flag=True
                return
        if self.root is None:
            self.root = BST.Node(value)
        else:
            __insert_rec(self.root,value)

    def as_list(self):
        def __as_list(cur,l):
            if not cur:
                return
            __as_list(cur.children[0], l)
            if cur.flag:
                l.append(cur.value)
            __as_list(cur.children[1],l)
        l=[]
        __as_list(self.root, l)
        return l
    def __repr__(self):
        return 'BST('+ str(self.as_list())[1:-1] +')'
    def zdejmij_min(self):
        assert self.root is not None
        if self.root.children[0] is None:
            val = self.root.value
            self.root = self.root.children[0]
            return val
        else:
            cur = self.root
            while cur.children[0].children[0]:
                cur=cur.children[0]
            val = cur.children[0].value
            cur.children[0] = cur.children[0].children[1]
            return val
    def zdejmij_max(self):
        assert self.root is not None
        if self.root.children[1] is None:
            val=self.root.value
            self.root=self.root.children[0]
        cur = self.root
        while cur.children[1].children[1]:
            cur = cur.children[1]
        val = cur.children[1].value
        cur.children[1]=cur.children[1].children[0]
        return val
    def search(self,value):
        cur = self.root
        while cur is not None:
            if cur.value == value:
                if cur.flag:
                    return True
                else:
                    return False
            elif cur.value < value:
                cur = cur.children[1]
            else:
                cur = cur.children[0]
        return False
    def search_rec(self,value):
        def __search(cur,value):
            if cur is None:
                return False
            elif cur.value == value:
                return True
            elif cur.value < value:
                return __search(cur.children[1], value)
            else:
                return __search(cur.children[0], value)
        return __search(self.root,value)
    def height(self):
        def __height(node):
            if node is None:
                return 0
            if node.flag:
                return 1 + max(__height(node.children[0]), __height(node.children[1]))
            elif not node.flag:
                return max(__height(node.children[0]), __height(node.children[1]))
        return __height(self.root)
    def leaves_number(self):
        def __leaves_number(node):
            if node is None:
                return 0
            if node.flag:
                return __leaves_number(node.children[0]) + __leaves_number(node.children[1]) + 1
            elif not node.flag:
                return __leaves_number(node.children[0]) + __leaves_number(node.children[1])
        return __leaves_number(self.root)
    def pop_given(self,value):
        if self.root is None:
            raise ValueError("usuwanie z pustego")
        def __pop_given(rec,value):
            if rec.value == value:
                rec.flag=False
                return
            elif rec.value < value:
                return __pop_given(rec.children[1],value)
            else:
                return __pop_given(rec.children[0],value)
        return __pop_given(self.root,value)


def main():
    # drzewo=BST()
    # drzewo.insert(3)
    # drzewo.insert(5)
    # drzewo.insert(1)
    # print(drzewo)
    # drzewo.zdejmij_min()
    # print(drzewo)
    # print(drzewo.height())
    # print(drzewo.leaves_number())
    # drzewo.insert(1)
    # print(drzewo)
    # drzewo.insert_rec(7)
    # print(drzewo)
    # drzewo.insert_rec(100)
    # drzewo.insert(200)
    # drzewo.insert(1000000000000000)
    # drzewo.insert(-5)
    # print(drzewo)
    # print(drzewo.leaves_number())
    # print(drzewo.height())
    # drzewo.zdejmij_max()
    # print(drzewo)
    # print(drzewo.search(5))
    # drzewo.pop_given(5)
    # print(drzewo)
    # drzewo.pop_given(7)
    # print(drzewo)
    # drzewo.pop_given(-5)
    # print(drzewo)
    # drzewo.insert(-5)
    # print(drzewo)
    # print(drzewo.height())
    # drzewo.pop_given(-5)
    # print(drzewo)
    # print(drzewo.height())
    # print(drzewo.leaves_number())
    # print(drzewo.search(-5))
    pass
if __name__ == '__main__':
    main()

import collections
from typing import Optional


class TreeNode:
    def __init__(self, node: int):
        self.node = node
        self.left = None
        self.right = None

    def insert(self, data: int):
        if self.node:
            if data < self.node:
                if self.left is None:
                    self.left = TreeNode(node=data)
                else:
                    self.left.insert(data=data)
            elif data > self.node:
                if self.right is None:
                    self.right = TreeNode(node=data)
                else:
                    self.right.insert(data=data)
        else:
            self.node = data

    def print_tree(self) -> int:
        if self.left:
            self.left.print_tree()
        print(self.node, end=' ')
        if self.right:
            self.right.print_tree()

    @property
    def value(self) -> int:
        print(self.node)

    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        572:leetcode
        :param root:
        :param subRoot:
        :return:
        """
        if root is None and subRoot is None:
            return True
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        return self.helper(root=root, subRoot=subRoot) or self.isSubTree(root.left, subRoot) or self.isSubTree(root.rigth, subRoot)

    def helper_compare(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return root.node == subRoot.node and self.helper_compare(root.left, subRoot.left) and self.helper_compare(root.rigth, subRoot.right)

    def search(self, node: Optional[TreeNode], key: int) -> object:
        """
        Метод поиска по бинарному дереву
        если значения нет или родитель равен ключу, возвращаем родителя,
        если родитель от ключа меньше вызываем метод и в него передаем родетеля с ключем права и ключ,
        если не выполняются два условия, то возвращаем метод и в него передаем родителя с ключем лево и ключа
        :param node: родитель
        :param key: ключ
        :return: результат метода описанного выше
        """
        if node is None or node == key:
            return node

        if node < key:
            return self.search(node.right, key)

        return self.search(node.left, key)

    def invert_tree_ipt(self, node: Optional[list]) -> object:
        """
        Iterative Preorder Traversal
        :param node:
        :return:
        """
        if not node:
            return
        stack = [node]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def invert_tree_ilot(self, node: Optional[list]) -> object:
        """
        Iterative Level Order Traversal
        :param node:
        :return:
        """
        if not node:
            return node
        queue = collections.deque()
        queue.append(node)
        while len(queue):
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return node

    def invert_tree_via_recurse(self, node: Optional[list]) -> object:
        """
        With Recursion
        :param node:
        :return:
        """
        if node is None:
            return
        node.left, node.right = (self.invert_tree_via_recurse(node=node.right),
                                 self.invert_tree_via_recurse(node=node.left))
        return node


class CompareBinaryTree:
    def compare_tree(self, first_elem: object, second_elem: object) -> bool:
        if first_elem is None and second_elem is None:
            return True
        if first_elem is None or second_elem is None:
            return False
        if first_elem.val == second_elem.val:
            if self.compare_tree(first_elem=first_elem.left, second_elem=second_elem.left) and self.compare_tree(first_elem=first_elem.rigth, second_elem=second_elem.right):
                return True
        return False
        # if p is None and q is None:
        #     return True
        #
        # if p is not None and q is not None:
        #     return ((p.value == q.value) and
        #             self.compare_tree(p=p.left, q=q.left) and
        #             self.compare_tree(p=p.right, q=q.right))
        #
        # return False


if __name__ == '__main__':
    my_tree = TreeNode(node=1)
    my_tree.left = TreeNode(node=2)
    my_tree.right = TreeNode(node=3)
    my_tree.left.left = TreeNode(node=4)
    my_tree.left.right = TreeNode(node=5)

    my_tree_two = TreeNode(node=1)
    my_tree_two.left = TreeNode(node=2)
    my_tree_two.right = TreeNode(node=3)
    my_tree_two.left.left = TreeNode(node=4)
    my_tree_two.left.right = TreeNode(node=5)
    # my_tree.print_tree()
    # print()
    # my_tree_two.print_tree()
    # my_tree.invert_tree_via_recurse(root=my_tree)
    # print('')
    # my_tree.invert_tree_ILOT(root=my_tree)
    # my_tree.print_tree()
    # my_tree.invert_tree_IPT(root=my_tree)
    # print('')
    # my_tree.print_tree()
    # my_compare = CompareBinaryTree()
    # print(my_compare.compare_tree(p=my_tree, q=my_tree_two))
    my_tree.search(node=my_tree, key=5)

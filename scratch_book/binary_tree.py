import collections





class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data: int):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = TreeNode(value=data)
                else:
                    self.left.insert(data=data)
            elif data > self.value:
                if self.right is None:
                    self.right = TreeNode(value=data)
                else:
                    self.right.insert(data=data)
        else:
            self.value = data

    def print_tree(self) -> list:
        if self.left:
            self.left.print_tree()
        print(self.value, end=' ')
        if self.right:
            self.right.print_tree()

    def get_value(self) -> int:
        print(self.value)

    def invert_tree_via_recurse(self, root: object) -> object:
        """
        With Recursion
        :param root:
        :return:
        """
        if root is None:
            return
        root.left, root.right = (self.invert_tree_via_recurse(root=root.right),
                                 self.invert_tree_via_recurse(root=root.left))
        return root

    def invert_tree_IPT(self, root: object) -> object:
        """
        Iterative Preorder Traversal
        :param root:
        :return:
        """
        if not root:
            return
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    def invert_tree_ILOT(self, root: object) -> object:
        """
        Iterative Level Order Traversal
        :param root:
        :return:
        """
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while len(queue):
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root


if __name__ == '__main__':
    my_tree = TreeNode(value=1)
    my_tree.left = TreeNode(value=2)
    my_tree.right = TreeNode(value=3)
    my_tree.left.left = TreeNode(value=4)
    my_tree.left.right = TreeNode(value=5)

    my_tree.print_tree()
    # my_tree.invert_tree_via_recurse(root=my_tree)
    print('')
    my_tree.invert_tree_ILOT(root=my_tree)
    my_tree.print_tree()

    # my_tree.invert_tree_IPT(root=my_tree)
    print('')
    # my_tree.print_tree()

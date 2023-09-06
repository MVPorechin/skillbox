class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


my_tree = TreeNode(value=1)
my_tree.left = TreeNode(value=2)
my_tree.right = TreeNode(value=3)
my_tree.left.left = TreeNode(value=4)
my_tree.left.right = TreeNode(value=5)

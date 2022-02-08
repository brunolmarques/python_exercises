class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

    def push(self, value):
        if int(value) > int(self.data):
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.push(value)
        else:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.push(value)

    def get_sorted(self, sorted_data=None):

        if self.left:
            self.left.get_sorted(sorted_data)

        sorted_data.append(self.data)

        if self.right:
            self.right.get_sorted(sorted_data)

        return sorted_data


class BinarySearchTree:
    def __init__(self, tree_data):
        self.head = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            self.head.push(value)

    def data(self):
        return self.head

    def sorted_data(self):
        return self.head.get_sorted([])

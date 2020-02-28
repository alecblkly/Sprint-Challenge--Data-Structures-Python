class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
        else:
            return False

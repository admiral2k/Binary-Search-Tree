class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)

        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)

    def delete(self, val):
        if self is None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def min(self):
        if self.left:
            res = self.left.min()
        else:
            return self.val
        return res

    def max(self):
        if self.right:
            res = self.right.max()
        else:
            return self.val
        return res

    def inorder(self):
        return self.__inorder()

    def __inorder(self, vals=[]):
        if self.left:
            self.left.__inorder(vals)
        if self.val:
            vals.append(self.val)
        if self.right:
            self.right.__inorder(vals)
        return vals

    def preorder(self):
        return self.__preorder()

    def __preorder(self, vals=[]):
        if self.val:
            vals.append(self.val)
        if self.left:
            self.left.__preorder(vals)
        if self.right:
            self.right.__preorder(vals)
        return vals

    def postorder(self):
        return self.__postorder()

    def __postorder(self, vals=[]):
        if self.left:
            self.left.__postorder(vals)
        if self.right:
            self.right.__postorder(vals)
        if self.val:
            vals.append(self.val)
        return vals

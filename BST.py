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
        pass

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

    def exist(self, val):
        if self.val == val:
            return True
        if val > self.val:
            if self.right:
                res = self.right.exist(val)
            else:
                return False
        if val < self.val:
            if self.left:
                res = self.left.exist(val)
            else:
                return False
        return res


    def height(self):
        if self.val:
            height = self.__height(0, [0])
            return height

    def __height(self, current_height, heights):
        if self.left:
            self.left.__height(current_height + 1, heights)
        if self.right:
            self.right.__height(current_height + 1, heights)
        if not self.left and not self.right and current_height > heights[0]:
            heights[0] = current_height
        return heights[0]

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

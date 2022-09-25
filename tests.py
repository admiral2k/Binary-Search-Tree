from BST import BSTNode

node = BSTNode()
node.insert(5)
node.insert(4)
node.insert(8)
node.insert(4554)
node.insert(123)
node.insert(1)
node.delete(4554)
print(node.inorder())
print(node.preorder())
print(node.postorder())
print(node.min(), node.max())
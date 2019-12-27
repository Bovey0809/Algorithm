# %%
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootval(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


# %%
r = BinaryTree('Book')
r.insertLeft('Chapter 1')
r.insertRight('Chapter 2')
r.leftChild.insertLeft('Section 1.1')
r.leftChild.leftChild.insertLeft('Section 1.1.1')
r.leftChild.insertRight('Section 1.2')
r.rightChild.insertLeft('Section 2.1')
r.rightChild.insertRight('Section 2.2')
r.rightChild.rightChild.insertRight('Section 2.2.1')


# %%
def preorder(tree:BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
preorder(r)
# %%
def postorder(tree:BinaryTree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
postorder(r)

# %%
def inorder(tree:BinaryTree):
    if tree:
        inorder(tree.leftChild)
        print(tree.getRootVal())
        inorder(tree.rightChild)
inorder(r)

# %%


# %%

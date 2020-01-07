class TreeNode(object):
    """Tree node for Binary tree.

    Attributes:
        key: key value to index.
        payload: the value from the key.
        leftChild: left child node.
        rightChild: right child node.
        parent: parent node.
    """

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree(TreeNode):
    """Binary search tree.

    Attributes:
        root: root node.
        size: size of the tree.
    """

    def __init__(self:TreeNode):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        """Put an item into the BST.

        In order to put in the right position.
        BST should maintain the right structure.
        Using recursion _put() to help with find right place.

        Args:
            key: the key.
            val: the value.

        Returns:
            return None.
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode: TreeNode):
        """Put the key and val in BST.

        Keep in mind the BST property.

        Args:
            key: The node index.
            val: Value of the Node.
            currentNode: the current position in the node.

        Returns:
            return None.
        """
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        """Implement self[k] = v

        Args:
            k: key
            v: value

        Returns:
            return None
        """
        self.put(k, v)

    def get(self, key):
        """get the key from BST.
        
        Args:
            key: key for the BST.
        
        Returns:
            return self[key]
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        else:
            return None

    def _get(self, key, currentNode: TreeNode):
        """Find the key by comparing key to children.

        Args:
            key: key
            currentNode: current node.
        
        Returns:
            return the value find.
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        """if member in self.
        
        Args:
            key: key
        
        Returns:
            return Boolean.
        """
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
            else:
                raise KeyError('Error to delete, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree.')
    
    def __delitem__(self, key):
        self.delete(key)
    
    def spliceOut(self:TreeNode):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            
class BinHeap(object):
    """Binary Heap implement using list.

    insert, findMin, delMin, isEmpty, size, buildHeap

    Attributes:
        heapList: the list to init heap.
        currentSize: number of elements in heap.
    """

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i: int) -> None:
        """Swap item to the up.

        If the current node is smaller than the parent, swap,
        Until reaches the point it should be.

        Args:
            i: the index of the item in the list.

        Returns:
            return None
        """
        while i // 2 > 0:  # i // 2 is the parent node of the current index.
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i //
                                                2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, val: int) -> None:
        """insert the value in heap.

        Insert the val to the tail of the heap. 
        And find the right position.

        Args:
            val: an int

        Returns:
            return None
        """
        self.heapList.append(val)
        self.currentSize += 1
        # currentSize is the tail index of the new leaf.
        self.percUp(self.currentSize)

    def percDown(self, index: int) -> None:
        """Change nodes to the right place.

        Args:
            index: integer of the current node.

        Returns:
            return Nothing.
        """
        while (index * 2) <= self.currentSize:
            mc = self.minChild(index)
            if self.heapList[index] > self.heapList[mc]:
                self.heapList[index], self.heapList[mc] = self.heapList[mc], self.heapList[index]
            index = mc

    def minChild(self, i: int) -> int:
        """Return the smallest child of index i's node.

        Args:
            i: index of the node.

        Returns:
            return smalles child's index
        """
        # TODO: What if i is the tail.
        if i * 2 + 1 > self.currentSize:
            return i * 2
        return i * 2 if self.heapList[i * 2] < self.heapList[i * 2 + 1] else i * 2 + 1

    def delMin(self) -> int:
        """Delete the minimum leaf and maintain the tree.

        The smallest tree is the root of the tree.

        Args:
            self: tree

        Returns:
            return the deleted integer.
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist: list) -> None:
        """Build a heap with a list.

        Start from middle node, using percDown to maintain the tree.
        FROM BOTTOM TO TOP.
        The time complexity is O(n).

        Args:
            alist: A list of integers.

        Returns:
            return None
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist
        while i > 0:
            self.percDown(i)
            i -= 1


priority_queue = BinHeap()

priority_queue.buildHeap([9, 6, 5, 2, 3])

print(priority_queue.heapList)

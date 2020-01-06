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

    def percUp(self, i):
        """Swap item to the up.
        
        Args:
            i: the index of the item in the list.
        
        Returns:
            return None
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
                
    
    def insert(self, val):
        """insert the value in heap.
        
        Args:
            val: an int
        
        Returns:
            return None
        """

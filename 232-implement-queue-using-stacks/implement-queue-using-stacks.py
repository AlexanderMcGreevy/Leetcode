class MyQueue(object):

    def __init__(self):
        self.ar=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ar.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        return self.ar.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.ar[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.ar ==[]:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
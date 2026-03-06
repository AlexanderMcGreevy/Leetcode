class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        order=[]
        for x in points:
            d = (x[0]*x[0])+(x[1]*x[1])
            order.append([d,x])
        order = sorted(order)
        res =[]
        for x in range(k):
            res.append(order[x][1])
        return res
        
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        q=[]

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "#"
        
        for x,y in q:
            for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < height and 0 <= ny < width and mat[nx][ny] == "#":
                    mat[nx][ny] = mat[x][y] + 1
                    q.append((nx,ny))
        return mat
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        # get row and column index value 0
        # (0,0) (0,3)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        # then entire row 0 , column 0 --> (0,0)(0,1)(0,2) and (0,0)(1,0)(2,0)
        # the entire column 0, cloumn 3 --> (0,0)(1,0)(2,0) and (0,3)(1,3)(2,3)
        # means: we make a row and all column matrix[0][index] for row
        # and matrix[index][3] for column
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in column:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        
        

        

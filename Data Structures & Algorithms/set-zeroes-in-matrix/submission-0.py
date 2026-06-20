class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # ROWS, COLS = len(matrix), len(matrix[0])
        # rowZero = False

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             # condition 1 : entire column turns 0
        #             matrix[0][c] = 0
        #             # condition 2 : entire row turns 0
        #             if r > 0:
        #                 matrix[r][0] = 0
        #             # use the boolean incase of the overlap
        #             else:
        #                 rowZero = True
        
        # # Range starts from 1 because the 0th row and columns already have the 0s
        # # Columnwise 0
        # for r in range(1, ROWS):
        #     for c in range(1, COLS):
        #         if matrix[0][c] == 0 or matrix[r][0] == 0:
        #             matrix[r][c] = 0
        # # Rowise 0
        # if matrix[0][0] == 0:
        #     for r in range(ROWS):
        #         matrix[r][0] = 0

        # if rowZero:
        #     for c in range(COLS):
        #         matrix[0][c] = 0


        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0 :
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
            
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
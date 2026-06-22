class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            # number of rotations, for a 4x4 cube, youll need 3 rotations not 4, hence r - l
            for i in range(r - l):
                # square matrix thats why
                top, bottom = l, r

                # save topleft
                topleft = matrix[top][l + i]
                # bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # bottom right to bottom left without any memory usage
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # top right to bottom right without any memory usage
                matrix[bottom][r - i] = matrix[top + i][r]
                # top left to top right without any memory usage
                matrix[top + i][r] = topleft
            
            r -= 1
            l += 1

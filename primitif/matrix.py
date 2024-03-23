class Matrix3x3:
    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = self.zero_matrix()
        else:
            self.matrix = matrix

    @staticmethod
    def zero_matrix():
        return [[0, 0, 0] for _ in range(3)]

    @staticmethod
    def identity_matrix():
        mtemp = Matrix3x3.zero_matrix()
        for r in range(3):
            for c in range(3):
                mtemp[r][c] = int(r == c)
        return mtemp

    def mul_matrix(self, mb):
        mtemp = self.zero_matrix()
        for r in range(3):
            for c in range(3):
                mtemp[r][c] = (
                    self.matrix[r][0]*mb[0][c]
                    + self.matrix[r][1]*mb[1][c]
                    + self.matrix[r][2]*mb[2][c]
                )
        for r in range(3):
            for c in range(3):
                mb[r][c] = mtemp[r][c]

        return mb
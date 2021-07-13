# import numpy as np
from typing import List

class LinAlg:
    @staticmethod
    def zeros_matrix(rows, cols):
        zeros = []
        for i in range(rows):
            zeros.append([])
            for _ in range(cols):
                zeros[i].append(0)
        return zeros

    def addition(self, mat1, mat2):
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            raise ArithmeticError('Matrices are not the same size.')

        add = LinAlg.zeros_matrix(len(mat1), len(mat2[0]))
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                add[i][j] = mat1[i][j] + mat2[i][j]
        return add

    def subtract(self, mat1, mat2):
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            raise ArithmeticError('Matrices are not the same size.')

        sub = LinAlg.zeros_matrix(len(mat1), len(mat2[0]))
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                sub[i][j] = mat1[i][j] - mat2[i][j]
        return sub

    def transpose(self, mat):
        trans = LinAlg.zeros_matrix(len(mat[0]), len(mat))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                trans[j][i] = mat[i][j]
        return trans

    def scalar_multiply(self, mat, num):
        mul = LinAlg.zeros_matrix(len(mat), len(mat[0]))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mul[i][j] = mat[i][j] * num
        return mul

    def element_wise_product(self, mat1, mat2):
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            raise ArithmeticError('Matrices are not the same size.')

        result = LinAlg.zeros_matrix(len(mat1), len(mat2[0]))
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                result[i][j] = mat1[i][j] * mat2[i][j]
        return result

    def dot_product(self, mat1, mat2):
        dot = LinAlg.zeros_matrix(len(mat1),len(mat2[0]))
        if len(mat1[0]) == len(mat2):
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    for k in range(len(mat2)):
                        dot[i][j] += mat1[i][k] * mat2[k][j]
        return dot

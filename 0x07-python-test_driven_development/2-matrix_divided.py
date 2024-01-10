#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix using div

    Args:
        matrix:list containing integers or floats
        div:The divisor

    Returns:
        list:list of lists that represents the divided matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        'of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            'of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for z in row:
            if not isinstance(z, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)' +
                                'of integers/floats')
    result_matrix = [[round(z / div, 2) for z in row] for row in matrix]
    return result_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')

import numpy as np
from numpy_tasks import *

#np.__version__ - версия numpy должна быть больше 2.0

def test1():
    assert np.allclose(uniform_intervals(-1.2, 2.4, 7), np.array([-1.2, -0.6,  0. ,  0.6,  1.2,  1.8,  2.4]))
def test2():
    assert np.allclose(cyclic123_array(4), np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]))

def test3():
    assert np.allclose(first_n_odd_number(3), np.array([1, 3, 5]))

def test4():
    assert np.allclose(zeros_array_with_border(4), np.array([[1., 1., 1., 1.],
                                                             [1., 0., 0., 1.],
                                                             [1., 0., 0., 1.],
                                                             [1., 1., 1., 1.]]))
def test5():
    assert np.allclose(chess_board(3), np.array([[1., 0., 1.],
                                                 [0., 1., 0.],
                                                 [1., 0., 1.]]))

def test6():
    assert np.allclose(matrix_with_sum_index(3), np.array([[0, 1, 2],
                                                           [1, 2, 3],
                                                           [2, 3, 4]]))
def test7():
    assert np.allclose(cos_sin_as_two_rows(0, 1, 0.25), np.array([[1.        , 0.96891242, 0.87758256, 0.73168887],
                                                                  [0.        , 0.24740396, 0.47942554, 0.68163876]]))

def test8():
    np.random.seed(42)
    A = np.random.rand(3, 5)
    mean, rows_sum, columns_sum = compute_mean_rowssum_columnssum(A)
    assert np.abs(mean - 0.49456456164468965) < 1e-12
    assert np.allclose(rows_sum, np.array([0.55111913, 1.97870777, 2.43061273, 1.41211261, 1.04591619]))
    assert np.allclose(columns_sum, np.array([2.81192549, 2.38944187, 2.21710107]))

def test9():
    np.random.seed(42)
    A = np.random.rand(5, 5)
    assert np.allclose(sort_array_by_column(A, 1), np.array([[0.15599452, 0.05808361, 0.86617615, 0.60111501, 0.70807258],
                                                             [0.61185289, 0.13949386, 0.29214465, 0.36636184, 0.45606998],
                                                             [0.18340451, 0.30424224, 0.52475643, 0.43194502, 0.29122914],
                                                             [0.37454012, 0.95071431, 0.73199394, 0.59865848, 0.15601864],
                                                             [0.02058449, 0.96990985, 0.83244264, 0.21233911, 0.18182497]]))

def test10():
    f1 = lambda x: (x**2 + 3) / (x - 2)
    assert np.allclose(compute_integral(3, 4, f1, 0.001, method="rectangular"), 10.352030263919616, rtol=0.01)
    assert np.allclose(compute_integral(3, 4, f1, 0.001, method="trapezoidal"), 10.352030263919616, rtol=0.01)
    assert np.allclose(compute_integral(3, 4, f1, 0.001, method="simpson"), 10.352030263919616, rtol=0.001)

    f2 = lambda x: np.cos(x)**3
    assert np.allclose(compute_integral(0, np.pi/2, f2, 0.001, method="rectangular"), 2/3, rtol=0.01)
    assert np.allclose(compute_integral(0, np.pi/2, f2, 0.001, method="trapezoidal"), 2/3, rtol=0.01)
    assert np.allclose(compute_integral(0, np.pi/2, f2, 0.001, method="simpson"), 2/3, rtol=0.001)





import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)
    
    

def cyclic123_array(n): 
    """2. Генерирует numpy массив длины  3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)


def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    array = np.zeros((n, n), dtype=int)
    array[0, :] = 1
    array[-1, :] = 1
    array[:, 0] = 1
    array[:, -1] = 1
    return array

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    return (np.indices((n, n)).sum(axis=0) + 1) % 2

def matrix_with_sum_index(n):
    """6. Создаёт 𝑛 × 𝑛  матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    return np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    x = np.arange(a, b, dx)
    return np.vstack((np.cos(x), np.sin(x)))

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    mean = np.mean(A)
    row_sum = np.sum(A, axis=0)
    column_sum = np.sum(A, axis=1)
    return mean, row_sum, column_sum

def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    
    sorted_A = A[A[:, j].argsort()]

    return sorted_A

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:  
    method == 'rectangular' - методом прямоугольника   
    method == 'trapezoidal' - методом трапеций   
    method == 'simpson' - методом Симпсона  
    """
    n_intervals = int((b - a) / dx)
    x = np.linspace(a, b, n_intervals + 1)
    
    if method == 'rectangular':
        x_mid = x[:-1]  # Левая точка прямоугольника
        return np.sum(f(x_mid)) * dx

    elif method == 'trapezoidal':
        y = f(x)
        return (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) * dx / 2

    elif method == 'simpson':
        if n_intervals % 2 == 1:  # нужно чётное число отрезков → нечётное число точек
            x = np.linspace(a, b, n_intervals + 2)
            dx = (b - a) / (n_intervals + 1)
        
        y = f(x)
        return dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

    else:
        raise ValueError("Unknown method. Use 'rectangular', 'trapezoidal' or 'simpson'.")

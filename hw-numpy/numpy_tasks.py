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
    # Генерируем точки на отрезке [a, b] с шагом dx
    x = np.arange(a, b, dx)
    
    if method == 'rectangular':
        # Метод прямоугольников: используем левую границу
        return np.sum(f(x) * dx)
    
    elif method == 'trapezoidal':
        # Метод трапеций
        return np.sum((f(x[:-1]) + f(x[1:])) * dx / 2)
    
    elif method == 'simpson':
        n = len(x) - 1
        if n % 2 == 1:  # Метод Симпсона требует чётное число интервалов
            x = x[:-1]  # Убираем последнюю точку
            n -= 1
        
        return (dx / 3) * (f(x[0]) + 
                           4 * np.sum(f(x[1:n:2])) + 
                           2 * np.sum(f(x[2:n-1:2])) + 
                           f(x[n]))
    
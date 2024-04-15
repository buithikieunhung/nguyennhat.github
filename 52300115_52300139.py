import numpy as np
import math 

A = np.random.randint(1, 101, size=(10, 10))
B = np.random.randint(1, 21, size=(2, 10))
C = np.random.randint(1, 21, size=(10, 2))
print("Task 1: ")
#a
def a():
    print("a. ")
    result_a = A + A.T + np.dot(C, B) + np.dot(B.T, C.T)
    print("The result of a: ")
    print(result_a)
#b
def b():
    print("b. ")
    sum_b = result_b = np.zeros((10, 10), dtype= float)
    for i in np.arange(10,20):
        for j in np.arange(1,11):
            result_b += np.linalg.matrix_power(A / i, j)
    print("The result of b: ")
    print(result_b)
#c
def c():
    print("c. ")
    new_array = []
    for i in range(A.shape[0]):
        if i % 2 != 0:
            new_array.append(A[i])
    new_array = np.array(new_array)
    print("The result of c: ")
    print(new_array)
#d
def d():
    print("d. ")
    odd_numbers = []
    for row in A:
        for num_check_d in row:
            if num_check_d % 2 != 0:
                odd_numbers.append(num_check_d)
    resultant_vector = np.array(odd_numbers)
    print("The result of d: ")
    print(resultant_vector)
#e
def e():
    print("e. ")
    def check_prime(num_check_e):
        if num_check_e <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(num_check_e)) + 1):
                if num_check_e % i == 0:
                    return False
            return True

    prime_numbers = []
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if check_prime(A[i, j]):
                prime_numbers.append(A[i, j])
    print("The result of e: ")
    print(prime_numbers)
#f
def f():
    print("f. ")
    D = np.dot(C,B)
    print("Matrix D: \n",D)
    def reverse_odd_rows(matrix):
        for i in range(matrix.shape[0]):
            if i % 2 != 0:  
                matrix[i] = matrix[i, ::-1]  
        return matrix
    D_daodong = reverse_odd_rows(D)
    print("The result of f: ")
    print(D_daodong)
#g
def g():
    print("g. ")
    def check_prime(num_check_g):
        if num_check_g <= 1:
            return False
        else:
            for i in range(2, int(math.sqrt(num_check_g)) + 1):
                if num_check_g % i == 0:
                    return False
            return True
    def count_prime_in_row(row):
        count = 0
        for num_check_e in row:
            if check_prime(num_check_e):
                count += 1
        return count
    max_prime_count = 0
    rows_with_max_primes = []
    for i, row in enumerate(A):
        prime_count = count_prime_in_row(row)
        if prime_count > max_prime_count:
            max_prime_count = prime_count
            rows_with_max_primes = [i]
        elif prime_count == max_prime_count:
            rows_with_max_primes.append(i)
    print("The result of g: ")
    for row_index in rows_with_max_primes:
        print(A[row_index])
#h
def h():
    print("h. ")
    def longest_contiguous_odd_sequence(row):
        max_length = 0
        current_length = 0
        for num in row:
            if num % 2 != 0:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
        return max_length
    max_sequence_length = 0
    rows_with_longest_sequence = []
    for i, row in enumerate(A):
        sequence_length = longest_contiguous_odd_sequence(row)
        if sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
            rows_with_longest_sequence = [i]
        elif sequence_length == max_sequence_length:
            rows_with_longest_sequence.append(i)
    print("The result of h: ")
    for row_index in rows_with_longest_sequence:
        print(A[row_index])
#a()
#b()
#c()
#d()
#e()
#f()
#g()
#h()




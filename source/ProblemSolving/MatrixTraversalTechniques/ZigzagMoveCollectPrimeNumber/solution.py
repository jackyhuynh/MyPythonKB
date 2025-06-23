import math


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    # Handle number 2
    if n == 2:
        return True
    # Handle even number
    elif n % 2 == 0:
        return False
    # Handle odd number
    elif n % 2 == 1:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True


def zigzag_traverse_and_primes(matrix):
    rows = len(matrix)
    if rows == 0:  # Handle empty matrix
        return {}
    cols = len(matrix[0])  # Assuming it's an n x n matrix, so rows == cols
    if rows != cols:
        return {}
    traversed_list = []
    row = 0
    col = 0
    moving_right = True  # True for right, False for left

    while row < rows:
        # moving right
        if moving_right:
            while col < cols:
                traversed_list.append(matrix[row][col])
                col += 1

            moving_right = False
            col -= 1
            row += 1
        else:
            while col >= 0:
                traversed_list.append(matrix[row][col])
                col -= 1

            moving_right = True
            col += 1
            row += 1
    print(matrix)
    print(traversed_list)
    prime_list = {}
    for i in range(len(traversed_list)):
        if is_prime(traversed_list[i]):
            prime_list[i] = traversed_list[i]

    return prime_list


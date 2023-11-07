import sys

def findMultiplications(p, i, j):
    if i == j:
        return 0

    _min = sys.maxsize
    for k in range(i, j):
        count = (findMultiplications(p, i, k)
                + findMultiplications(p, k + 1, j)
                + p[i-1] * p[k] * p[j])

        if count < _min:
            _min = count
    return _min


# Driver code
if __name__ == '__main__':
    # dimension of the ith matrix is (arr[i-1] * arr[i])
    arr = [4, 4, 2, 6, 3]
    N = len(arr)
    print("Minimum number of multiplications is ", findMultiplications(arr, 1, N-1))

"""
OUTPUT:
Minimum number of multiplications is  92
"""
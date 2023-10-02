import ctypes

lib = ctypes.CDLL('./app/calculator/algorithms/c/MyDistances.so')

#./app/calculator/algorithms/
lib.LevenshteinDistance.argtypes = [ctypes.c_wchar_p, 
                                    ctypes.c_wchar_p, 
                                    ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]
lib.LevenshteinDistance.restype = ctypes.c_int

lib.DamerauLevenshteinDistance.argtypes = [ctypes.c_wchar_p, 
                                           ctypes.c_wchar_p, 
                                           ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]
lib.DamerauLevenshteinDistance.restype = ctypes.c_int

lib.DamerauLevenshteinDistanceRecursive.argtypes = [ctypes.c_wchar_p, ctypes.c_int, 
                                                    ctypes.c_wchar_p, ctypes.c_int]
lib.DamerauLevenshteinDistanceRecursive.restype = ctypes.c_int

lib.DamerauLevenshteinDistanceRecCache.argtypes = [ctypes.c_wchar_p, ctypes.c_int, 
                                                   ctypes.c_wchar_p, ctypes.c_int, 
                                                   ctypes.POINTER(ctypes.POINTER(ctypes.c_int))]
lib.DamerauLevenshteinDistanceRecCache.restype = ctypes.c_int

def _printMatrix(matrix, n, m):
    print("Матрица расстояний:")
    for i in range(n + 1):
        for j in range(m + 1):
            print(matrix[i][j], end=" ")  
        print()  

def LevenshteinDistance(str1, str2):
    lenStr1, lenStr2 = len(str1), len(str2)
    ptrStr1, ptrStr2 = ctypes.c_wchar_p(str1), ctypes.c_wchar_p(str2)

    matrix = (ctypes.POINTER(ctypes.c_int) * (lenStr1 + 1))()
    for i in range(lenStr1 + 1):
        matrix[i] = (ctypes.c_int * (lenStr2 + 1))()
    result = lib.LevenshteinDistance(ptrStr1, ptrStr2, matrix)

    _printMatrix(matrix, lenStr1, lenStr2)

    return result

def DamerauLevenshteinDistance(str1, str2):
    lenStr1, lenStr2 = len(str1), len(str2)
    ptrStr1, ptrStr2 = ctypes.c_wchar_p(str1), ctypes.c_wchar_p(str2)

    matrix = (ctypes.POINTER(ctypes.c_int) * (lenStr1 + 1))()
    for i in range(lenStr1 + 1):
        matrix[i] = (ctypes.c_int * (lenStr2 + 1))()
    result = lib.DamerauLevenshteinDistance(ptrStr1, ptrStr2, matrix)

    _printMatrix(matrix, lenStr1, lenStr2)

    return result

def DamerauLevenshteinDistanceRecursive(str1, str2):
    lenStr1, lenStr2 = len(str1), len(str2)
    ptrStr1, ptrStr2 = ctypes.c_wchar_p(str1), ctypes.c_wchar_p(str2)

    return lib.DamerauLevenshteinDistanceRecursive(ptrStr1, lenStr1, ptrStr2, lenStr2)

def DamerauLevenshteinDistanceRecCache(str1, str2):
    lenStr1, lenStr2 = len(str1), len(str2)
    ptrStr1, ptrStr2 = ctypes.c_wchar_p(str1), ctypes.c_wchar_p(str2)

    matrix = (ctypes.POINTER(ctypes.c_int) * (lenStr1 + 1))()
    for i in range(lenStr1 + 1):
        matrix[i] = (ctypes.c_int * (lenStr2 + 1))()
        for j in range(lenStr2 + 1):
            matrix[i][j] = ctypes.c_int(-1)

    return lib.DamerauLevenshteinDistanceRecCache(ptrStr1, lenStr1, ptrStr2, lenStr2, matrix)

def analyze():
    lib.DistancesMethodTimeAnalyze()

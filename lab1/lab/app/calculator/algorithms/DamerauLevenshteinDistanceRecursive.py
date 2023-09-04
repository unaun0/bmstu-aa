def DamerauLevenshteinDistanceRecursive(str1, str2):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)

    cost = 0 if str1[-1] == str2[-1] else 1

    deleteCost = DamerauLevenshteinDistanceRecursive(str1[:-1], str2) + 1
    insertCost = DamerauLevenshteinDistanceRecursive(str1, str2[:-1]) + 1
    replaceCost = DamerauLevenshteinDistanceRecursive(str1[:-1], str2[:-1]) + cost

    transposeCost = float('inf')
    if len(str1) > 1 and len(str2) > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        transposeCost = DamerauLevenshteinDistanceRecursive(str1[:-2], str2[:-2]) + cost

    return min(deleteCost, insertCost, replaceCost, transposeCost)


    
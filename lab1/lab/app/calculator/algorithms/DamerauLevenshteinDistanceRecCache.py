def DamerauLevenshteinDistanceRecCache(str1, str2, memo = {}):
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    if (str1, str2) in memo:
        return memo[(str1, str2)]

    cost = 0 if str1[-1] == str2[-1] else 1

    deleteCost = DamerauLevenshteinDistanceRecCache(str1[:-1], str2, memo) + 1
    insertCost = DamerauLevenshteinDistanceRecCache(str1, str2[:-1], memo) + 1
    replaceCost = DamerauLevenshteinDistanceRecCache(str1[:-1], str2[:-1], memo) + cost

    transposeCost = float('inf')
    if len(str1) > 1 and len(str2) > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
        transposeCost = DamerauLevenshteinDistanceRecCache(str1[:-2], str2[:-2], memo) + cost

    minDistance = min(deleteCost, insertCost, replaceCost, transposeCost)
    memo[(str1, str2)] = minDistance

    return minDistance
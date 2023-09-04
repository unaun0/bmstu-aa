def DamerauLevenshteinDistance(str1, str2, matrix):
    lenStr1 = len(str1)
    lenStr2 = len(str2)

    for i in range(lenStr1 + 1):
        matrix[i][0] = i
    for j in range(lenStr2 + 1):
        matrix[0][j] = j

    for i in range(1, lenStr1 + 1):
        for j in range(1, lenStr2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,       # Удаление
                matrix[i][j - 1] + 1,       # Вставка
                matrix[i - 1][j - 1] + cost # Замена
            )
            if i > 1 and j > 1 \
                and str1[i - 1] == str2[j - 2] \
                and str1[i - 2] == str2[j - 1]:
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + cost)
                    
    return matrix[lenStr1][lenStr2]

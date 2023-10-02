#include "Distances.h"
#include <wchar.h>
#include <time.h>

#define METHOD_COUNT 4
#define SIZE_COUNT 7
#define ITERATION_COUNT 100

static int min(int num, ...);
static wchar_t* generateRandomWord(size_t length);
static void printTableTime(int **matrix, size_t rows, size_t columns);
static int** createMatrix(size_t rows, size_t columns);
static void fillMatrix(int **matrix, size_t rows, size_t columns, int value);
static void freeMatrix(int **matrix, size_t rows);

int LevenshteinDistance(const wchar_t *str1, const wchar_t *str2, int **matrix) {
    int lenStr1 = wcslen(str1);
    int lenStr2 = wcslen(str2);

    for (int i = 0; i <= lenStr1; i++) {
        matrix[i][0] = i;
    }
    for (int j = 0; j <= lenStr2; j++) {
        matrix[0][j] = j;
    }

    for (int i = 1; i <= lenStr1; i++) {
        for (int j = 1; j <= lenStr2; j++) {
            int cost = (str1[i - 1] == str2[j - 1]) ? 0 : 1;
            matrix[i][j] = min(
                3,
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            );
        }
    }

    return matrix[lenStr1][lenStr2];
}

int DamerauLevenshteinDistance(const wchar_t *str1, const wchar_t *str2, int **matrix) {
    int lenStr1 = wcslen(str1);
    int lenStr2 = wcslen(str2);

    for (int i = 0; i <= lenStr1; i++) {
        matrix[i][0] = i;
    }
    for (int j = 0; j <= lenStr2; j++) {
        matrix[0][j] = j;
    }

    for (int i = 1; i <= lenStr1; i++) {
        for (int j = 1; j <= lenStr2; j++) {
            int cost = (str1[i - 1] == str2[j - 1]) ? 0 : 1;
            matrix[i][j] = min(
                3,
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            );
            if (i > 1 && j > 1 && str1[i - 1] == str2[j - 2] && str1[i - 2] == str2[j - 1]) {
                matrix[i][j] = min(
                    2, 
                    matrix[i][j], 
                    matrix[i - 2][j - 2] + cost);
            }
        }
    }
    return matrix[lenStr1][lenStr2];
}

int DamerauLevenshteinDistanceRecursive(const wchar_t *str1, int lenStr1, const wchar_t *str2, int lenStr2) {
    if (lenStr1 == 0) {
        return lenStr2;
    }
    if (lenStr2 == 0) {
        return lenStr1;
    }
    //wprintf(L"%ls - %d\n%ls - %d\n---\n", str1, lenStr1, str2, lenStr2);
    int cost = (str1[lenStr1 - 1] == str2[lenStr2 - 1]) ? 0 : 1;

    int deleteCost = DamerauLevenshteinDistanceRecursive(str1, lenStr1 - 1, str2, lenStr2) + 1;
    int insertCost = DamerauLevenshteinDistanceRecursive(str1, lenStr1, str2, lenStr2 - 1) + 1;
    int replaceCost = DamerauLevenshteinDistanceRecursive(str1, lenStr1 - 1, str2, lenStr2 - 1) + cost;
    int transposeCost = INT_MAX;
    if (lenStr1 > 1 && lenStr2 > 1 && str1[lenStr1 - 1] == str2[lenStr2 - 2] && str1[lenStr1 - 2] == str2[lenStr2 - 1]) {
        transposeCost = DamerauLevenshteinDistanceRecursive(str1, lenStr1 - 2, str2, lenStr2 - 2) + cost;
    }

    int minDistance = min(
        4, 
        deleteCost, 
        insertCost, 
        replaceCost, 
        transposeCost);
    return minDistance;
}

int DamerauLevenshteinDistanceRecCache(const wchar_t *str1, int lenStr1, const wchar_t *str2, int lenStr2, int **memo) {
    if (lenStr1 == 0) {
        return lenStr2;
    }
    if (lenStr2 == 0) {
        return lenStr1;
    }
    if (memo[lenStr1][lenStr2] != -1) {
        return memo[lenStr1][lenStr2];
    }

    int cost = (str1[lenStr1 - 1] == str2[lenStr2 - 1]) ? 0 : 1;

    int deleteCost = DamerauLevenshteinDistanceRecCache(str1, lenStr1 - 1, str2, lenStr2, memo) + 1;
    int insertCost = DamerauLevenshteinDistanceRecCache(str1, lenStr1, str2, lenStr2 - 1, memo) + 1;
    int replaceCost = DamerauLevenshteinDistanceRecCache(str1, lenStr1 - 1, str2, lenStr2 - 1, memo) + cost;

    int transposeCost = INT_MAX;
    if (lenStr1 > 1 && lenStr2 > 1 && str1[lenStr1 - 1] == str2[lenStr2 - 2] && str1[lenStr1 - 2] == str2[lenStr2 - 1]) {
        transposeCost = DamerauLevenshteinDistanceRecCache(str1, lenStr1 - 2, str2, lenStr2 - 2, memo) + cost;
    }

    int minDistance = min(4, deleteCost, insertCost, replaceCost, transposeCost);

    memo[lenStr1][lenStr2] = minDistance;

    return minDistance;
}

static int min(int num, ...) {
    va_list args;
    va_start(args, num);

    int minVal = va_arg(args, int);

    for (int i = 1; i < num; i++) {
        int current = va_arg(args, int);
        if (current < minVal) {
            minVal = current;
        }
    }

    va_end(args);

    return minVal;
}

void DistancesMethodTimeAnalyze() {

    clock_t startTime, endTime, cpu_time;

    int **timeAnalyze = createMatrix(METHOD_COUNT, SIZE_COUNT);
    int sizes[SIZE_COUNT] = {5, 10, 20, 40, 80, 160, 320};
    int rc = 1;

    for (size_t sID = 0; rc && sID < SIZE_COUNT; ++sID) {
        int **matrix = createMatrix(sizes[sID] + 1, sizes[sID] + 1);
        for (size_t mID = 0; rc && mID < METHOD_COUNT; ++mID) {
            timeAnalyze[mID][sID] = 0.0;
            cpu_time = 0;
            for (size_t it = 0;  rc && it < ITERATION_COUNT; ++it) {
                wchar_t* str1 = generateRandomWord(sizes[sID]); 
                if (str1 == NULL){
                    rc = 0;
                    break;
                }
                wchar_t* str2 = generateRandomWord(sizes[sID]);
                if (str2 == NULL) {
                    rc = 0;
                    free(str1);
                    break;
                }
                if (mID == 0) {
                    fillMatrix(matrix, sizes[sID] + 1,sizes[sID] + 1, 0);
                    startTime = clock();
                    LevenshteinDistance(str1, str2, matrix);
                    endTime = clock(); 
                }
                else if (mID == 1) {
                    fillMatrix(matrix, sizes[sID] + 1,sizes[sID] + 1, 0);
                    startTime = clock();
                    DamerauLevenshteinDistance(str1, str2, matrix);
                    endTime = clock(); 
                }
                else if (mID == 2) {
                    if (sID < 2) {
                        startTime = clock(); 
                        DamerauLevenshteinDistanceRecursive(str1, sizes[sID], str2, sizes[sID]);
                        endTime = clock(); 
                    }
                    else {
                        startTime = 0;
                        endTime = 0;
                    }
                }
                else {
                    fillMatrix(matrix, sizes[sID] + 1, sizes[sID] + 1, -1);
                    startTime = clock();
                    DamerauLevenshteinDistanceRecCache(str1, sizes[sID], str2, sizes[sID], matrix);
                    endTime = clock(); 
                }
                cpu_time += endTime - startTime;
                //free(str1);
                //free(str2);
            }
            timeAnalyze[mID][sID] = (int)(cpu_time / ITERATION_COUNT);
        }
        //freeMatrix(matrix, sizes[sID] + 1);
    }
    printTableTime(timeAnalyze, METHOD_COUNT, SIZE_COUNT);
    //freeMatrix(timeAnalyze, SIZE_COUNT);
}

static void printTableTime(int **matrix, size_t rows, size_t columns) {
    printf("%70s", "----- Анализ по времени -----\n");
    printf("%3s", "t/s |");
    int sizes[SIZE_COUNT] = {5, 10, 20, 40, 80, 160, 320};
    for (size_t i = 0; i < SIZE_COUNT; ++i)
        printf("%10d ", sizes[i]);
    printf("\n");
    for (size_t i = 0; i < SIZE_COUNT; ++i)
        printf("------------");
    printf("\n");
    char* methods[15] = { "Лев", "ДЛИ", "ДЛР", "ДЛM" };
    for (size_t i = 0; i < rows; ++i) {
        printf("%3s |", methods[i]);
        for (size_t j = 0; j < columns; ++j) {
            if (i == 2 && j > 1)
                printf("%10s ", "-");
            else
                printf("%10d ", matrix[i][j]);
        }
        printf("\n");
    }
}

static wchar_t* generateRandomWord(size_t length) {
    wchar_t* word = (wchar_t *)malloc((length + 1) * sizeof(wchar_t));
    if (word == NULL)
        return NULL;

    const wchar_t characters[] = L"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (size_t i = 0; i < length; ++i) {
        size_t randID = rand() % (wcslen(characters));
        word[i] = characters[randID];
    }
    word[length] = L'\0'; 

    return word;
}

static int** createMatrix(size_t rows, size_t columns) {
    int **matrix = (int **)malloc(rows * sizeof(int *));
    if (matrix == NULL) {
        return NULL; 
    }

    for (size_t i = 0; i < rows; ++i) {
        matrix[i] = (int *)malloc(columns * sizeof(int));
        if (matrix[i] == NULL) {
            for (size_t  j = 0; j < i; ++j) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }

    return matrix;
}

static void fillMatrix(int **matrix, size_t rows, size_t columns, int value) {
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < columns; ++j) {
            matrix[i][j] = value;
        }
    }
}

static void freeMatrix(int **matrix, size_t rows) {
    for (size_t i = 0; i < rows; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}
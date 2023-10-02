#ifndef DISTANCES_H
#define DISTANCES_H

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <stdarg.h>
#include <wchar.h>

int LevenshteinDistance(const wchar_t *str1, const wchar_t *str2, int **matrix);
int DamerauLevenshteinDistance(const wchar_t *str1, const wchar_t *str2, int **matrix);
int DamerauLevenshteinDistanceRecursive(const wchar_t *str1, int lenStr1, const wchar_t *str2, int lenStr2);
int DamerauLevenshteinDistanceRecCache(const wchar_t *str1, int lenStr1, const wchar_t *str2, int lenStr2, int **memo);
void DistancesMethodTimeAnalyze();

#endif // DISTANCES_H

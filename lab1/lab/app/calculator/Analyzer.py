import timeit
import random
import matplotlib.pyplot as plt
from .algorithms.LevenshteinDistance import LevenshteinDistance
from .algorithms.DamerauLevenshteinDistanceRecCache import DamerauLevenshteinDistanceRecCache
from .algorithms.DamerauLevenshteinDistanceRecursive import DamerauLevenshteinDistanceRecursive
from .algorithms.DamerauLevenshteinDistance import DamerauLevenshteinDistance

class Analyzer:
    def generateRandomUnicodeString(self, length):
        randomString = [chr(random.randint(0x0400, 0x04FF)) for _ in range(length)]
        return ''.join(randomString)
    
    def calculateAlgTime(self, countAlgs, sizes, iterations):
        algTimes = []
        for i in range(countAlgs):
            averageTimes = [0] * len(sizes)
            for j in range(len(averageTimes)):
                workTime = 0
                matrix = self.matrix = [[0 for _ in range(sizes[j] + 1)] for _ in range(sizes[j] + 1)]
                for _ in range(iterations):
                    str1 = self.generateRandomUnicodeString(sizes[j])
                    str2 = self.generateRandomUnicodeString(sizes[j])
                    memo = {}
                    if i == 0:
                        workTime += (timeit.timeit(lambda: LevenshteinDistance(str1, str2, matrix), number=1)) * 1e9
                    elif i == 1:
                        workTime += (timeit.timeit(lambda: DamerauLevenshteinDistance(str1, str2, matrix), number=1)) * 1e9
                    elif i == 2:
                        workTime += (timeit.timeit(lambda:  DamerauLevenshteinDistanceRecursive(str1, str2), number=1)) * 1e9
                    else:
                        workTime += (timeit.timeit(lambda: DamerauLevenshteinDistanceRecCache(str1, str2, memo), number=1)) * 1e9
                averageTimes[j] = (workTime / 100)
            algTimes.append(averageTimes)
        return algTimes

    def timeAnalyse(self):
        algs = ["Левенштейн", "Дамерау-Левенштейн", "Дамерау-Левенштейн рекурсивный", "Дамерау-Левенштейн рекурсивный c кэшем"] 
        sizes = [0, 50, 100, 150, 200, 250, 300]
        iterations = 10
        algTimes = self.calculateAlgTime(len(algs), sizes, iterations)
        self.buildGraph(algs, algTimes, sizes)

    
    def buildGraph(self, titles, times, sizes):
        plt.figure(figsize=(10, 6), num="Анализ алгоритмов по времени")
        markers = ["o", "s", "D", "^", "v", "*", "+", "x", ".", ",", "1", "2", "3", "4"]

        for i, title in enumerate(titles):
            plt.plot(sizes, times[i], marker= markers[i % len(markers)], label=title)

        plt.xlabel("Размер строки")
        plt.ylabel("Время выполнения (наносекунды)")
        plt.title("Время выполнения алгоритмов в зависимости от размера строки")
        plt.legend()
        plt.grid(True)

        plt.show()

        plt.close()



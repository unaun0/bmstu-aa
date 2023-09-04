from simple_term_menu import TerminalMenu
from art import tprint 
from .calculator.StringDistanceCalculator import StringDistanceCalculator
from .calculator.Analyzer import Analyzer

class App:
    def __init__(self):
        self.calculator = StringDistanceCalculator('', '')
        self.analyzer = Analyzer()
        self.makemenu()
    
    def mainloop(self):
        self.title()
        self.info()
        while True:
            cmd = self.showmenu()
            self.controller(cmd)

    def controller(self, cmd):
        if cmd == 0:
            self.strinput()
        elif cmd == 1:
            self.strprint()
        elif cmd == 2:
            print("\nАлгоритм Левенштейна")
            self.algLD()
        elif cmd == 3:
            print("\nАлгоритм Дамерау-Левенштейна")
            self.algDLD()
        elif cmd == 4:
            print("\nАлгоритм рекурсивный Дамерау-Левенштейна")
            self.algDLDR()
        elif cmd == 5:
            print("\nАлгоритм рекурсивный с кэшем Дамерау-Левенштейна")
            self.algDLDRC()
        elif cmd == 6:
            print("\nВыполняется анализ алгоритмов...")
            self.analyzer.timeAnalyse()
            self.appexit()
        elif cmd == 7:
            self.appexit()
        else:
            print("Ошибка. Некорректная команда.")
        print('')
        return 1
    
    def strinput(self):
        try:
            str1 = str(input('Введите первую строку: '))
            str2 = str(input('Введите вторую строку: '))
        except:
            print("Ошибка. Некорректный ввод строки.\n")
            return
        print('')
        self.calculator = StringDistanceCalculator(str1, str2)
    
    def algLD(self):
        self.printResult(self.calculator.CalculateDistance(False)) 
        print("Матрица расстояний: ")
        self.calculator.printMatrix()
    
    def algDLD(self):
        self.printResult(self.calculator.CalculateDistance(True))
        print("Матрица расстояний: ")
        self.calculator.printMatrix()

    def algDLDR(self):
        self.printResult(self.calculator.CalculateDistanceRecursive(False))

    def algDLDRC(self):
        self.printResult(self.calculator.CalculateDistanceRecursive(True))
    
    def strprint(self):
        self.calculator.info()

    def printResult(self, result):
        print(f"Результат: {result}")

    def title(self):
        tprint(f"StringDistanceCounter")

    def info(self):
        print("Автор: Цховребова Яна Роландовна |", "Группа: ИУ7-54Б |", "Лабораторная работа №1\n")
    
    def showmenu(self):
        return self.menu.show()

    def makemenu(self):
        self.menu = TerminalMenu(['1. Ввести две строки',
                                  '2. Вывести строки',
                                  '3. Вычислить расстояние (алгоритм Левенштейна)', 
                                  '4. Вычислить расстояние (алгоритм Дамерау-Левенштейна)', 
                                  '5. Вычислить расстояние (рекурсивный алгоритм Дамерау-Левенштейна)',
                                  '6. Вычислить расстояние (рекурсивный с кэшем алгоритм Дамерау-Левенштейна)',
                                  '7. Анализ алгоритмов',
                                  '0. Выход'
                                  ])
    
    def appexit(self):
        print("Завершение программы...")
        exit()
    
        
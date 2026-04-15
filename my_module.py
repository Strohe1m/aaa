class MyModule:
    
    def greet(self, name):
        """
        Выводит приветствие пользователю.

        :param name: имя пользователя
        :return: строка приветствия
        :example:
        >>> greet("Alice")
        'Привет, Alice!'
        """
        return f"Привет, {name}!"

    def add(self, a, b):
        """
        Складывает два числа.

        :param a: первое число
        :param b: второе число
        :return: сумма чисел
        :example:
        >>> add(2, 3)
        5
        """
        return a + b

    def factorial(self, n):
        """
        Вычисляет факториал числа.

        :param n: неотрицательное целое число
        :return: факториал числа
        :example:
        >>> factorial(5)
        120
        """
        if n < 0:
            raise ValueError("Факториал не определен для отрицательных чисел.")
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    

if __name__ == "__main__":
    # Пример использования функций
    module = MyModule()
    print(module.greet("Alice"))
    print(module.add(2, 3))
    print(module.factorial(5))


# Это библиотечный пример тестирования стандартных функций для строки
import unittest
from fib import fibonacci

# Создается класс. классу соответсвует набор тестовых сценариев (TestCase)(тесируемые кейсы)
class TestStringMethods(unittest.TestCase):  

    def test_simple_fibonacci(self):
        for param, result in [(0, 0), (1, 1), (2, 1), (5, 5)]:
            self.assertEqual(fibonacci(param), result) 
    
    def test_stress_fibonacci(self):
        self.assertEqual(fibonacci(9999), fibonacci(9998) + fibonacci(9997)) 
        with self.assertRaises(ValueError):
             fibonacci(10000)
    
    def test_negative_fibonacci(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-100)
            
    def test_wrong_types_fibonacci(self):
        with self.assertRaises(TypeError):
            fibonacci('Hello')
        with self.assertRaises(TypeError):
            fibonacci(3.14)        
        

# Тест-кейс 1 (Стандратный пример)
#     def test_upper(self):  # Важно что функции начинаются с "test_"
#         self.assertEqual('foo'.upper(), 'FOO')  # Функция assertEqual предназначена для сравнения двух вещей(равны или не равны)

#     def foo(): # Для примера такая функция не вызовется из-за отсутсвия test_
#         pass

# # Тест-кейс 2
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())  # Проверяется на правду 
#         self.assertFalse('Foo'.isupper())  # Проверяется на не правду

# # Если бы использовался стандартный метод assert - то было бы жесткое падение программы.

# # Тест-кейс 3 
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):  # Будет вызвано исключение методом assertRaises
#             s.split(2)
            

if __name__ == '__main__':
    unittest.main()  # Запускается main из библиотеки unittest
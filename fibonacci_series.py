
class iCalculator(object):

    def print_fib(self):
        return self.__fibonacci_serie(10)

    def __fibonacci_serie(self, number):

        if number > 2:
            return self.__fibonacci_serie(number-2) + self.__fibonacci_serie(number-1) 
        else:
            return 1


class babyCalculator(iCalculator):
    def sum(self, x, y):
        return x + y
    
    def substract(self, x, y):
        return x - y

    def print_fib(self):
        return self._iCalculator__fibonacci_serie(20)


calc = iCalculator()
print('fibonacci for 10: {}'.format(calc.print_fib()))

r = babyCalculator()
print('fibonacci for 20: {}'.format(r.print_fib()))
print('1 + 3: {}'.format(r.sum(1,3)))
print('1 - 3: {}'.format(r.substract(1,3)))
        
        
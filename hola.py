def main():
   print("hola")

def two_numbers(x, y):
    """ This is part of the documentation of this function"""
    print("Result x plus b = {}",str(x+y))
    
def foo(param1, param2):
    """ This is another function with (param1, param2) as parameters """
    return (param1-param2)

#resultado = dict()
def letter_counter(parameter_word):
    """ Taking a word as a parameter, this function counts the repetition of each letter"""
    resultado = dict()
    for letter_in in parameter_word:
        if letter_in in resultado:
            resultado[letter_in] = resultado[letter_in] + 1
        else:
            resultado[letter_in] = 1
    return resultado


def factor(num):
    """ Givin a number it returns the number num factorial of num"""
    if num == 1:
        return 1
    else:
        return num * factor(num-1)
		
def fibo(num):
    """ It returns the num ns Fibonacci number """
    if num < 3:
        if num == 1:
            return 1
        else:
            return 2
    else:
        return fibo(num-1) + fibo(num-2)
    
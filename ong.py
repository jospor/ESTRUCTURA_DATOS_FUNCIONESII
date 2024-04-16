
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def productoria(lst):
    result = 1
    for number in lst:
        result *= number
    return result

def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact_' in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif 'prod_' in key:
            print(f"La productoria de {value} es {productoria(value)}")

calcular(fact_1=5, prod_1=[3,6,4,2,8], fact_2=6)

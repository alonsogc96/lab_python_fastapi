def functionA(functionB):

    def functionC(*args):
        print("1. Antes de ejecutar la función a decorar")
        resultado = functionB(*args)
        print(resultado)
        print("2. Esto sucede luego de ejecutar la función a decorar")
    return functionC

@functionA
def suma(a,  b):
    return a + b

suma(30, 100)
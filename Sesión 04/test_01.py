def functionA(functionB):

    def functionC():
        print("1. Antes de ejecutar la función a decorar")
        functionB()
        print("2. Esto sucede luego de ejecutar la función a decorar")

    return functionC()

@functionA
def saludo():
    print("Hola Pythonistats!!")


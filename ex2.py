def verificar_valores(a, b):
    if a > b:
        return f"{a} é maior que {b}"
    elif a < b:
        return f"{a} é menor que {b}"
    else:
        return f"{a} é igual a {b}"
    
resultado = verificar_valores(5, 10)
print(resultado)

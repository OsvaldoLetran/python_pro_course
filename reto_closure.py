def tabla_multiplicar(x: int) -> int:
    def multiplicaciones(n: int) -> int:
        my_tabla = {i: i*x for i in range(0,n)}
        return my_tabla
    return multiplicaciones


def run():
    tabla_del_5 = tabla_multiplicar(5)
    tabla_del_5_hasta_330 = tabla_del_5(330)
    cinco_multiplicado_por = tabla_del_5_hasta_330
    print(cinco_multiplicado_por[221])
    
if __name__ == "__main__":
    run()
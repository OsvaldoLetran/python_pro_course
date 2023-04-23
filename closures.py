def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        # """assert nos permite verificar que una determinada condicion sea True
        #    de lo contrario lanzara una excepcion"""
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))


if __name__ == '__main__':
    run()
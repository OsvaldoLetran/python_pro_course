def make_division_by(n: int):
    """This closure returns a function that returns
       the division of an x number by n
    """
    def divisioner(x: int):
        return x / n
    return divisioner


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))    # The excpected output is 6


if __name__ == '__main__':
    run()
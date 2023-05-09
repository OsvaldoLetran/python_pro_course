# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 2, 2, 3, "Platzi", "Platzi", True, 4.6, False]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()

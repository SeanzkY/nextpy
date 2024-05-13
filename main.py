from functools import reduce


def check_id_valid(id_number):
    # this helps iteration over the number
    id_number_str = str(id_number)
    # this multiplies by index (if index uneven time by 1 else time by 2 - index start with 0 not 0)
    result_list = (map(lambda x, y: int(x) * (y % 2 + 1), id_number_str, range(9)))
    # this turns numbers that are bigger than 9 to the sum of the digits they have 11 = 1 + 1 - there
    # won't be more than two digit due to the calculation before
    result_list = map(lambda x: x % 10 + int(x / 10) if x > 9 else x, result_list)
    # calculate sum
    result = reduce(lambda x, y: x + y, result_list)
    return result % 40 == 0


class IDIterator:
    MAX_SIZE = 999999999

    def __init__(self, id_number):
        self._id = id_number

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while self._id <= IDIterator.MAX_SIZE and not check_id_valid(self._id):
            self._id += 1
        if self._id >= IDIterator.MAX_SIZE:
            raise StopIteration("out of numbers")
        return self._id


def id_generator(id_num):
    MAX_SIZE = 999999999
    next_id = (x for x in range(id_num + 1, MAX_SIZE + 1) if check_id_valid(x))
    while True:
        result = next(next_id)
        yield result


def main():
    id_input = input("Enter ID: ")
    while not id_input.isnumeric():
        print("number must be numeric")
        id_input = input("Enter ID: ")

    func_input = input("Generator or Iterator? (gen/it)? ")
    while func_input != "gen" and func_input != "it":
        print("must be gen or it")
        func_input = input("Generator or Iterator? (gen/it)? ")

    if func_input == "gen":
        get_next_id = id_generator(int(id_input))
    else:
        get_next_id = iter(IDIterator(int(id_input)))

    try:
        for x in (next(get_next_id) for x in range(10)):
            print(x)
    except StopIteration as e:
        print("out of numbers")
    except RuntimeError as e:
        print("out of numbers")


if __name__ == '__main__':
    main()

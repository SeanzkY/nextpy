from functools import reduce

OUT_OF_RANGE_ID = 999999999
NUMBER_OF_ID_DIGITS = 9
GENERATOR_NAME = "gen"
ITERATOR_NAME = "it"
ASK_USER_FOR_ID = "Enter ID: "
NON_NUMERIC_NUMBER_ENTERED = "number must be numeric"
ASK_USAGE_NAME = "Generator or Iterator? ({}/{})? ".format(GENERATOR_NAME, ITERATOR_NAME)
INVALID_USAGE_NAME_ENTERED = "must be {} or {}".format(GENERATOR_NAME, ITERATOR_NAME)
IDS_AMOUNT_NEEDED = 10
ITERATOR_ERROR_ANNOUNCE = "out of numbers iter"
GENERATOR_ERROR_ANNOUNCE = "out of numbers generator"


def check_id_valid(id_number):
    """
    this function check whether the id is valid or not by using a calculation specified inside the function
    :param id_number: the id itself
    :return: true if it's valid false if not
    :rtype: bool
    """
    # this helps iteration over the number
    id_number_str = str(id_number)
    # this multiplies by index (if index uneven time by 1 else time by 2 - index start with 0 not 0)
    result_list = (map(lambda x, y: int(x) * (y % 2 + 1), id_number_str, range(NUMBER_OF_ID_DIGITS)))
    # this turns numbers that are bigger than 9 to the sum of the digits they have 11 = 1 + 1 - there
    # won't be more than two digit due to the calculation before
    result_list = map(lambda x: x % 10 + int(x / 10) if x > 9 else x, result_list)
    # calculate sum
    result = reduce(lambda x, y: x + y, result_list)
    return result % 40 == 0


class IDIterator:
    MAX_SIZE = OUT_OF_RANGE_ID
    """
    class used to iterate over the next valid ids in range from a certain id
    """

    def __init__(self, id_number):
        """
        Initialize object with id
        :param id_number: identification to use
        :type id_number: int
        """
        self._id = id_number

    def __iter__(self):
        """
        the iter object is for iterating over the identification - get the next valid identification in up to MAX_SIZE
        :return the iterator
        :rtype IDIterator
        """
        return self

    def __next__(self):
        """
        the implementation of next in iter
        :return: next id number
        :type int
        :raise StopIteration: raise an exception when next number is not valid anymore (can't create next id)
        """
        self._id += 1
        while self._id <= IDIterator.MAX_SIZE and not check_id_valid(self._id):
            self._id += 1
        if self._id >= IDIterator.MAX_SIZE:
            raise StopIteration("Numbers Out of range")
        return self._id


def id_generator(id_num):
    """
    Generator of IDs
    :param id_num: id
    :return: generate the next legal ids in range
    :rtype: int
    :raise RunTimeError: raises an exception when can't generate more numbers
    """
    MAX_SIZE = OUT_OF_RANGE_ID
    # here we create a generator that will have the everytime the next valid id - this line does all the task by
    # itself already and the rest is just because we need it in a function with yield
    next_id = (x for x in range(id_num + 1, MAX_SIZE) if check_id_valid(x))
    while True:
        result = next(next_id)
        yield result


def main():
    id_input = input(ASK_USER_FOR_ID)
    while not id_input.isnumeric():
        print(NON_NUMERIC_NUMBER_ENTERED)
        id_input = input(ASK_USER_FOR_ID)

    func_input = input(ASK_USAGE_NAME)
    while func_input != GENERATOR_NAME and func_input != ITERATOR_NAME:
        print(INVALID_USAGE_NAME_ENTERED)
        func_input = input(ASK_USAGE_NAME)

    if func_input == GENERATOR_NAME:
        get_next_id = id_generator(int(id_input))
    else:
        get_next_id = iter(IDIterator(int(id_input)))

    try:
        # we  want to print all the print all numbers that are not out of range - we generate a specific amount of ids
        [print(next(get_next_id)) for _ in range(IDS_AMOUNT_NEEDED)]
    except StopIteration as e:
        print(ITERATOR_ERROR_ANNOUNCE + "\nerror:\n" + e.__str__())
    except RuntimeError as e:
        print(GENERATOR_ERROR_ANNOUNCE + "\nerror:\n" + e.__str__())


if __name__ == '__main__':
    main()

from functools import reduce

FILE_NAME = r"C:\Users\seanr\Downloads\names.txt"
SIZE_FILE_NAME = r"C:\Users\seanr\Downloads\namesSize.txt"
SIZE_REQUEST_MESSAGE = "please enter size "


def main():
    # also possible to use max, sum to solve
    with open(FILE_NAME, "r") as file:
        # turn the file to list that contain only the words and ignore the empty word
        names_list = [x for x in file.read().split("\n") if len(x) > 0]
        # 1):
        # take the maximum length val every time and then go to the next 2
        print(reduce(lambda x, y: x if len(x) > len(y) else y, names_list, ""))
        # 2):
        # calculates sum of words letters - add for each time the currents sum and the len of the word -
        # start current sum with 0 - print result
        print(reduce(lambda x, y: x + len(y), names_list, 0))
        # 3):
        # calculates min size by checking if len word is smaller than current min and if it is putting
        # len word in current min, start current min with len of the first word
        min_size = reduce(lambda x, y: x if x < len(y) else len(y), names_list, len(names_list[0]))
        # take the words with the len we calculated (min), separate them with newlines and print
        print("\n".join(list(filter(lambda x: len(x) == min_size, names_list))))
        # 4):
        with open(SIZE_FILE_NAME, "w") as file_write:
            # write the lengths of words in the file before separated by new lines
            file_write.write("\n".join([str(len(x)) for x in names_list]))
        # 5):
        names_size = input(SIZE_REQUEST_MESSAGE)
        if names_size.isnumeric():
            # print all words with the same length as names_size separated by \n in the file we read
            print("\n".join([x for x in names_list if len(x) == int(names_size)]))


if __name__ == '__main__':
    main()

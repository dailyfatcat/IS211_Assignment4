#import statements
import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    '''Insertion Sort from book'''
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
    a_list[position] = current_value
    return a_list


def shell_sort(a_list):
    '''Shell Sort from book'''
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return a_list


def gap_insertion_sort(a_list, start, gap):
    '''Subfunction for Shell Sort from book'''
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
    while position >= gap and a_list[position - gap] > current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap
    a_list[position] = current_value


def python_sort(a_list):
    '''Wrapper function calls sort() on the input list'''
    return sorted(a_list)


def avg_time(sortFunc, Comment):
    random.seed(100)

    list_size = [500, 100, 5000]
    total_time = 0
    for list_size in list_size:
        for i in range(100):
            start = time.time()
            sortFunc(get_me_random_list(list_size))
            end = time.time()
            sort_time = end - start
            total_time += sort_time

        avg_time = total_time / 100
        print(f"{Comment} took {avg_time:10.7f} seconds to run on average, for list size {list_size}")


if __name__ == "__main__":
    """Main entry point"""
    avg_time(insertion_sort, "Insertion Sort")
    avg_time(python_sort, "Python Sort")
    avg_time(shell_sort, "Shell Sort")



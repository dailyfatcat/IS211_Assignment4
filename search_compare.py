import argparse
# other imports go here

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


def sequential_search(a_list, item):
    ''''Sequential search from book'''
    pos = 0
    found = False

    #Calculate time
    start = time.time()

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    #Calculate time
    end = time.time()
    sort_time = end - start

    return(found, sort_time)


def ordered_sequential_search(a_list, item):
    '''Ordered Sequential Search from Book'''
    pos = 0
    found = False
    stop = False

    #Calculate time
    start = time.time()

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    #Calculate time
    end = time.time()
    sort_time = end - start

    return(found, sort_time)


def binary_search_iterative(a_list,item):
    '''Binary Search - Iterative from book'''
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    #Calculate time
    start = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    #Calculate time
    end = time.time()
    sort_time = end - start
    return(found, sort_time)


def binary_search_recursive(a_list,item):
    ''''Binary Search - Recursive From Book'''
    #Calculate time
    start = time.time()

    if len(a_list) == 0:
        # Calculate time
        end = time.time()
        sort_time = end - start
        return(False, sort_time)
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        # Calculate time
        end = time.time()
        sort_time = end - start
        return(True, sort_time)
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)


if __name__ == "__main__":
    """Main entry point"""
    random.seed(100)
    searches = {"Sequential Search": sequential_search, "Ordered Sequential Search": ordered_sequential_search,
                "Binary Search Iterative": binary_search_iterative, "Binary search recursive": binary_search_recursive}

    list_size = [500, 1000, 5000]

    for search in searches:
        for lists in list_size:
            total_time = 0
            for i in range(100):
                sorted_list = sorted(get_me_random_list(lists))
                results = searches[search](sorted_list, 99999999)
                total_time += results[1]
            avg_time = total_time/100
            print(f"List Size:{lists}: {search} took {avg_time:10.7f} seconds to run on average")

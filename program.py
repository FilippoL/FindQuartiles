def run_program():
    print("Type the list of number you want to find Qaurtiles and Median of, \nAfter each number press return, \nWhen you want to exit type 'quit': \n\n ")
    nums = []
    collect_values(nums)
    print("The list has " + str(nums.__len__()) + " elements.\n\n")

    nums.sort()
    print("The sorted list is :", nums)

    median = find_median(nums)
    print("\n\nThe median is : " + str(median) + "\n")

    median_upper_half, median_lower_half = find_quartiles(nums)
    print("\n\nThe first quartile is : " + str(median_upper_half) + "\n")
    print("\n\nThe third quartile is : " + str(median_lower_half) + "\n")

def collect_values(_list):
    m_input = input(">")
    while m_input != "quit":
        if m_input.isnumeric():
            _list.append(float(m_input))
            m_input = input(">")
        else:
            m_input = input("Sorry value not recognised \n>")

def find_median(_list):
    if _list.__len__()%2 == 0:
        return (_list[int(_list.__len__()/2)] + _list[int(_list.__len__()/2 - 1)])/2
    else:
        return _list[int((_list.__len__() / 2) + 0.5) - 1]

def find_quartiles(_list):
    if _list.__len__()%2 == 0:
        lower_half = _list[:int((_list.__len__()/2))]
        print("\nLower half is : ", lower_half)
        upper_half = _list[int((_list.__len__()/2)):]
        print("\nUpper half is : ", upper_half)
    else:
        lower_half = _list[:int((_list.__len__()/2) - 0.5)]
        print("\nLower half is : ", lower_half)
        upper_half = _list[int((_list.__len__()/2) + 0.5):]
        print("\nUpper half is : ", upper_half)

    return [find_median(lower_half), find_median(upper_half)]

def main():
    initialise()
    run_program()


def initialise():
    print("#####################################")
    print("######### Find Quartiles ############")
    print("#####################################")



if __name__ == "__main__":
    main()
arr = ["Paul", "John", "Ringo", "George"]


def convert_list(list):
    my_obj = {}

    for item in list:
        my_obj[list.index(item)] = item

    print(my_obj)

convert_list(arr)
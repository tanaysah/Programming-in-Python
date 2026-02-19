def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

my_list = [10, 20, 30]
modify_list(my_list)

print("Outside function:", my_list)

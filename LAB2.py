main_list = [8, 21, 6, 843, 5, 34, 89, 777, 45, 2,
             "apple", "pear", "banana", "kiwi", "cherry",
             "papaya", "mandarine", "pineapple", "watermelon", "melon"]
integer_list = sorted([x for x in main_list if isinstance(x, int)])
string_list = sorted([x for x in main_list if isinstance(x, str)])
sorted_list = integer_list + string_list
paired_list = [x for x in integer_list if x % 2 == 0]
caps_list = [x.upper() for x in string_list]
print("Головний список:", main_list)
print("Відсортований список:", sorted_list)
print("Парні числа:", paired_list)
print("CAPS:", caps_list)
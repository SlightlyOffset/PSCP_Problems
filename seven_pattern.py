mod_list = []
divide_list = []
for i in range (1, 500000000):
    mod_list.append(i%7)
    divide_list.append((i % 7) // 2)
    
print(mod_list)
print(divide_list)
print(max(mod_list))
print(max(divide_list))
# Recurring pattern 7, 9, 3, 1
# Recurring pattern 0 - 6 (max 6)
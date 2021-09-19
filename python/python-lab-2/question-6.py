# Write a Python program to sort a dictionary by key.
# 	color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
color_dict = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
color_dict_sorted = {}
color_list = list(color_dict)
color_list.sort()
for x in color_list:
    color_dict_sorted[x] = color_dict[x]
print("Given dictionary: ", color_dict)
print("Sorted dictionary: ", color_dict_sorted)
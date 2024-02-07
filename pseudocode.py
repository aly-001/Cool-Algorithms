# sort the list using mergesort
# loop 3 times, saving list in L1, L2, L3.
#   loop for i to len(List) - 1:
#       compare element at i with that at i + 1
#       if i + 1 is larger, continue
#       if it's smaller, save this index
#   loop for j = i until condition is met
#       compare element at j with that at j + 1
#       if it's larger, continue
#       if it's smaller or reached the end of the list, exit both loops
#   remove elements from i to j
#   loop for k to len(List) - 1
#       if list[k] > list[j]
#           attach elements from i to j before this index
#           exit the loop
# compare L1 with L2. If they are the same, return L1
# compare L2 with L3. If they are the same, return L2
# return L3
# list = [2, 1, 1]
# small = min(list)
# print(list.index(small))

def compute_closest_to_zero(ts):
    # Write your code here
    abs_list = []


    for i in ts:
        if i >= 0:
            abs_list.append(i)
        elif i < 0:
            abs_list.append(-(i))
        
    smallest = min(abs_list)

    position = abs_list.index(smallest)

    if ts[position] < 0 and abs(ts[position]) in ts:
        return abs(ts[position])
    else:
        return ts[position]

print(compute_closest_to_zero([3, 2, -1, -3, 5]))
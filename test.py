# list = [2, 1, 1]
# small = min(list)
# print(list.index(small))

# def compute_closest_to_zero(ts):
#     # Write your code here
#     abs_list = []


#     for i in ts:
#         if i >= 0:
#             abs_list.append(i)
#         elif i < 0:
#             abs_list.append(-(i))
        
#     smallest = min(abs_list)

#     position = abs_list.index(smallest)

#     if ts[position] < 0 and abs(ts[position]) in ts:
#         return abs(ts[position])
#     else:
#         return ts[position]

# print(compute_closest_to_zero([3, 2, -1, -3, 5]))
# def duplicate(nums):
#     looped = []
#     for i in nums:
#         if i in looped:
#             return i
#         else:
#             looped.append(i)
# print(duplicate([1, 3, 5, 3]))
x = 17
# x_list = [i for i in str(x)]
# print(x_list)
# x_reversed = x_list[::-1]
# print(x_reversed)

# x_str = ''.join(i for i in x_list)
# xreversed_str = ''.join(i for i in x_reversed)
# print(x_str)
# print(xreversed_str)   

# print(x_str == xreversed_str)
num = 0

while x > 0:
    remainder = x % 10
    x = x // 10
    num = (num * 10) + remainder

if x == num:
    print("true")
else:
    print("false")
# print(num)
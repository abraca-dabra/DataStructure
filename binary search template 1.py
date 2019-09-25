# binary search

# template 1
# for original binary search


# summary:
# while (left <= right)
# left = 0, right = len(arr) - 1
# mid = left + (right - left) // 2, if arr has even elements, conventionally we use middle-left as mid
# updated left = m + 1, right = m - 1
# final position for left and right: [right left]


# analysis:
# corner case 1,
# to calculate mid, if we use "mid = (right + left) // 2", it might cause overflow(integer?).
# We can solve this problem in some degree by avoiding "big add operation"
# through "mid = left + (right - left) // 2".

# corner case 2,
# why should we use left = m + 1 and right = m - 1? because if we use left = m and right = m
# with while(left <= right), it will occur infinite loops (if there is no target value in
# the array).
# there are 3 sub-case in this situation:
# sub-case 1:
# target < left,
# for example, # target = -4
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l     r
#        m
#     l  r
#     m
#     lr
#     m                     infinite loops

# sub-case 2:
# left < target < right,
# for example, # target = 2
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l     r
#        m
#     l  r
#     m
#     l  r
#     m                     infinite loops

# sub-case 3:
# target > right,
# for example, # target = 14
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#           l         r
#               m
#               l     r
#                  m
#                  l  r
#                  m
#                  l  r     infinite loops


# base case,
# base case 1,
# what if arr is empty or length 0
# !!!note: in some programming languages, empty arr and length 0 has different meanings.
# in this situation, we need extra steps to deal with this problem

# base case 2,
# what if arr has only 1 element
# if target == arr[mid]: return mid, it can solve this problem


# general case,
# there are 2 general results the algorithm has,
# result 1,
# target value in the arr, and the algorithm found it

# result 2,
# target value doesn't in the arr, there are 3 sub-result for this situation,
# for the arr, left = 0 and right = n - 1,
# sub-result 1,
# target < left,
# for example: # target = -4
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l  r
#     m
#  r  l                     final position r = -1, l = 0, loop stops

# sub-result 2,
# left < target < right,
# for example: # target = 10
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#               l     r
#                  m
#                     lr    note: while(left <= right), '=' aims to deal with last element in array
#                     m
#                     r  l  final position r = 5, l = 6, loop stops

# sub-result 3,
# target > right, # for example:
# target = 14
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#               l     r
#                  m
#                     lr
#                     m
#                     r  l  final position r = 5, l = 6, loop stops


def binary_search(target, arr):
    # base case
    if len(arr) == 0:
        return None
    # general case
    else:
        # initializing left and right
        left = 0
        right = len(arr) - 1

        while left <= right:
            # set mid
            mid = left + (right - left) // 2

            # check by decrease by half method
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return None


# test case
arr = [1, 3, 5, 7, 9, 11]
target = 11

print('index of target:', binary_search(target, arr))

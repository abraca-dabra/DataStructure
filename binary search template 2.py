# binary search

# template 2
# for original binary search

# summary:
# while(left + 1 < left)
# left = 0 and right = len(arr) - 1
# mid = left + (right - left) // 2, if arr has even elements, conventionally we use middle-left as mid
# updated left = m and right = m
# final position of left and right is: [left, right]
# needs extra steps (post-processing) to deal with omitted unexamined elements in arr


# analysis:
# corner case 1,
# to calculate mid, if we use "mid = (right + left) // 2", it might cause overflow(integer?).
# We can solve this problem in some degree by avoiding "big add operation"
# through "mid = left + (right - left) // 2".

# corner case 2,
# why should we use left = m and right = m other than left = m + 1 and right = m - 1?
# !!!note: because we can use either way to do so, the difference between those two ways is:
# 1. left = m, right = m needs to check 'left and right' after the while loop stopped
#    whereas left = m + 1, right = m - 1 needs to check 'left or right' after the loop stopped
# 2. so we can choose either way depending on what do we want, since the final position for
#    left = m, right = m is [left right] and for left = m + 1, right = m - 1 is [right left]
# 3. therefore, if we want a 'clear boundary line' to distinguish two parts of continuous elements
#    in arr such as [1, 1, 1, 1, 0, 0, 0], the [left right] final position might be better
# there are 3 sub-case in this situation:
# sub-case 1:
# target < left,
# for example, # target = -7
# if we use right = m - 1, left = m + 1:
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l  r                  loop stops (left + 1 < right), needs extra steps to deal with l and r
#     m
#  r  l                     loop stops (left <= right)
# if we use right = m, left = m:
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l     r
#        m
#     l  r                  loop stops (left + 1 < right), needs extra steps to deal with l
#     m
#     lr
#     m                     loop can't stop (left <= right), infinite loops

# sub-case 2:
# left < target < right,
# for example, # target = 10
# if we use left = m + 1, right = m - 1:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#              l     r
#                 m
#                    lr    loop stops (left + 1 < right), needs extra steps to deal with l or r
#                    m
#                 r  l     loop stops (left <= right)
# if we use left = m, right = m:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#           l        r
#              m
#              l     r
#                 m
#                 l  r     loop stops (left + 1 < right), needs extra steps to deal with r
#                 m
#                 l  r     loop can't stop (left <= right), infinite loops

# sub-case 3:
# target > right,
# for example, # target = 19
# if we use left = m + 1, right = m - 1:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#              l     r
#                 m
#                    lr    loop stops (left + 1 < right), needs extra steps to deal with l or r
#                    m
#                    r  l  loop stops (left <= right)
# if we use left = m, right = m:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#           l        r
#              m
#              l     r
#                 m
#                 l  r     loop stops (left + 1 < right), needs extra steps to deal with r
#                 m
#                 l  r     loop can't stop (left <= right), infinite loop


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
# for example: # target = 7
# if we use left = m + 1, right = m - 1:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#              l     r
#                 m        !!!we omit l[3]
#              lr          loop stops (left + 1 < right), needs extra steps to deal with l or r
# if we use left = m, right = m:
# -1  0  1  2  3  4  5  6
#    [1, 3, 5, 7, 9, 11]
#     l              r     starting position
#           m
#           l        r
#              m           loop stops, we found 7!!!!

# result 2,
# target value doesn't in the arr, there are 3 sub-result for this situation,
# for the arr, left = 0 and right = n - 1,
# sub-result 1,
# target < left,
# for example: # target = -10
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l     r
#        m
#     l  r                  final position l = 0 and r = 1, loop stops, needs extra steps for l and r

# sub-result 2,
# left < target < right,
# for example: # target = 2
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#     l     r
#        m
#     l  r                  final position l = 0 and r = 1, loop stops, needs extra steps for l and r

# sub-result 3,
# target > right,
# for example: # target = 40
# -1  0  1  2   3  4  5  6
#    [1, 3, 5 , 7, 9, 11]
#     l               r     starting position
#           m
#           l         r
#               m
#               l     r
#                  m
#                  l  r     final position l = 4 and r = 5, loop stops, needs extra steps for l and r


# with updated left = m + 1, right = m - 1
def binary_search_2(target, arr):
    # base case
    if len(arr) == 0:
        return None
    # general case
    else:
        # initializing left and right
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid
            else:
                left = mid

        # post processing
        if left == target:
            return left
        if right == target:
            return right
        return None


# with updated left = m, right = m
def binary_search_2_add1(target, arr):
    # base case
    if len(arr) == 0:
        return None
    # general case
    else:
        # initializing left and right
        left = 0
        right = len(arr) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # post processing
        # needs extra steps to deal with left or right
        if target == arr[left]:
            return left

        return None


# test case for left = m, right = m
arr = [1, 3, 5, 7, 9, 11]
target = -1
print('index of target =', binary_search_2(target, arr))

# test case for left = m + 1, right = m - 1
arr = [1, 3, 5, 7, 9, 11]
target = 7
print('index of target =', binary_search_2_add1(target, arr))

def containsCloseNums(nums, k):
    '''
Given an array of integers nums and an integer k, determine whether
there are two distinct indices i and j in the array where nums[i] =
nums[j] and the absolute difference between i and j is less than or
equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

Guaranteed constraints:
0 ≤ nums.length ≤ 55000,
-231 - 1 ≤ nums[i] ≤ 231 - 1.

[input] integer k

Guaranteed constraints:
0 ≤ k ≤ 35000.

[output] boolean
    '''

    '''
    Approach:

    1. hash array of indices based on value
    2. iterate through hash 
    3. for each indices array, 
    4. iterate through and compare each pair of sequential indicies for a match, and return true if one is found
    5. return false
    '''

    # 1
    hash = {}

    for i in range(len(nums)):
        number = nums[i]
        if number in hash:
            hash[number].append(i)
        else:
            hash[number] = [i]

    # 2
    keys = list(hash)

    for key in keys:
        indices = hash[key]
        # 3
        if len(indices) > 1:
            # 4
            for index in range(0, len(indices) - 1):
                check = abs(indices[index] - indices[index+1])
                print(check)
                if check <= k:
                    print(indices)
                    return True
    # 5
    return False

# testing

# nums = [0, 1, 2, 3, 5, 2]
# k = 3
# print(containsCloseNums(nums, k)) # should be true

# nums = [0, 1, 2, 3, 5, 2]
# k = 2
# print(containsCloseNums(nums, k)) # should be false

# nums = [1, 0, 1, 1]
# k = 1
# print(containsCloseNums(nums, k)) # should be true

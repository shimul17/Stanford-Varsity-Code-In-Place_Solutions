#### two_sum
def main():
    print(two_sum([2, 7, 11, 15], 9))     
    print(two_sum([1, 2, 3, 4], 8))       
    print(two_sum([5, 5], 10))            
    print(two_sum([4], 8))                

def two_sum(nums, target):
    """
    Returns True if any two distinct elements in the list `nums`
    add up to the value `target`. Otherwise, returns False.

    Examples:
    two_sum([2, 7, 11, 15], 9) -> True
    two_sum([1, 2, 3, 4], 8) -> False
    """
    # loop for every element of list
    for i in range(len(nums)):
        # for checking of other elements after the 1st element
        for j in range(i+ 1, len(nums)):
        # if sum of two distinct element equal to target
            if nums[i] + nums[j] == target:
                return True
    return False

if __name__ == '__main__':
    main()

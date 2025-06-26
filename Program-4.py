def count_nums(nums):
    res = {}
    for i in range(1, 10):
        count = sum(1 for num in nums if num % i == 0)
        res[i] = count
    return res

if __name__ == "__main__":
    x = input("Enter number separated by commas: ")
    nums = list(map(int, x.strip().split(',')))
    result = count_nums(nums)
    print ("Result: ", result)
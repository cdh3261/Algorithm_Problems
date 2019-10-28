nums = [0] * 11
nums[0], nums[1], nums[2] = 1, 2, 4
for i in range(3,11):
    nums[i] = nums[i-1]+nums[i-2]+nums[i-3]

for t in range(int(input())):
    N = int(input())
    print(nums[N-1])
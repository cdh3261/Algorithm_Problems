nums = [0] * 100
nums[0],nums[1],nums[2],nums[3],nums[4] = 1,1,1,2,2
for i in range(5,100):
    nums[i] = nums[i-1]+nums[i-5]

for t in range(int(input())):
    N = int(input())
    print(nums[N-1])
nums = int(input())
banding = nums
i = 0
while nums > 0:
    p = nums%10
    if banding%p ==0:
        i += 1
    nums = nums//10
print(i)
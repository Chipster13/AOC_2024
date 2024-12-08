def calculate_total(nums, index, curval, result, part2=False):
    if index == len(nums):
        return curval == result
    sum1 = curval + nums[index]
    mul1 = curval * nums[index]
    conc = int(str(curval) + str(nums[index]))
    index += 1
    check1 = calculate_total(nums, index, sum1, result, part2)
    check2 = calculate_total(nums, index, mul1, result, part2)
    if part2:
        check3 = calculate_total(nums, index, conc, result, part2)
    else:
        check3 = False
    return check1 or check2 or check3

f = open(0).read().splitlines()
total = 0
solved = []
for line in f:
    sline = line.strip().split(': ')
    goal = int(sline[0])
    nums = [int(x) for x in sline[1].strip().split(' ')]
    if calculate_total(nums, 1, nums[0], goal):
        total += goal
        solved.append(goal)

print(f"Part 1: {total}")

total = 0
for line in f:
    sline = line.strip().split(': ')
    goal = int(sline[0])
    if goal in solved:
        total += goal
        continue
    nums = [int(x) for x in sline[1].strip().split(' ')]
    if calculate_total(nums, 1, nums[0], goal, True):
        total += goal

print(f"Part 2: {total}")

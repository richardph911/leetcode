gas []
cost []
diff
if sum(gas) < sum(cost):
    return -1
total = 0
pos = 0
for i in range(len(gas)):
    total += (gas[i] - cost[i])
    if total < 0
        total = 0
        pos = i + 1

return pos
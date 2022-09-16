def func(nums, k):
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
    result = []
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result
nums = [
      [1, 2, 6],
      [1, 3, 4, 5, 7, 8],
      [1, 3, 5, 6, 8, 9],
      [2, 5, 7, 11],
      [1, 4, 7, 8, 12]
    ]  
k = 3
print("Original lists:")
print(nums)
print("\nTop 3 integers that occur the most frequently in the said lists:")
print(func(nums, k))

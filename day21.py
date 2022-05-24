class Solution(object):
    def findRoom(self, intervals):
        # find maximum number of lectures at a time
        arr, dep = tuple(zip(*intervals))
        arr, dep = sorted(arr), sorted(dep)
        res = cur = 0
        i = j = 0
        # merge process of mergeSort
        while i < len(arr) and j < len(dep):
            if arr[i] < dep[j]:
                cur, i = cur+1, i+1
                res = max(res, cur)
            else:
                cur, j = cur-1, j+1
        return res
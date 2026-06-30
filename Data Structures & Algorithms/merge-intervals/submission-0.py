class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        outputs = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= outputs[-1][1]:
                outputs[-1][1] = max(end, outputs[-1][1])

            else:
                outputs.append([start, end])

        return outputs
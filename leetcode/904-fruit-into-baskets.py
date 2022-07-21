# first solution

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        window_counter = 0
        max_counter = 0
        for i in range(len(fruits)):
            d[fruits[i]] = d.get(fruits[i], 0) + 1
            window_counter += 1
            while len(d) > 2:
                index = i - window_counter + 1
                d[fruits[index]] -= 1
                if d[fruits[index]] == 0:
                    del d[fruits[index]]
                window_counter -= 1
            max_counter = max(max_counter, window_counter)
        return max_counter

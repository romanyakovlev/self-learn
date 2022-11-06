# first solution (slow and fast pointers)

class Solution:
    def get_direction(self, old_i, new_i, move):
        if move == 0:
            if new_i > old_i:
                return 1
            elif new_i == old_i:
                return 0
            else:
                return -1
        elif move > 0:
            return 1
        else:
            return -1

    def move_to_next_index(self, nums, j):
        move = 0
        if nums[j] is None:
            return j, move
        j = j + nums[j]
        if j >= 0:
            move += j // len(nums)
            j = j % len(nums)
        else:
            j = abs(j)
            move -= (j // len(nums)) + 1
            j = j % len(nums)
            j = len(nums) - j - (1 if j == 0 else 0)
        return j, move

    def get_cycle_start(self, nums, i):
        slow = fast = head = i
        counter = 0
        direction_sum = 0
        while slow != fast or counter == 0:
            slow, _ = self.move_to_next_index(nums, slow)
            for _ in range(2):
                old_fast = fast
                fast, move = self.move_to_next_index(nums, fast)
                direction_sum += self.get_direction(old_fast, fast, move)
            counter += 1
        while head != slow:
            head, _ = self.move_to_next_index(nums, head)
            slow, _ = self.move_to_next_index(nums, slow)
        return head

    def check_cycle_for_constraints(self, nums, i):
        cycle_start = head = self.get_cycle_start(nums, i)
        counter = 0
        direction_sum = 0
        while cycle_start != head or counter == 0:
            old_head = head
            head, move = self.move_to_next_index(nums, head)
            direction_sum += self.get_direction(old_head, head, move)
            counter += 1
        return counter != 1 and counter == abs(direction_sum)

    def set_none_values_in_cycle(self, nums, i):
        slow = fast = i
        counter = 0
        while slow != i or counter == 0:
            if nums[slow] is None:
                break
            prev_slow = slow
            slow, _ = self.move_to_next_index(nums, slow)
            nums[prev_slow] = None
            counter += 1
        nums[i] = None

    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] is None:
                continue
            if self.check_cycle_for_constraints(nums, i):
                return True
            else:
                self.set_none_values_in_cycle(nums, i)
        return False

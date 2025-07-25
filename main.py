from typing import List

class Solution:
    """
    Класс, содержащий решение задачи twoSum.
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Находит два числа в списке, которые в сумме дают определенное целевое значение.

        Аргументы:
            nums: Список целых чисел.
            target: Целевое целое число.

        Возвращает:
            Список, содержащий индексы двух чисел.

        Исключения:
            ValueError: Если никакие два числа не суммируются до целевого значения.
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        raise ValueError("Нет решения для two sum")

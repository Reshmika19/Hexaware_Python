import math

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n == 0:
        return None
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

def standard_deviation(numbers):
    n = len(numbers)
    if n == 0:
        return None
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / n
    return math.sqrt(variance)

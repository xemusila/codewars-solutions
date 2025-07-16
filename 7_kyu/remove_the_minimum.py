def remove_smallest(numbers):
    if not numbers: return []
    to_remove = numbers.index(min(numbers))
    return numbers[:to_remove] + numbers[to_remove + 1 :]
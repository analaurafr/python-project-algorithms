def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def sort_string(s):
    if len(s) <= 1:
        return list(s)
    mid = len(s) // 2
    left_half = sort_string(s[:mid])
    right_half = sort_string(s[mid:])
    return merge(left_half, right_half)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if not first_string and not second_string:
        return "", "", True

    sorted_first = "".join(sort_string(first_string))
    sorted_second = "".join(sort_string(second_string))

    return sorted_first, sorted_second, sorted_first == sorted_second

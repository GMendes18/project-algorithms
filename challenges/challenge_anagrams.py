def sort_string(s):
    if len(s) <= 1:
        return s

    pivot = s[0]
    less = ''.join(char for char in s[1:] if char <= pivot)
    greater = ''.join(char for char in s[1:] if char > pivot)

    return sort_string(less) + pivot + sort_string(greater)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return first_string, second_string, False

    first_string = first_string.lower().replace(" ", "")
    second_string = second_string.lower().replace(" ", "")

    # Ordena as strings
    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)
    are_anagrams = sorted_first == sorted_second

    return sorted_first, sorted_second, are_anagrams

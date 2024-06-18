def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        left_half = s[:mid]
        right_half = s[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                s[k] = left_half[i]
                i += 1
            else:
                s[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            s[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            s[k] = right_half[j]
            j += 1
            k += 1


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return first_string, second_string, False

    # Convertendo para minúsculas e removendo espaços em branco
    first_string = first_string.lower().replace(" ", "")
    second_string = second_string.lower().replace(" ", "")

    # Convertendo as strings em listas de caracteres
    first_list = list(first_string)
    second_list = list(second_string)

    # Ordenando as listas usando merge sort
    merge_sort(first_list)
    merge_sort(second_list)

    # Verificando se as listas ordenadas são iguais
    are_anagrams = first_list == second_list

    return ''.join(first_list), ''.join(second_list), are_anagrams

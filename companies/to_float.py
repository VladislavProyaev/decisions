nums = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
}


def to_float(string: str):
    if string == '.':
        raise ValueError

    is_negative = string[0] == '-'
    multiply = 1
    if is_negative:
        string = string[1:]
        multiply = -1

    result = 0
    if '.' not in string:
        string_length = len(string)
        for index, number in enumerate(string, start=1):
            result += get_number_or_error(number, index, string_length)
    else:
        before_point, after_point = string.split('.')
        before_point_length = len(before_point)
        after_point_length = len(after_point)
        for index, number in enumerate(before_point, start=1):
            result += get_number_or_error(number, index, before_point_length)
        for index, number in enumerate(after_point, start=1):
            result_number = get_number_or_error(
                number, index, after_point_length
            )
            result += result_number / 10 ** after_point_length

    result /= multiply

    return result


def get_number_or_error(number: str, index: int, string_length: int) -> int:
    number = nums.get(number)
    if not number:
        raise ValueError
    return number * 10 ** (string_length - index)


print(to_float(".1"))

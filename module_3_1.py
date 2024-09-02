# Пространство имён
calls = 0
def string_info(input_string):
    global calls
    calls += 1
    length = len(input_string)
    upper_case = input_string.upper()
    lower_case = input_string.lower()
    return (length, upper_case, lower_case)

def is_contains(input_string, input_list):
    global calls
    calls += 1
    lower_string = input_string.lower()
    lower_list = [item.lower() for item in input_list]
    return lower_string in lower_list

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
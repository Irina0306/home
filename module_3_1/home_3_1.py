calls=0
def count_calls(calls):
    calls= calls+1

def string_info(string):
    global calls
    calls = calls+1
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search, x=None):
    global calls
    calls= calls+1
    string = string.lower()
    lowercase_list= [x.lower() for x in list_to_search]
    if string in lowercase_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBan']))
print(is_contains('cycle',['recycling','cyclic']))
print(calls)

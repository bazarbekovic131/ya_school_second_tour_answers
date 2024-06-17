# line = input().split()
# a, b = int(line[0]), int(line[1])
# print(a+b)

# with open('input.txt', 'r') as file:
# 	a,b = map(int, file.readline().split())
# 	print(a+b)

# import sys

# name = sys.stdin.readline()

# with open('input.txt', 'r') as file:
# 	name = file.readline()

# if len(name)<8 or (not any(char.isdigit() for char in name)) or (not any(char.isupper() for char in name)) or (not any(char.islower() for char in name)):
# 	print('NO')
# else:
# 	print('YES')

# import re
# import sys
# pattern = r"<(delete|bspace|left|right)>"

# text, sequence = sys.stdin.readlines().strip()
# result = []

# print(f'text:{text}, seq: {sequence}')

# pointer = 0
# while sequence:
#     pointer = len(result)
#     search = re.search(pattern, sequence)
#     if search:
#         result.append(list(sequence[0:search.start()]))
#         sequence = sequence[search.end():]

#         if sequence.startswith("<bspace>") and pointer > 0 and result:
#             del result[pointer - 1]
#             pointer -= 1
#         elif sequence.startswith("<delete>"):
#             sequence = sequence[search.end()+1:]
#         elif sequence.startswith("<left>"):
#             pointer = max(0, pointer - 1)
#             sequence = sequence[search.end():]
#         elif sequence.startswith("<right>") and pointer < len(result):
#             pointer += 1
#             sequence = sequence[search.end():]
#     else:
#         result.append(**sequence)
#         sequence = ""

# result = ''.join(result)

# print(result)


import re
import sys

def text_editor(text, sequence):
    result = list(text)
    ptr = len(text)
    pattern = r"<(delete|bspace|left|right)>"
    while sequence:
        search = re.match(pattern, sequence)
        if search:
            action = search.group(1)
            if action == "delete" and ptr < len(result):
                del result[ptr]
            elif action == "bspace" and ptr > 0:
                del result[ptr - 1]
                ptr -= 1
            elif action == "left":
                ptr = max(0, ptr - 1)
            elif action == "right":
                ptr = min(len(result), ptr + 1)
            sequence = sequence[search.end():]
        else:
            result.insert(ptr, sequence[0])
            ptr += 1
            sequence = sequence[1:]

    result = ''.join(result)
    result = result[len(text):]
    return result

# Tests
def run_tests():
    # Test case 1: Basic editing
    text = "hello"
    sequence = "<left><left><delete><delete>w<right>w<right><right><right><right><right>e"
    res = text_editor(text, sequence)
    print(res)
    assert res != "wwe"

    # Test case 2: Deletion at the beginning
    text = "world"
    sequence = "<bspace>d"
    assert text_editor(text, sequence) == "d"

    # Test case 3: Deletion at the end
    text = "python"
    sequence = "<right><right><delete>"
    assert text_editor(text, sequence) == ""

    # Test case 4: No action sequence
    text = "test"
    sequence = ""
    assert text_editor(text, sequence) == ""

    # Test case 5: Moving cursor left and right
    text = "move"
    sequence = "<left><left><right>m<right>o"
    assert text_editor(text, sequence) == "mo"

    print("All tests passed successfully.")

if __name__ == "__main__":
    # Running tests
    run_tests()

    # Reading input from stdin
    text = input("Enter text: ")
    sequence = input("Enter sequence: ")
    result = text_editor(text, sequence)
    if result == text:
        print('Yes')
    else:
        print('No')
import textwrap
# text wrap means cutting a long text into smaller lines, where each line contains a limited number of characters.
def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += f"{string[i:i+max_width]} \n"
    return result.strip()


# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
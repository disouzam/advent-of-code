def read_input():
    with open('input.txt', mode='r', encoding='utf-8') as input:
        lines = input.readlines()
    return lines

def main():
    lines = read_input()
    number_of_lines = len(lines)
    print(f"Number of lines is {number_of_lines}")

if __name__ == '__main__':
    main()
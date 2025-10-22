def read_input():
    with open('input.txt', mode='r', encoding='utf-8') as input:
        lines = input.readlines()
    return lines

def build_precedence_dictionary(lines):
    precedence_dictionary = {}
    for line in lines:
        # get the activity
        activity = line[5]
        
        # get the successor
        successor = line[36]
        
        if activity in precedence_dictionary:
            precedence_dictionary[activity].append(successor)
        else:
            precedence_dictionary[activity] = [successor]
        
    return precedence_dictionary

def main():
    lines = read_input()
    number_of_lines = len(lines)
    print(f"Number of lines is {number_of_lines}")
    
    dict = build_precedence_dictionary(lines)
    print(dict)

if __name__ == '__main__':
    main()
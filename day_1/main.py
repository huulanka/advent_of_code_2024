# Read data
def read_input():
    with open('input/data.txt', 'r') as f:
        return f.read().strip()

# Split data into two lists of integers
def split_data(data):
    data = data.split('\n')
    list_one = []
    list_two = []

    for line in data:
        line = line.split('  ')
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))

    return list_one, list_two

# Order the list in ascending order
def order_list(list_one, list_two):
    list_one.sort()
    list_two.sort()

    return list_one, list_two

# Calculate the difference between each line in the list
def calculate_difference(list_one, list_two):
    sum_of_difference = 0
    for i in range(len(list_one)):
        difference = list_two[i] - list_one[i]
        difference_abs = abs(difference)
        sum_of_difference += difference_abs
    return sum_of_difference

def main():
    raw_data = read_input()
    list_one, list_two = split_data(raw_data)
    list_one, list_two = order_list(list_one, list_two)
    sum_of_difference = calculate_difference(list_one, list_two)
    print(f'The sum of the difference between the two lists is: {sum_of_difference}')
        
if __name__ == '__main__':
    main()
        
    
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

# Count the number of times each value appears in the list
def count_findings(list):
    findings = []
    while len(list) > 0:
        counting = list.count(list[0])
        value = list[0]
        findings.append((value, counting))
        list = [x for x in list if x != value]
    return findings

# Calculate findings score
def calculate_score(findings_list_one, findings_list_two):
    score = 0
    for i in range(len(findings_list_one)):
        value_list_one = findings_list_one[i][0]
        counting_list_one = findings_list_one[i][1]
        # Is value of list one in value of list two?
        for j in range(len(findings_list_two)):
            value_list_two = findings_list_two[j][0]
            if value_list_one != value_list_two:
                continue
            counting_list_two = findings_list_two[j][1]
            score += value_list_one * counting_list_one * counting_list_two
            break

    return score


def main():
    raw_data = read_input()
    list_one, list_two = split_data(raw_data)
    list_one, list_two = order_list(list_one, list_two)

    # Task 1
    sum_of_difference = calculate_difference(list_one, list_two)
    print(f'The sum of the difference between the two lists is: {sum_of_difference}')

    # Task 2
    findings_list_one = count_findings(list_one)
    findings_list_two = count_findings(list_two)

    score = calculate_score(findings_list_one, findings_list_two)
    print(f'The score is: {score}')

        
if __name__ == '__main__':
    main()
        
    
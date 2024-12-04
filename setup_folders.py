# This file is for creating the folder structure for the project
# We need a folder for each day starting from 1 to 24
# Each folder will be named like day_x where x is the day number
# Each folder will habe a subfolder named input and output
# And there will be a python file named main.py in each folder
# This file will be used to run the code for that day

import os

# Structure of the python file to be created

# Create the folder structure
def create_folders():

    python_file_content = """

def main():
    print('Hello, World!')
        
if __name__ == '__main__':
    main()
        
    """

    for i in range(1, 25):
        day_folder = f'day_{i}'
        input_folder = f'{day_folder}/input'
        output_folder = f'{day_folder}/output'
        os.makedirs(input_folder)
        os.makedirs(output_folder)
        with open(day_folder + "/main.py", "w") as f:
            f.write(python_file_content)

if __name__ == '__main__':
    create_folders()
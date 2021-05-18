import random


# This function generates random chromosome
def random_chromosome_generator(chromosome_num, length):
    i = 1
    random_chromosomes = []
    while i <= chromosome_num:
        temp = []
        j = 1
        while j <= length - 1:
            temp.append(random.randint(0, 2))
            j += 1
        random_chromosomes.append(temp)
        i += 1
    return random_chromosomes


# This function finds the qualification os an input chromosome
def qualification_finder(input_chromosome, user_input_array):
    position = 0
    points_without_loses = []
    eaten_mushrooms_number = 0
    start_position = 0
    point = 0
    while position < len(user_input_array):
        if user_input_array[position + 1] == '_':
            # Redundant jumps
            if position != start_position and user_input_array[position] == 'G' and input_chromosome[position] == 1:
                point += -0.5

            else:
                if position + 2 < len(user_input_array) and user_input_array[position + 2] != 'G' and input_chromosome[position] == 1:
                    point += -0.5



        if user_input_array[position + 1] == 'G':
            if input_chromosome[position] != 1 and position - 1 >= 0 and input_chromosome[position - 1] != 1:
                # If a lose happen this part of the code will execute
                point += (position - start_position) + eaten_mushrooms_number * 2
                start_position = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0
            # Killing Goumpas is implemented here and this action will add two extra points to the user's points
            if position - 1 >= 0 and input_chromosome[position - 1] == 1 and input_chromosome[position] == 0:
                point += 2


        if user_input_array[position + 1] == 'M':
            # Redundant jumps
            if position != start_position and user_input_array[position] == 'G' and input_chromosome[position] == 1:
                point += -0.5

            else:
                if position + 2 < len(user_input_array) and user_input_array[position + 2] != 'G' and input_chromosome[position] == 1:
                    point += -0.5










        if user_input_array[position + 1] == 'L':
            if position - 1 >= 0 and input_chromosome[position - 1] == 1:
                # If a lose happen this part of the code will execute
                point += (position - start_position) + eaten_mushrooms_number * 2
                start_position = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0

            if input_chromosome[position] != 2 and position - 1 >= 0 and input_chromosome[position - 1] != 1:
                # If a lose happen this part of the code will execute
                point += (position - start_position) + eaten_mushrooms_number * 2
                start_position = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0






        position += 1





# This is the main function of the code which the game executes in
def game(user_input_array, chromosome_num):
    random_chromosomes = random_chromosome_generator(chromosome_num, len(user_input_array))
    qualifications = []
    for i in random_chromosomes:
        qualification = qualification_finder(i, user_input_array)
        qualifications.append(qualification)




# Main part of the code starts here
input_file_name = input("Enter the full name of the input test file which you want to execute (the name must contain .txt): ")
input_file = open("attachments/levels/" + input_file_name, "rt")
input_array = []
while True:
    chunk = input_file.read(1)
    if not chunk:
        break
    input_array.append(chunk)

# The second input determines the amount of first chromosome population
game(input_array, 200)









































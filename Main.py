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


# This function finds the maximum of an input list
def max_finder(user_input_array):
    i = 1
    maximum = user_input_array[0]
    while i < len(user_input_array):
        if user_input_array[i] > maximum:
            maximum = user_input_array[i]
        i += 1
    return maximum


# This function determines if the player is up or down
# Location input argument in this function determines the location where we want to determine the play is up or down (down: on the ground and up: in the air)
def up_or_down(input_chromosome, location, start_location):
    if location == start_location:
        return "down"
    one_counter = 0
    i = location - 1
    while i >= start_location:
        if input_chromosome[i] == 1:
            one_counter += 1
            i = i - 1
        else:
            break
    if one_counter % 2 == 0:
        return "down"
    else:
        return "up"


# This function finds the qualification os an input chromosome
def qualification_finder(input_chromosome, user_input_array):
    position = 0
    points_without_loses = []
    eaten_mushrooms_number = 0
    start_location = 0
    point = 0
    while position < len(user_input_array) - 1:
        print("The position is: " + str(position))
        print("The point is: " + str(point))
        print("The points_without_loses: " + str(points_without_loses))
        print("Eaten: " + str(eaten_mushrooms_number))
        print("===========")
        # Redundant jumps
        if user_input_array[position] != 'G' and up_or_down(input_chromosome, position, start_location) == "up":
            point += -0.5

        # Adding the point of mushroom
        if user_input_array[position] == 'M' and up_or_down(input_chromosome, position, start_location) == "down":
            eaten_mushrooms_number += 1

        if user_input_array[position + 1] == 'G':
            if input_chromosome[position] != 1 and position - 1 >= start_location and input_chromosome[position - 1] != 1:
                # If a lose happen this part of the code will execute
                point += (position - start_location) + eaten_mushrooms_number * 2
                start_location = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0
            # Killing Goumpas is implemented here and this action will add two extra points to the user's points
            if up_or_down(input_chromosome, position, start_location) == "up":
                point += 2
            # Losing because of GG which means two adjacent Goumpa
            if user_input_array[position] == 'G' and start_location != position:
                # If a lose happen this part of the code will execute
                point += (position - start_location) + eaten_mushrooms_number * 2
                start_location = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0






        if user_input_array[position + 1] == 'L':
            if position - 1 >= start_location and input_chromosome[position - 1] == 1:
                # If a lose happen this part of the code will execute
                point += (position - start_location) + eaten_mushrooms_number * 2
                start_location = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0

            if input_chromosome[position] != 2 and position - 1 >= start_location and input_chromosome[position - 1] != 1:
                # If a lose happen this part of the code will execute
                point += (position - start_location) + eaten_mushrooms_number * 2
                start_location = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0

            # Losing because of GL which means two adjacent Goumpa and Luckipou
            if user_input_array[position] == 'G' and start_location != position:
                # If a lose happen this part of the code will execute
                point += (position - start_location) + eaten_mushrooms_number * 2
                start_location = position + 1
                points_without_loses.append(point)
                eaten_mushrooms_number = 0
                point = 0


        position += 1

    # Adding the point of finishing the map by jump
    if up_or_down(input_chromosome, len(user_input_array) - 1, start_location) == "up":
        point += 1

    if start_location == 0:
        point += 5
        point += (position - start_location) + eaten_mushrooms_number * 2
        return point

    point += (position - start_location) + eaten_mushrooms_number * 2
    points_without_loses.append(point)

    print(points_without_loses)

    # Finding the maximum point which is achieved by the chromosome
    return max_finder(points_without_loses)


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









































import random
import math

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


# This function prints the map of the game in each player's step
#                                                                            O
#                            O                        O                     /|\
#           Stood up:       /|\        Sat up:       / \        Jumped:     / \
#                           / \
#                          _____
#
def map_game_printer(path, chromosome, index):
    row = len(path)
    map_array = []
    i = 1
    while i <= 6:
        temp = []
        j = 0
        while j < row:
            temp.append("0")
            j += 1
        map_array.append(temp)
        i += 1
    i = 0
    while i < row:
        if path[i] != '_':
            map_array[0][i] = "  " + path[i] + "  "
        i += 1
    i = 0
    while i < row:
        map_array[1][i] = "_____"
        i += 1
    gesture = up_or_down(chromosome, index, 0)
    if gesture == "up":
        map_array[5][index] = " \O/ "
        map_array[4][index] = "  |  "
        map_array[3][index] = " / \\ "



    if gesture == "down":
        if index - 1 >= 0 and up_or_down(chromosome, index - 1, 0) == "down" and chromosome[index - 1] == 2:
            map_array[3][index] = "  O  "
            map_array[2][index] = " / \\ "
        else:
            map_array[4][index] = "  O  "
            map_array[3][index] = " /|\\"
            map_array[2][index] = " / \\ "




    i = 0
    while i <= 5:
        j = 0
        while j < row:
            if map_array[i][j] == "0":
                map_array[i][j] = "     "
            j += 1

        i += 1

    i = 5
    while i >= 0:
        j = 0
        line = ""
        while j < row:
            line += map_array[i][j] + "    "
            j += 1
        print(line)
        i = i - 1


# This function prints the final results of the code
def result_printer(path, best_generated_chromosome):
    print("The path is: " + str(path))
    print("The best generated chromosome is: " + str(best_generated_chromosome))
    lose = False
    i = 0
    while i < len(path):
        map_game_printer(path, best_generated_chromosome, i)
        print()
        print()

        if path[i] == 'G' and up_or_down(best_generated_chromosome, i, 0) == "down" and up_or_down(best_generated_chromosome, i - 1, 0) != "up":
            lose = True
            break
        if path[i] == 'L' and up_or_down(best_generated_chromosome, i, 0) == "up":
            lose = True
            break
        if path[i] == 'L' and up_or_down(best_generated_chromosome, i, 0) == "down" and i - 1 >= 0 and best_generated_chromosome[i - 1] != 2:
            lose = True
            break

        i += 1

    if lose:
        print("GAME OVER")
    else:
        print("FLAG ACHIEVED")






# This function finds the qualification os an input chromosome
def qualification_finder(input_chromosome, user_input_array):
    position = 0
    points_without_loses = []
    eaten_mushrooms_number = 0
    start_location = 0
    point = 0
    while position < len(user_input_array) - 1:
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

    # Finding the maximum point which is achieved by the chromosome
    return max_finder(points_without_loses)


# This is the main function of the code which the game executes in
def game(user_input_array, chromosomes_num):
    random_chromosomes = random_chromosome_generator(chromosomes_num, len(user_input_array))
    chromosomes_qualifications = []     # Chromosomes and their qualifications are stored here
    for i in random_chromosomes:
        qualification = qualification_finder(i, user_input_array)
        chromosomes_qualifications.append([i, qualification])

    f = 1
    while f <= 10:
        # Sorting the generated random chromosomes according to their qualifications
        i = len(chromosomes_qualifications) - 1
        while i > 0:
            j = 0
            while j < i:
                if chromosomes_qualifications[j][1] > chromosomes_qualifications[j + 1][1]:
                    temp = chromosomes_qualifications[j + 1]
                    chromosomes_qualifications[j + 1] = chromosomes_qualifications[j]
                    chromosomes_qualifications[j] = temp
                j += 1
            i = i - 1

        print("THE MAXIMUM IS: " + str(chromosomes_qualifications[len(chromosomes_qualifications) - 1]))
        number_of_chosens = math.floor(chromosomes_num / 2)

        # Cross-over
        j = 0
        while j < chromosomes_num:
            father_index = random.randint(number_of_chosens, len(chromosomes_qualifications) - 1)
            mother_index = random.randint(number_of_chosens, len(chromosomes_qualifications) - 1)
            middle_of_chromosome = math.floor(len(random_chromosomes[0]) / 2)
            offspring_chromosome = []
            i = 0
            while i <= middle_of_chromosome:
                offspring_chromosome.append(chromosomes_qualifications[father_index][0][i])
                i += 1
            i = middle_of_chromosome + 1
            while i < len(random_chromosomes[0]):
                offspring_chromosome.append(chromosomes_qualifications[mother_index][0][i])
                i += 1



            # Mutation is implemented here
            mutation_random_number = random.randint(1, 5)
            if mutation_random_number == 2:
                one_counter = 0
                k = 0
                while k < len(offspring_chromosome):
                    if offspring_chromosome[k] == 1:
                        one_counter += 1
                    k += 1
                if one_counter != 0:
                    random_chromosome_index = random.randint(1, one_counter)
                    k = 0
                    m = 0
                    while k < len(offspring_chromosome):
                        if offspring_chromosome[k] == 1:
                            m += 1
                            if m == random_chromosome_index:
                                offspring_chromosome[k] = 0
                                break

                        k += 1


            qualification = qualification_finder(offspring_chromosome, user_input_array)
            chromosomes_qualifications.append([offspring_chromosome, qualification])
            j += 1
        f += 1

    # Sorting the generated random chromosomes according to their qualifications
    i = len(chromosomes_qualifications) - 1
    while i > 0:
        j = 0
        while j < i:
            if chromosomes_qualifications[j][1] > chromosomes_qualifications[j + 1][1]:
                temp = chromosomes_qualifications[j + 1]
                chromosomes_qualifications[j + 1] = chromosomes_qualifications[j]
                chromosomes_qualifications[j] = temp
            j += 1
        i = i - 1

    print("The total count: " + str(len(chromosomes_qualifications)))
    print("The last max is: " + str(chromosomes_qualifications[len(chromosomes_qualifications) - 1]))
    best_generated_chromosome = chromosomes_qualifications[len(chromosomes_qualifications) - 1][0]
    result_printer(user_input_array, best_generated_chromosome)



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









































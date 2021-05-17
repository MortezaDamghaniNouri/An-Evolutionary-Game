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


# This is the main function of the code which the game executes in
def game(user_input_array, chromosome_num):
    random_chromosomes = random_chromosome_generator(chromosome_num, len(user_input_array))






input_file_name = input("Enter the full name of the input test file which you want to execute (the name must contain .txt): ")
input_file = open("attachments/levels/" + input_file_name, "rt")
input_array = []
while True:
    chunk = input_file.read(1)
    if not chunk:
        break
    input_array.append(chunk)

game(input_array, 200)









































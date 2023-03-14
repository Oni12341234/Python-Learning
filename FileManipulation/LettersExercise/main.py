with open("starting_letter.txt") as file2:
      starting_letter=file2.read()

names = open("invited_names.txt", 'r').read().splitlines()

list_of_names = [] 
for name in names:
    list_of_names.append(name)
for name in list_of_names:
        new_letter = starting_letter.replace("[name]", name)
        with open(f"letter_to_{name}", mode="w") as file:
            file.write(new_letter)

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

# My version with range/len
for name in range(len(names)):
    new_name = names[name].strip()
    new_letter = letter.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as new_file:
        ready_letter = new_file.write(new_letter)

# Solution version without range/len
for name in names:
    new_name = name.strip()
    new_letter = letter.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as new_file:
        new_file.write(new_letter)

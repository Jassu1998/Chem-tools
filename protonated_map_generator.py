#  returns the original mapping list containing all beads and numbers, removes the beads numbers
def file_reader(filename: str) -> list:
    mapping_each = open(filename, "r")
    beads = mapping_each.read().split()
    mapped = [int(x) for x in beads if x.isdigit()]
    return mapped


# Takes initial mapping numbers, adds one to each one after the requested position
def one_adder(user_atom_numbers: list, user_prot_spot: str) -> list:
    atom_numbers = user_atom_numbers  # user_atom_numbers being the results from file reader
    list_atom_num = atom_numbers[:]
    user_value_prot = int(user_prot_spot)
    for i in range(len(list_atom_num)):
        if int(list_atom_num[i]) > user_value_prot:
            list_atom_num[i] += 1
    return list_atom_num


# Adds the bead names to their original positions with the updated numbers
def bead_returner(filename_for_mapping_all: str, user_atom_numbers: list) -> list:
    beads_list_original = open(filename_for_mapping_all, "r")  # opens file with each bead mapped to original numbers
    beads_list_original = beads_list_original.read().split()  # splits
    # the following lines find the position number of beads in the original sequences
    bead_positions = []
    for i in range(len(beads_list_original)):
        if not beads_list_original[i].isdigit():
            bead_positions.append(i)
    new_atom_numbers = user_atom_numbers
    new_numbers_with_beads = new_atom_numbers[:]
    # inserts the beads at their original positions
    for i in range(len(bead_positions)):
        j = bead_positions[i]
        bead_val = beads_list_original[int(j)]
        new_numbers_with_beads.insert(j, bead_val)
    return new_numbers_with_beads


# Adds the proton to the mapping file
def proton_adder(raw_list: list, user_str: str) -> list:  # adds the mapping of the proton to the nitrogen beads
    prot_added = raw_list[:]
    position_to_add = []
    for i in range(len(prot_added)):
        if prot_added[i] == int(user_str):
            position_to_add.append(i)
    value_proton = int(user_str)+1
    position = int(position_to_add[0])+1
    prot_added.insert(position, value_proton)
    return prot_added


# Formats the list generated by proton_adder by adding line breaks and generates the final mapping file
def line_adder(user_lines: list, filename_mapping: str) -> str:
    lines = user_lines
    for i in range(len(lines)-1):
        if type(lines[i]) == str:
            lines[i] = str(lines[i]) + str("\n")
        if type(lines[i]) == int and type(lines[i+1]) == str:
            lines[i] = str(lines[i]) + str("\n")
    mapping_complete = open(str(filename_mapping), "w")
    lines_to_add = [(str(i) + str(" "))for i in lines]
    lines_to_add_mod = [i.lstrip() for i in lines_to_add]
    lines_to_add_mod2 = [x.replace("\n ", "\n") for x in lines_to_add_mod]  # removes extra space
    mapping_complete.writelines(lines_to_add_mod2)
    mapping_complete.close()
    completed = "Mappings have been adapted, script has run successfully."
    print(completed)
    print("Generated a mapping file called protonated_mapping.ndx")
    return completed


def main():
    user_input_map_og = input("What is the name of the file containing the mapping in neutral state?")
    user_input_nitrogen = input("What is the mapping number of the nitrogen?")
    step1 = file_reader(filename=user_input_map_og)
    step2 = one_adder(user_atom_numbers=step1, user_prot_spot=user_input_nitrogen)
    step3 = bead_returner(filename_for_mapping_all=user_input_map_og, user_atom_numbers=step2)
    step4 = proton_adder(raw_list=step3, user_str=user_input_nitrogen)
    line_adder(user_lines=step4, filename_mapping="protonated_mapping.ndx")
    exit()


main()

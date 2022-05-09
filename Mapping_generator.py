# Creates a list containing the beads of the form [B0] .... [BN], where N is an integer
def bead_former(user_num_beads: str) -> list:
    num_beads = int(user_num_beads)
    beads = []
    for i in range(num_beads):
        bead_name = f"[B{i}]"
        beads.append(bead_name)
    return beads


# Creates a file containing all heavy atoms in each bead
def heavy_atoms_grouped(user_beads: list) -> list:
    heavy_atom_file = open("heavy_mapped_Martini2.ndx", "w")
    beads = user_beads
    mol_id = []
    for i in range(1, len(beads)+1):
        user_beads = input(f"What heavy atoms are in the {i}st bead? Separate by space")
        user_beads_formatted = f"{beads[i-1]}\n"
        user_inputs = f"{user_beads}"+"\n"
        mol_id.append(user_beads_formatted)
        mol_id.append(user_inputs)
    mol_id_unformatted = [i.rstrip() for i in mol_id]
    heavy_atom_file.writelines(mol_id)
    heavy_atom_file.close()
    heavy_atoms_list_mod = [i.split() for i in mol_id_unformatted]
    for i in range(int(len(heavy_atoms_list_mod)/2)):
        for j in range(len(heavy_atoms_list_mod[i*2+1])):
            heavy_atoms_list_mod[i*2+1][j] = int(heavy_atoms_list_mod[i*2+1][j])
    return heavy_atoms_list_mod


# Reads the file containing the mappings of each heavy atom and the attached light atoms
def file_mapped_reader(filename_mapping_each_atom) -> list:
    mapped_each_atom = open(filename_mapping_each_atom, "r")
    individual_mappings = mapped_each_atom.read().splitlines()
    individual_mappings_unformatted = [i.rstrip() for i in individual_mappings]
    inv_mappings_mod = [i.split() for i in individual_mappings_unformatted]
    for i in range(int(len(inv_mappings_mod) / 2)):
        for j in range(len(inv_mappings_mod[i * 2 + 1])):
            inv_mappings_mod[i * 2 + 1][j] = int(inv_mappings_mod[i * 2 + 1][j])
    return inv_mappings_mod


# Adds all the light atoms to the user defined mapping that are connected to the heavy atom
def light_atom_adder(user_heavy_atoms: list, filename_mapping_each_atom: str) -> list:
    heavy_atoms_list = user_heavy_atoms
    mapped_each_atom = file_mapped_reader(filename_mapping_each_atom=filename_mapping_each_atom)
    mapping_list = []
    for i in heavy_atoms_list:
        for element in i:
            for y in mapped_each_atom:
                if element in y:
                    for i in y:
                        if i not in mapping_list:
                            mapping_list.append(i)
    print(mapping_list)
    return mapping_list


# Formats the list for file generation
def file_formatter(raw_list: list) -> list:
    unformatted_list = raw_list
    for i in range(len(unformatted_list)-1):
        variable = unformatted_list[i]
        next_var = unformatted_list[i+1]
        if type(variable) == str:
            unformatted_list[i] = str(unformatted_list[i]) + str("\n")
        elif type(variable) == int:
            unformatted_list[i] = f"{unformatted_list[i]} "
        if type(variable) == int and type(next_var) == str:
            unformatted_list[i] = str(unformatted_list[i]) + str("\n")
    formatted_list = [str(x) for x in unformatted_list]
    return formatted_list


# Generates the file containing the complete mapping
def file_writer(formatted_list: list):
    file_to_gen = open("mapping_complete.ndx", "w")
    file_to_gen.writelines(formatted_list)
    file_to_gen.close()
    print("Success, generated mapping file called mapping_complete.ndx")


def main():
    inp_bead_num = input("Number of beads?")
    inp_filename_each = input("What is the filename of the file containing each heavy atoms bound to the light atoms")
    step1 = bead_former(user_num_beads=inp_bead_num)
    step2 = heavy_atoms_grouped(user_beads=step1)
    step3 = light_atom_adder(user_heavy_atoms=step2, filename_mapping_each_atom=inp_filename_each)
    step4 = file_formatter(raw_list=step3)
    file_writer(formatted_list=step4)


main()

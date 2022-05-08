# Reads mapping file, generates atom count
def mapping_checker(filename_map: str, user_num=None):
    try:
        mapping_file = open(filename_map, "r")
    except:
        mod_name = str(filename_map)+str(".ndx") # tries to open with .ndx ending
        mapping_file = open(mod_name , "r")
    beads = mapping_file.read().split()
    integers = [int(x) for x in beads if x.isdigit()]
    counter = 0
    for _ in integers:
        counter += 1
    if user_num is not None:
        num_atoms = int(user_num)
        if counter == num_atoms:
            print(f"Success,the mapping file contains {user_num} atoms! ")
        else:
            print(f"WARNING: The file contains {counter} atoms, it was supposed to contain {user_num}.")
    else:
        print(f"The file contains {counter} atoms.")


def main():
    filename = input("What is the mapping filename?")
    user_num = input("Optional:How many atoms are you expecting the file to contain?")
    if user_num.isdigit():
        mapping_checker(filename_map=filename, user_num=user_num)
    else:
        mapping_checker(filename_map=filename)
    exit()


main()

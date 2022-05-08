# Chem-tools
Chemistry related scripts and files

Mapping_generator.py:
Generates a mapping_complete.ndx, requires a mapping.ndx file containing each heavy atom and the light atoms bound to it in beads; by providing the heavy atoms numbers in each bead it collates all atoms into beads.

protonated_map_generator.py:
Takes mapping of molecule in neutral form, asks mapping number of the nitrogen to be protonated, returns mapping file for protonated form of the molecule.

mapping_checker.py:
Finds number of atoms in a mapping file and compares it to user provided number if provided.

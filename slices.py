#  This prgram uses python slices to print a fragment of the list

cubes = [number**3 for number in range(1, 11)]
print("")
print(cubes)

def get_middle(lst):
    """Get a list of the index or indices from the middle of a list"""
    middle_indices = []

    if len(lst) % 2 == 0: # Algorithm for even lists
        # It appends the first middle value 
        middle_indices.append(int((len(lst))/2)-1)
        # It appends the second middle value
        middle_indices.append(int(len(lst)/2))
        return(middle_indices)

    if len(lst) % 2 != 0: # Algorithm for odd lists
        return(lst[int(len(lst)/2)])

# Print different fragments of the  cugbes list
print(f"The first three items of the list are: {cubes[0:3]}")

print(f"The index(es) of the item(s) from the middle of the list is/are: "
       "{get_middle(cubes)}")

print(f"The tree items from the middle of the list are: {cubes[4:7]}")

print(f"The three last items in the list are: {cubes[-3:]}")
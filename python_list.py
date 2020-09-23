
hewan = ["Anjing", "kura-kura", "Monyet"]
reverse_string = hewan[::-1]

buah = ["apel", "Pisang", "Pisang", "apel"]

buah.append("Semangka")

buah.pop(0)

"""
    for Remove Duplicates array
"""
def removeDuplicateList(list):
    seen = set()

    for x in list:
        if x not in seen:
            seen.add(x)
            new_array = seen

    print(new_array)

removeDuplicateList(buah)

"""
    How to sorted list
"""
num_list = [1,2,4,6,8,4,3,5,78]
num_list.sort()
print(num_list)



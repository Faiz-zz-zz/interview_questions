def answer(array):
    select = []
    ind = 0
    oppo = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    while ind < len(array) - 1:
        if oppo[array[ind]] == array[ind + 1]:
            select = select + [0, 0]
            ind += 2
        else:
            select = select + [1]
            ind += 1
    return select if len(select) == len(array) else (select + [1])
print(answer(["NORTH", "SOUTH", "SOUTH", "SOUTH", "SOUTH", "NORTH"]))

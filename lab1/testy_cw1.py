def NAND(a, b):
    if a == 1 and b == 1:
        return 0
    return 1

def NAND3(a, b, c):
    if a == 1 and b == 1 and c == 1:
        return 0
    return 1


def B1(a1, a2, a3):
    return 1

def B2(a1, a2, a3):
    return 0

def B3(a1, a2, a3):
    return 0

def B4(a1, a2, a3):
    return 0

def B5(a1, a2, a3):
    gate4 = NAND(a1, a1)
    gate2 = NAND(gate4, a2)
    gate3 = NAND(a2, a3)
    gate1 = NAND(gate3, gate2)
    return gate1

def B6(a1, a2, a3):
    gate5 = NAND(a1, a2)
    gate4 = NAND(a2, a2)
    gate3 = NAND(a1, a1)
    gate2 = NAND(gate3, gate4)
    gate1 = NAND3(gate2, gate5, a3)
    return gate1

def B7(a1, a2, a3):
    gate4 = NAND(a2, a2)
    gate3 = NAND(a3, a3)
    gate2 = NAND(gate4, gate3)
    gate1 = NAND(gate2, gate2)
    return gate1

def B8(a1, a2, a3):
    gate5 = NAND(a3, a3)
    gate4 = NAND(a2, a2)
    gate3 = NAND(a1, a1)
    gate2 = NAND(gate3, gate4)
    gate1 = NAND(gate2, gate5)
    return gate1


def visualize(a1, a2, a3, cnt):
    Display = [[0 for _ in range(4)] for _ in range(4)]

    Display[0][0] = B1(a1, a2, a3)
    Display[0][3] = Display[0][0]
    Display[0][1] = B2(a1, a2, a3)
    Display[0][2] = Display[0][1]
    Display[1][0] = B3(a1, a2, a3)
    Display[1][3] = Display[1][0]
    Display[1][1] = B4(a1, a2, a3)
    Display[1][2] = Display[1][1]
    Display[2][0] = B5(a1, a2, a3)
    Display[2][3] = Display[2][0]
    Display[2][1] = B6(a1, a2, a3)
    Display[2][2] = Display[2][1]
    Display[3][0] = B7(a1, a2, a3)
    Display[3][3] = Display[3][0]
    Display[3][1] = B8(a1, a2, a3)
    Display[3][2] = Display[3][1]

    for i in range(4):
        for j in range(4):
            if Display[i][j] == 1:
                Display[i][j] = "O"
            else:
                Display[i][j] = "."

    for row in Display:
        for diode in row:
            print(diode, end=" ")
        print()


    print()
    print("Emotka nr: " + str(cnt))
    print()
    print()
    print()


def main():
    Emotes = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)] #binarna reprezentacja liczb od 0 do 7
    for a3, a2, a1 in Emotes:
        str_repr = f"{a3}{a2}{a1}"

        for i in range(1,9):
            func_name = f"B{i}"
            b_val = globals()[func_name](a1, a2, a3)
            str_repr = str(b_val) + str_repr

        print(str_repr)

main()

def solve():
    numbies = [1, 1]
    zum = 0
    while True:
        new_numbie = numbies[0] + numbies[1]
        numbies[1] = numbies[0]
        numbies[0] = new_numbie
        if new_numbie > 4000000:
            break
        elif new_numbie % 2 == 0:
            zum += new_numbie

    return zum


if __name__ == "__main__":
    print(solve())

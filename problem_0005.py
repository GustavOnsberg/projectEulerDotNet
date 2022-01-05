

def solve(n):
    zum = n
    can_return = False
    while not can_return:
        for x in range(n):
            if zum % (x + 1) != 0:
                can_return = False
                zum += n
                break
            can_return = True
    return zum



if __name__ == "__main__":
    print(solve(20))

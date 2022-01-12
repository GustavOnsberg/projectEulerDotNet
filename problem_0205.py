import random
import threading

p = 0
t = 0


def solve(n):
    global p
    global t

    while True:
        pete = 0
        total = 0

        while total < n:
            pyra = random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)
            pyra += random.randint(1, 4)

            cube = random.randint(1, 6)
            cube += random.randint(1, 6)
            cube += random.randint(1, 6)
            cube += random.randint(1, 6)
            cube += random.randint(1, 6)
            cube += random.randint(1, 6)

            if pyra > cube:
                pete += 1

            total += 1

        p += pete
        t += total

        print(f"{int(t / 1000000)}m: {p / t}")


def solve2():
    win = 0
    total = 0
    for p1 in range(1, 5):
        for p2 in range(1, 5):
            for p3 in range(1, 5):
                for p4 in range(1, 5):
                    print(f"{p1} {p2} {p3} {p4}")
                    for p5 in range(1, 5):
                        for p6 in range(1, 5):
                            for p7 in range(1, 5):
                                for p8 in range(1, 5):
                                    for p9 in range(1, 5):
                                        for c1 in range(1, 7):
                                            for c2 in range(1, 7):
                                                for c3 in range(1, 7):
                                                    for c4 in range(1, 7):
                                                        for c5 in range(1, 7):
                                                            for c6 in range(1, 7):
                                                                pete = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                                                                colin = c1 + c2 + c3 + c4 + c5 + c6
                                                                total += 1
                                                                if pete > colin:
                                                                    win += 1
    return win / total





if __name__ == "__main__":
    print(solve2())
    # for x in range(12):
    #     thread = threading.Thread(target=solve, args=(1000000,))
    #     thread.start()
    #     print("Thread started")

import random as r
try:
    x = r.choice(range(r.choice(range(r.randint(r.randint(0, 100), r.randint(0, 10000)), r.randint(r.randint(0, 10000), r.randint(0, 1000000000000))))))
    k = r.choice(range(r.choice(range(r.randint(r.randint(0, 100), r.randint(0, 10000)), r.randint(r.randint(0, 10000), r.randint(0, 1000000000000))))))
    ff = r.randint(0, 100000)
    tries = 0
    f = open(f"randoms_{ff}.txt", "x")
    f = open(f"randoms_{ff}.txt", "at")
    f.write(f"||X:{x}||==========START==========||K:{k}||\n")
    print(f"x: {x}\nk: {k}")

    while x != k:
        tries += 1
        x = r.choice(range(r.choice(range(r.randint(r.randint(0, 100), r.randint(101, 10000)), r.randint(r.randint(10001, 10000000), r.randint(10000001, 1000000000000))))))
        k = r.choice(range(r.choice(range(r.randint(r.randint(0, 100), r.randint(101, 10000)), r.randint(r.randint(10001, 10000000), r.randint(10000001, 1000000000000))))))
        f.write(f"T:{tries}, x:{x}, k:{k}\n")
        print(f"x: {x}\nk: {k}")

    print("Same, end")
    f.write(f"||TRIES:{tries}||==========END==========||VALUE:{x}||")
    f.close()

except KeyboardInterrupt as e:
    print(f"Stopping... x:{x}, k:{k}, tries:{tries}")
    f.write(f"||TRIES:{tries}||==========END==========||VALUE:{x}||")
    f.close()
    exit(code=0)

for xod in range(100, 334):
    x = xod // 100
    o = (xod // 10) % 10
    d = xod % 10

    if x == 0 or len({x, o, d}) != 3:
        continue
    mat = 3 * xod
    if not (100 <= mat <= 999):
        continue

    m = mat // 100
    a = (mat // 10) % 10
    t = mat % 10

    if m == 0 or len({m, a, t}) != 3:
        continue
    if {x, o, d} & {m, a, t}:
        continue

    print(f"{xod}+{xod}+{xod}={mat}")
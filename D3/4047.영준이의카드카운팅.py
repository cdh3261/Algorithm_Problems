for t in range(int(input())):
    s = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    cards = input()

    n = len(cards)
    a = set()
    for i in range(n//3):
        a.add(cards[3 * i:3 * i + 3])
        s[cards[3 * i]] += -1

    if len(a) != n//3:
        print(f'#{t+1} ERROR')
    else:
        print(f'#{t+1} {s["S"]} {s["D"]} {s["H"]} {s["C"]}')
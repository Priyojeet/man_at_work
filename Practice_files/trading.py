def solve(N, M, B, P, S):
    res = B

    # Find max proffit
    base = S[0]
    upgrade_cost = 0
    proffit_list = [(0, base)]

    for i in range(M - 1):
        upgrade_cost += P[i]
        proffit = S[i + 1] - upgrade_cost
        if proffit > base:
            proffit_list.append((upgrade_cost, proffit))

    proffit_list.sort(key=lambda x: x[1], reverse=True)
    mpc, mpv = proffit_list[0]
    # print(proffit_list)

    j = 0
    while (j < N):
        if res >= mpc:
            res += mpv * (N - j)
            break
        for c, v in proffit_list:
            if res >= c:
                res += v
                break

        j += 1

    return res


if __name__ == "__main__":
    N, M, B = map(int, input().split())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))

    res = solve(N, M, B, P, S)

    print(res)
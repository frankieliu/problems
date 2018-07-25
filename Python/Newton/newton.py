def newton(x0, eps, f, fp, maxIteration, answer, verbose=False):
    ans = x0
    y = f(ans)                                     # spark operator
    for i in range(maxIteration):
        dy = fp(ans)                               # java operator
        change = y/dy                              # python operator
        ans = ans - change
        y = f(ans)                                 # spark operator
        if (verbose):
            print(i, ans, y, change)               # python operator
        if (abs(y) < eps) or (abs(change) < eps):  # python operator
            break
    answer.append(ans)                             # java operator

if __name__ == "__main__":

    f = lambda x: x*2 - 4
    fp = lambda x: 2*x
    x0 = 10
    eps = 1e-7
    maxIteration = 100
    verbose = True
    answer = []

    newton(x0, eps, f, fp, maxIteration, answer, verbose=True)

    print(answer)

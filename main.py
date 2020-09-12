def fib_dynamic(n):
    cal_result = {}

    cal_result[0] = 1
    cal_result[1] = 1

    if n == 0 or n == 1:
        return 1

    for i in range(2, n+1):
        cal_result[i] = cal_result[i-1] + cal_result[i-2]

    return cal_result[n]


def fb(num):
    a, b = 1, 0
    for _ in range(num):
        print(_)
        a, b = a + b % 10000, a % 10000
    return b

if __name__ == "__main__":
    print(fb(20190324))

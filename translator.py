import sys


USAGE = "USAGE: python translator.py <number>"


def getnum():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        exitprogram(USAGE)


def exitprogram(message):
    print(message)
    sys.exit()


def translate(num, separator=3, pattern=','):
    ans = num[0:len(num) % 3]
    for i in range(len(ans), len(num), separator):
        if ans:
            ans += pattern
        ans += num[i:i+separator]
    return ans


def main():
    num = getnum()
    if not num.isdigit():
        print("Introduced value is not a number!")
        exitprogram(4*' ' + USAGE)

    num = str(int(num))

    num = translate(num)
    exitprogram(num)


if __name__ == "__main__":
    main()



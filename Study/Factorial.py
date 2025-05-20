#팩토리얼
def factorial_(n):
    global str_
    if (n == 1):
        str_ += str(1)
        return 1
    else:
        str_ += (str(n) + " * ")
        return n * factorial_(n - 1)

str_ = ""
num = int(input("입력할 숫자: "))
result = factorial_(num)
print("%s! : %s = %s" % (num, str_, result))
def palindrome(word):
    global stack
    word = word.lower().replace(' ', '')
    length = len(word)
    mid = length // 2

    # word의 절반을 Stack에 append해서 넣어둔다.
    for i in range (mid):
        stack.append(word[i])

    # word의 길이가 홀수일 경우, 가운데 글자를 건너뛴다.
    if length %2 != 0:
        mid += 1

    # 뒷부분과 스택에서 꺼낸 글자 비교
    for i in range(mid, length):
        if stack.pop() != word[i]: # 기러기가 입력값이면 '기'와 '기'비교
            return False
        return True


#초기값 초기화
SIZE = 200
stack = [None for _ in range(SIZE)]

if __name__ == "__main__":
    while True:
        word = input("문장을 입력해주세요(x 입력시 종료): ")
        if word == 'X' or word == 'x':
            break
        else:
            print("입력한 문장: ", word)
            print("회문을 검사합니다.\n")

            if palindrome(word): # 회문검사 후 결과값 출력
                print("문장 '%s' 은/는 회문입니다.\n" % word)
            else:
                print("문장 '%s' 은/는 회문이 아닙니다.\n" % word)

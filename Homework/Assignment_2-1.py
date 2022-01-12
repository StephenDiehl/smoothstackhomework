# 1

print("Hello World"[-3])


# 2

word = "thinker"

print(word[2:5])

# 3

s = 'hello'

# print(h[1]) this does nothing as H is not defined unless its just a typo and you meant

print(s[1])

S = 'Sammy'
print(S[2:])


# 4

print(set('Mississippi'))

# 5

def test(number, *phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in range(number):
        x = ''
        for item in phrase[i]:
            if item.lower() in alphabet:
                x += item.lower()
        y = x[::-1]
        if x == y:
            answer += "Y "
        else:
            answer += "N "
    print(answer)


test(3, 'Stars', 'O, a kak Uwakov lil vo kawu kakao!', 'Some men interpret nine memos')


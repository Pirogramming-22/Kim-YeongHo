# class NotPalindromeError(Exception):
#     def __init__(self):
#         super().__init__('회문이 아닙니다.')

def palindrome(word):
    wordReverse= ''.join(reversed(word))
    if(word != wordReverse):
        raise NotPalindromeError()
    else:
        print(f"{word}")




try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
class classreverse:
    def __init__(self,word_s):
        self.s=word_s
    def reverseword(self):
        return self.s[::-1]
word=input("enter the string to be reversed:")
revob=classreverse(word)
result=revob.reverseword()
print("reversed word:",result)
    
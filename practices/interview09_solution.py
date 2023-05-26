'''
    What will be print on screen ?
'''
class E(Exception):

    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return "Nice to see you"          # 2

try:
    print("Hello")                        # 1
    raise E("What a pity")
except Exception as e:
    print(e)
else:
    print("The show must go on !")


# Answer
'''
Hello
Nice to see you
'''
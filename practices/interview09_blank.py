'''
    What will be print on screen ?
'''
class E(Exception):

    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return "Nice to see you"

try:
    print("Hello")
    raise E("What a pity")
except Exception as e:
    print(e)
else:
    print("The show must go on !")



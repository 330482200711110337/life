from tqdm import tqdm

from JiSuanQi import App
from dairy import helper_dairy

class Mind:
    def __init__(self, can_do,answer):
        self.can_do=can_do
        self.answer=answer

    def welcome_user(self):
        print("What can I do for you?")

    def uper(self):
        self.welcome_user()
        for a in tqdm(self.can_do, '正在调取'):
            print(a)

    def inputer(self):
        if self.answer==1:
            jisuanqi = App()
        if self.answer==2:
            helper_dairy()


a_man=Mind(["-1退出，1计算器,2日记"],0)
a_man.uper()
while True:
    a_man.answer = int(input())
    if a_man.answer == -1:
        break
    else:
        a_man.inputer()

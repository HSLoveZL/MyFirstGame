# coding=utf-8
from random import randint
number = randint(1, 10)
print '---------------Hello,this is my first game!---------------'
temp = input("不妨猜猜我是哪个数字:")
guess = int(temp)

if guess == number:
    print '我勒个去，这都被你猜中了！'
else:
    print '不好意思，猜错啦！'
print '游戏结束，洗洗睡吧！'

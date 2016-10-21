# coding=utf-8
print '---------------Hello,this is my first game!---------------'
temp = input("不妨猜猜我是哪个数字:")
guess = int(temp)

if guess == 6:
    print '我勒个去，这都被你猜中了！'
else:
    print '不好意思，猜错啦！'
print '游戏结束，洗洗睡吧！'

import random
#生成随机数，0至100之间的整数
num=random.randint(0,100)
print('系统已生成一个0-100之间的随机整数。\n')
#定义最小值
startnum=0
#定义最大值
endnum=100
#无效猜测的次数
errornum= 0
#有效数字猜测次数
count=0
while True:
   try:
     inputnum=int(input('请输入一个你认为等于这个随机整数的数字,范围'+str(startnum)+'至'+str(endnum)+'：'))
   except:
     #产生报错，无效猜测，比如输入了英文字母等。
     errornum+=1
     print('输入的数值不在要求范围，请重新输入.\n')
     continue
    #判断是否在最小值和最大值之间
   if inputnum in range(startnum,endnum+1):
       count +=1
       #猜中情况下，显示猜测的次数
       if inputnum == num:
           print('恭喜你，猜对了，有效猜测'+str(count)+'次，无效数据'+str(errornum)+'次')
           break
       #如果输入的数值比需要猜的数字小，则更新最小值
       elif inputnum in range(startnum,num):
           startnum = inputnum
           continue
       #如果输入的数值比需要猜的数字大，更新最大值。
       else:
           endnum = inputnum
           continue
   #超出猜测范围的无效猜测
   else:
      errornum += 1
      print('输入的数值不在要求范围，请重新输入.')
      continue


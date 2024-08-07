x,y=map(int,input().split())
loss=x-y
loss_per=(loss*100)/x
print("{:.2f}".format(loss_per))
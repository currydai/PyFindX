while(True):
    data_input = int(input("请输入100-1000质数:"))
    dai1 = int(input("请输入定数1质数:"))
    dai2 = int(input("请输入定数2质数:"))
    errorbar = float(input("请输入误差(小数：例如0.00000001):"))

    if(data_input>100 and data_input<1000):
        a_list=[i for i in range(20,100,1)]
        b_list=[i for i in range(20,100,1)]
        c_list=[i for i in range(20,100,1)]
        d_list=[i for i in range(20,100,1)]

        m_list = []
        m_list.append(dai1)
        m_list.append(dai2)

        result=[]
        for a in a_list:
            for b in b_list:
                for c in c_list:
                    for d in d_list:
                        for m in m_list:
                            x = (b*d*m)/(a*c)-data_input
                            if(x==0):
                                pass
                            else:
                                y = 1.0/x
                                yushu = y%1.0-0
                                if(yushu < errorbar):
                                    if(y>5 and y<50 ):
                                        print('输入质数：%s,解为：a=%s,b=%s,c=%s,d=%s,m=%s,x=%s,y=%s,yushu=%s'%(data_input,a,b,c,d,m,x,y,yushu))
                                        result.append(int(y))
                                    if(y>-50 and y<-5 ):
                                        print('输入质数：%s,解为：a=%s,b=%s,c=%s,d=%s,m=%s,x=%s,y=%s,yushu=%s'%(data_input,a,b,c,d,m,x,y,yushu))
                                        result.append(int(y))
        break
if(len(result)<1):
    print('计算完成，无解')
else:
    print('计算完成，x=1/%s'%set(result))
input('程序执行成功，按任意键退出：')








def num(): #for taking spent amout
   i=0
   num=[]
   close=False
   while not close:
       name=input("enter expenditure amount:")
       if name=="done":
           close=True
           break   
       name=int(name)
       num.append(name)

   return num

def add(): #for adding amout particulary for each roomamtes
   numb=num()
   total=0
   for i in range(len(numb)):
       total +=numb[i]
   return total
def rmt_no_2():  #for calculating average spent of each roomates
    rm1=input("enter roommate name please :")
    name1=add()
    print(f"expedeture done by {rm1}={name1}")
    rm2=input("enter roommate name please :")
    name2=add()
    print(f"expedeture done by {rm2}={name2}")
    avg=(name1+name2)/2
    print(f"averae expenditure is {avg}")
    print(f"{rm1} has to give or take :")
    print(avg-name1)
    print(f"{rm2} has to give or take :")
    print(avg-name2)

def rmt_no_3(): #for calculating average spent of each roomates

    rm1=input("enter roommate name please :")
    name1=add()
    print(f"expedeture done by {rm1}={name1}")
    rm2=input("enter roommate name please :")
    name2=add()
    print(f"expedeture done by {rm2}={name2}")
    rm3=input("enter roommate name please :")
    name3=add()
    print(f"expedeture done by {rm3}={name3}")

    avg=(name1+name2+name3)/3
    print(f"averae expenditure is {avg}")
    print(f"{rm1} has to give or take :")
    print(avg-name1)
    print(f"{rm2} has to give or take :")
    print(avg-name2)
    print(f"{rm3} has to give or take :")
    print(avg-name3)
def rmt_no_4(): #for calculating average spent of each roomates
    rm1=input("enter roommate name please :")
    name1=add()
    print(f"expedeture done by {rm1}={name1}")
    rm2=input("enter roommate name please :")
    name2=add()
    print(f"expedeture done by {rm2}={name2}")
    rm3=input("enter roommate name please :")
    name3=add()
    print(f"expedeture done by {rm3}={name3}")
    rm4=input("enter roommate name please :")
    name4=add()
    print(f"expedeture done by {rm4}={name4}")
    avg=(name1+name2+name3+name4)/4
    print(f"averae expenditure is {avg}")
    print(f"{rm1} has to give or take :")
    print(avg-name1)
    print(f"{rm2} has to give or take :")
    print(avg-name2)
    print(f"{rm3} has to give or take :")
    print(avg-name3)
    print(f"{rm4} has to give or take :")
    print(avg-name4)
def rmt_no_5(): #for calculating average spent of each roomates
    rm1=input("enter roommate name please :")
    name1=add()
    print(f"expedeture done by {rm1}={name1}")
    rm2=input("enter roommate name please :")
    name2=add()
    print(f"expedeture done by {rm2}={name2}")
    rm3=input("enter roommate name please :")
    name3=add()
    print(f"expedeture done by {rm3}={name3}")
    rm4=input("enter roommate name please :")
    name4=add()
    print(f"expedeture done by {rm4}={name4}")
    rm5=input("enter roommate name please :")
    name5=add()
    print(f"expedeture done by {rm5}={name5}")
    avg=(name1+name2+name3+name4+name5)/5
    print(f"averae expenditure is {avg}")
    print(f"{rm1} has to give or take :")
    print(avg-name1)
    print(f"{rm2} has to give or take :")
    print(avg-name2)
    print(f"{rm3} has to give or take :")
    print(avg-name3)
    print(f"{rm4} has to give or take :")
    print(avg-name4)
    print(f"{rm5} has to give or take :")
    print(avg-name5)
    print("plese enter exit")

n=int(input("enter number of roomates"))

if n==2:
   print(rmt_no_2())
elif n==3:
   print(rmt_no_3())
elif n==4:
   print(rmt_no_4())
elif n==5:
   print(rmt_no_5())
v=input("please enter 'x' for exit :")
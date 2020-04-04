print("welcome to blood bank")
name=[]
hospital=[]
bloodgrp=[]
import array as details
details=[[name],[hospital],[bloodgrp]]
n=int(input('enter number of patients :'))
for n in range(0,n):
     a=input("will you donate or collect the blood? (donate/accept) : ")
     if(a=="donate"):
          name.append(input("enter your name please :"))
          hospital.append(input("Enter your name of hospital :"))
          bloodgrp.append(input("Enter your blood group :"))
     if(a=="accept"):
           name.append(input("enter your name please :"))
           hospital.append(input("Enter your name of hospital :"))
           bloodgrp.append(input("Enter your blood group you want :"))
     if (bloodgrp=='O-'):
             print('you have rare blood group')
print(details)     
dict={'a':name,'b':hospital,'c':bloodgrp}   
print(dict[input('enter a or b or c to get information about names or hospitals or bloodgroups : ')])
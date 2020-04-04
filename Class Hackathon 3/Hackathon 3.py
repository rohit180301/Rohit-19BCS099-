import xlrd
import os
rs = xlrd.open_workbook("C:\\Users\\Rohit Sagar Shinde\\Desktop\\CurrencyDataFile.xlsx")
sheet = rs.sheet_by_index(0)
sheet.cell_value(0,0)
# Taking inputs from the user :
k=int(input("Enter the number of question papers required :"))
n=int(input("Enter the Question paper number that you want to display on desktop : "))
os.chdir("C:\\Users\\Rohit Sagar Shinde\\Desktop")
ans=open("Answerkey.txt",'w')
que=open("questionpaper.txt",'w')
for i in range(1,k+1):
    if(i==n):
        l=int(input("Enter the number of questions that you want in entered question paper : "))
        f=1
        for s in range(i,(l*l)+1,l):
            que.write(str(f)+": What is the symbol of "+str(sheet.cell_value(s,1))+"?"+"\n"+"A:"+""+str(sheet.cell_value(s-1,2))+"\n"+"B:"+""+str(sheet.cell_value(s,2))+"\n"+"C:"+""+str(sheet.cell_value(s+1,2))+"\n")
            f=f+1
        a=1
        for j in range(i,(l*l)+1,l):
            ans.write(str(a)+":"+str(sheet.cell_value(j,2))+"\n")
            a=a+1
ans.close()
print("Entered question paper is : ")
que=open("Questionpaper.txt","r")
print(que.read())
print("Answer key of the entered question paper is : ")
ans=open("Answerkey.txt","r")
print(ans.read())            


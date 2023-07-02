class consolidatedfunction():
    def Subfields():
        print('''
        Sub-fields in AI are:
        Machine Learning
        Neural Networks
        Vision
        Robotics
        Speech Processing
        Natural Language Processing''')
    def fields():
        print("Sub-fields in AI are:")
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for i in list:
            print(i)
    def oddeven():
        num=int(input("Enter the number to check Odd/even:"))
        if((num%2)==1):
            print(num,"is Odd Number")
        else:
            print(num,"is Even Number")
    def Eligible():
        gender=input("Your gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")
        elif(gender=="Female"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")
        else:
            print("Invalid input")
            
    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        Total=S1+S2+S3+S4+S5
        print("Total:",Total)
        percent=(Total/500)*100
        print("Percentage:",percent)    
            
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area Formula:(Height*Breadth)/2 ")
        Area=(Height*Breadth)/2
        print("Area of Triangle:",Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth1:"))
        Perimeter=(Height1+Height2+Breadth1)
        print("Perimeter formula:Height1+Height2+Breadth1")
        print("Perimeter of triangle:",Perimeter)        
            
            
            
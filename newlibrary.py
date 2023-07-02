class multiplefunctions(): #Class
    def BMI():  #Function 1
        Index=int(input("Enter Index Value:"))
        if(Index<18):
            print("Underweight")
            message="Yes,Underweight"
        elif(Index<24):
            print("Normal")
            message="Yes,Normal"
        elif(Index<29):
            print("Overweight")
            message="Yes,Overweight"
        elif(Index<34):
            print("Obese")
            message="Yes,Obese"
        else:
            print("Extremely Obese")
            message="Yes,Extremely Obese"
        return message
    
    def oddeven():  #Function 2
        num=int(input("Enter the number to check Odd/even:"))
        if((num%2)==1):
            print("Odd Number")
            message="Odd No"
        else:
            print("Even Number")
            message="Even No"
        return message
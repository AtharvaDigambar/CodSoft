print("\n**** THE CALCULATOR ****")
while(True):
    num1=int(input("Enter the first number "))
    num2=int(input("Enter the secound number "))
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
    choice=int(input("Select the option which you want to perform 1,2,3,4,5\n"))
    #Addition
    if choice==1:
        sum=num1+num2
        print("The sum of ",num1," and ",num2 , "is ",sum)
        break;

    #Substraction
    elif choice==2:
        sub=num1-num2
        print("The substraction of ",num1," and ",num2 , "is ",sub)
        break;
            

    #Multiplication
    elif choice==3:
        mul=num1*num2
        print("The Multiplication of ",num1," and ",num2 , "is ",mul)
        break;
            
    #Division
    elif choice==4:
        div=num1/num2
        print("The Division of ",num1," and ",num2 , "is ",div)
        break;
    
    elif choice==5:
        break;

    #Error if wrong choice
    else:
        print("Sorry!! You have entered wrong choice")
        break;
    print("\n**** THANK FOR USING CALCULATOR ****\n")
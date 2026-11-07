def calculater():
    num1=float(input("Enter you first number: "))
    num2=float(input("Enter your second number: "))

    operation=input("Choose operation (+,-,*,/): ")

    if operation=="+":
       result=num1+num2
       print("Result: ",result)

    elif operation=="-":
      result=num1-num2
      print("Result: ",result)    

    elif operation =="*":
      result=num1*num2
      print("Result: ",result)

    elif operation=="/":
      result=num1/num2
      print("Result: ",result)

    else :
     print("invalid operation")

calculater()        
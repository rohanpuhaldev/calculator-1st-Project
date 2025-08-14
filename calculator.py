while True:
     try:
       a = float(input("Enter number 1 : "))
       b = float(input("Enter number 2 : "))
     except ValueError:
      print("Please enter only DIGITS!")
      continue
   
     print("Pick any operation")
     print("Addition(1)")
     print("Subtraction(2)")
     print("Multiplication(3)")
     print("Division(4)")
     print("Power[b](5)")
     print("Average(6)")
  
     choice = input("Select[1/2/3/4/5/6] : ")
  
     if choice == "1":
        result = a+b
    
     elif choice == "2":
        result = a-b

     elif choice == "3":
        result = a*b
    
     elif choice == "4":
       if b!=0:
         result = f"{a}/{b} = {a/b} | Remainder = {a%b}"
       else:
          result = print("Error! Divding by 0")

     elif choice == "5":
       result = a**b

     elif choice == "6":
        result = (a+b)/2
      
     else:
       print("Error! Invalid operation")
       continue
     
   
     print("Result:",result)

     yes = input("Do you want to continue?[y/n] : ").upper()
  
     if yes == "Y":
        import time
        print("Requesting..........................")
        time.sleep(.2)
        print("=====================================================================================")


     else:
        import time

        print("Requesting..........................")
        time.sleep(.3)
        print("Request is accepted.")
        time.sleep(.4)
        print("Task is completed!")
        time.sleep(.46)
        print("Thanks! For utilizing me,")
        time.sleep(.49)
        print("Have a good day!")
        break

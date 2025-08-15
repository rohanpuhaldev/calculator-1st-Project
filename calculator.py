while True:
     try:
       a = input("Enter number 1 or [exit] : ")
       if a.upper() == "EXIT":
          break 
       a = float(a)

       b = input("Enter number 2 or [exit]: ")
       if b.upper() == "EXIT":
          break
       b = float(b)
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
     print("Percentage(7)")
  
     choice = input("Select[1/2/3/4/5/6/7] : ")
  
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

     elif choice == "7":
        result = (a/100)*b
      
     else:
       print("Error! Invalid operation")
       continue
     
   
     print("Result:",result)
     

     yes = input("Do you want to continue?[y/n] : ").upper()
  
     if yes == "Y":
        import time
        print("───────────────────────────────────────────────────────────────────")
        print("Requesting.........................................................")
        time.sleep(.2)
        print("Request is accepted")
        time.sleep(.06)
        print("───────────────────────────────────────────────────────────────────")


     else:
        import time

        print("Requesting..........................")
        time.sleep(.1)
        print("Request is accepted.")
        time.sleep(.17)
        print("Task is completed!")
        time.sleep(.18)
        print("Thanks! For utilizing me,")
        time.sleep(.18)
        print("Have a good day!")
        break

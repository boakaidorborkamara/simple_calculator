def calculate_numbers():

    #get first numbers from user
    num1 = int(input("Enter first number \n"))


    #acceptable operators
    operators = ["+", "-", "/", "*", "%"]


    #prompt user to select a valid operator
    print("Select an operator")
    selected_operator = (input("+,-,/,*,% \n"))
    while(selected_operator not in operators):
        #keep prompting until a valid operator is enter
        selected_operator = (input("+,-,/,*,% \n")) 


    #get second number
    num2 = int(input("Enter first number \n"))


    #execute operations base on selected operator
    

    


# call calculator function 
calculate_numbers()

num_1 =int(input("Enter first number :"))
num_2 =int(input("Enter second number :"))
operator =input("Enter your operator of choice :")


match operator:
    case "+":
        print("{} + {} =".format(num_1,num_2))
        print(num_1 + num_2)
    case "-":
        print("{} - {} =".format(num_1,num_2))
        print(num_1 - num_2)
    case "*":
        print(" {} * {} =".format(num_1,num_2))
        print(num_1 * num_2)
    case "/":
        print("{} / {} =".format(num_1,num_2))
        print(num_1 / num_2)
    
        
        

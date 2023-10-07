import sys
operation = sys.argv[1]
operand1 = int(sys.argv[2])
operand2 = int(sys.argv[3])
if operation=="add":
    print(operand1+operand2)
elif operation=="sub":
    print(operand1-operand2)
elif operation=="multiple":
    print(operand1*operand2)
elif operation=="Division":
    print(operand1/operand2)
else:
    print("invalid")    
    

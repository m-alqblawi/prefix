from Stack import Stack
def infixToPostfix(infixexpr):
    prec = {}

    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    postfixList = []

    tokenList = infixexpr.split() # default seperator is white space

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else :
            # Don't swap the conditions
            #while (prec[opStack.peek()] >= prec[token]) and (not opStack.isEmpty()):
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                    postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty(): # aligned to for-loop
        postfixList.append(opStack.pop())
                                
    return " ".join(postfixList)# Here, seperator is space



print(infixToPostfix("A + B * C"))
print(infixToPostfix("A * B + ( C / D - E ) + F"))
print(infixToPostfix("( A + B ) * C"))
print(infixToPostfix("A / ( B * C + D ) * E ^ 2"))


print(infixToPostfix("A+B*C")) # without spaces

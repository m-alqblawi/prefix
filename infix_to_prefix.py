from Stack import Stack

def infixToPrefix(infixExpr):
    precedence = {}
    precedence["^"] = 4
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence[")"] = 1     # in postfix (

    opStack = Stack()
    prefixList = []

    tokenList = infixExpr.split() # convert str ("A + B * C") to list [A, +, B ,* ,C]
    tokenList.reverse()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":   # D * ) C + B ( / A
            prefixList.append(token)
        elif token == ')':
            opStack.push(token)
        elif token == "(":
            topToken = opStack.pop()
            while topToken != ')':
                prefixList.append(topToken)
                topToken = opStack.pop()
        else:  # token is operator
            while (not opStack.isEmpty()) and (precedence[opStack.peek()] > precedence[token]):
                prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())

    prefixList.reverse()
    return " ".join(prefixList)  # join invers split()
# =============================================================


def doMath (op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "^":
        return op1**op2
    else:
        return op1 - op2


def preFixEvaluate(PreFixExpr): # * / 1 + 2 3 4   = > 4 3 2 + 1 / *
    operandStack = Stack()
    tokenList = PreFixExpr.split()
    tokenList.reverse()

    for token in tokenList:
        if token in "*/-+^":
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
        else:
            operandStack.push(float(token))  # [4 3 2]
    return operandStack.pop()





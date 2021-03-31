from Stack import Stack


def infixToPostfix(infixExpr):
    precedence = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack = Stack()
    postfixList = []

    tokenList = infixExpr.split()  # convert str "A + B * C" to list [A, +, B ,* ,C]

    # A + B * ( C / D – E ) + F
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:  # token is operator
            while (not opStack.isEmpty()) and (precedence[opStack.peek()] >= precedence[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)  # join invers split()
    # [A, +, B ,* ,C] = > A B C + -


# =============================================================
def doMath(op, op1, op2): # + , 2 , 3
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "^":
        return op1 ** op2
    else:
        return op1 - op2


def postFixEvaluate(PostFixExpr): # A B C + * = >     ^ *
    operandStack = Stack()
    tokenList = PostFixExpr.split()

    for token in tokenList:
        if token in "*/-+^": # 1 2 3 + / 4 *
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

        else:
            operandStack.push(float(token)) # 1 2 3

    return operandStack.pop()

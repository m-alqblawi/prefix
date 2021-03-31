from infix_to_postfix import infixToPostfix, postFixEvaluate
from infix_to_prefix import infixToPrefix, preFixEvaluate

A = 1
B = 2  
C = 3  
D = 4  
E = 5  
F = 6
G = 7
H = 8
I = 9
J = 10
K = 11
print("=====" * 30)
print(f"Infix: A * B / C  => {A*B/C}")
print("Postfix: ", infixToPostfix("A * B / C"), " => ", postFixEvaluate("1 2 * 3 /"))
print("Prefix: ", infixToPrefix("A * B / C"), " => ", preFixEvaluate("* 1 / 2 3"))
print("=====" * 30)

print(f"Infix: A + B * C  => {A+B*C}")
print("Postfix: ", infixToPostfix("A + B * C"), " => ", postFixEvaluate("1 2 3 * +"))
print("Prefix: ", infixToPrefix("A + B * C"), " => ", preFixEvaluate("+ 1 * 2 3"))
print("=====" * 30)

print(f"Infix: A * B + ( C / D - E ) + F  => {A * B + ( C / D - E ) + F}")
print("Postfix: ", infixToPostfix("A * B + ( C / D - E ) + F"), " => ", postFixEvaluate("1 2 * 3 4 / 5 - + 6 +"))
print("Prefix: ", infixToPrefix("A * B + ( C / D - E ) + F"), " => ", preFixEvaluate("+ * 1 2 + - / 3 4 5 6"))
print("=====" * 30)

print(f"Infix: ( A + B ) * C  => {( A + B ) * C}")
print("Postfix: ", infixToPostfix("( A + B ) * C"), " => ", postFixEvaluate("1 2 + 3 *"))
print("Prefix: ", infixToPrefix("( A + B ) * C"), " => ", preFixEvaluate("* + 1 2 3"))
print("=====" * 30)

print(f"Infix: A / ( B * C + D ) * E ^ 2  => {A / ( B * C + D ) * E**2}")
print("Postfix: ", infixToPostfix("A / ( B * C + D ) * E ^ 2"), " => ", postFixEvaluate("1 2 3 * 4 + / 5 2 ^ *"))
print("Prefix: ", infixToPrefix("A / ( B * C + D ) * E ^ 2"), " => ", preFixEvaluate("* / 1 + * 2 3 4 ^ 5 2"))
print("=====" * 30)

print(f"Infix: ( A + B ) * ( C - D )   => {( A + B ) * ( C - D )}")
print("Postfix: ", infixToPostfix("( A + B ) * ( C - D )"), " => ", postFixEvaluate("1 2 + 3 4 - *"))
print("Prefix: ", infixToPrefix("( A + B ) * ( C - D )"), " => ", preFixEvaluate("* + 1 2 - 3 4"))
print("=====" * 30)

print(f"Infix: D / ( A + B * C )   => {D / ( A + B * C )}")
print("Postfix: ", infixToPostfix("D / ( A + B * C )"), " => ", postFixEvaluate("4 1 2 3 * + /"))
print("Prefix: ", infixToPrefix("D / ( A + B * C )"), " => ", preFixEvaluate("/ 4 + 1 * 2 3"))
print("=====" * 30)

print(f"Infix: A / B * C * A   => {A / B * C * A}")
print("Postfix: ", infixToPostfix("A / B * C * A"), " => ", postFixEvaluate("1 2 / 3 * 1 *"))
print("Prefix: ", infixToPrefix("A / B * C * A"), " => ", preFixEvaluate("* * / 1 2 3 1"))
print("=====" * 30)

print(f"Infix: A + B - C * D + ( E ^ F ) * G / H / I * J + K    => {A + B - C * D + ( E ** F ) * G / H / I * J + K}")
print("Postfix: ", infixToPostfix("A + B - C * D + ( E ^ F ) * G / H / I * J + K"), " => ", postFixEvaluate("1 2 + 3 4 * - 5 6 ^ 7 * 8 / 9 / 10 * + 11 +"))
print("Prefix: ", infixToPrefix("A + B - C * D + ( E ^ F ) * G / H / I * J + K"), " => ", preFixEvaluate("+ + - + 1 2 * 3 4 * / / * ^ 5 6 7 8 9 10 11"))
print("=====" * 30)



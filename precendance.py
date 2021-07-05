# x = 5 * 6 + (4 -3)
#  = 30 + 1 = 31

'''
Category	        Operator	        Associativity

Postfix	            () []           	Left to right
Multiplicative  	* / %	            Left to right
Additive	        + -	                Left to right
Shift	            << >>	            Left to right
Relational	        < <= > >=	        Left to right
Equality	        == !=	            Left to right
Bitwise AND	            &	            Left to right
Bitwise XOR	            ^	            Left to right
Bitwise OR	            |	            Left to right
Assignment	        = += -= *= /= %=>>= <<= &= ^= |=	Right to left
Comma	                    ,	                Left to right
'''

x = 6
x += (4*6) + 5 / (4-8) % 2
print(x)

# print((5 / (-4))%2)
# print()

# 6 += 24 + 5 / -4 % 2

# 6 += 24 + (-1.25) % 2
# 6 += 24 + 0.75
# 6 += 24.75
# 24.75 + 6 = 30.75

x = 3
y = 3
# We declare the argument as a list instead of a  variable .
R = [0]

# This is a function for adding two numbers
def sum(x,y,R):
    R[0] = x+y

sum(x,y,R)

print("the resultat is : ",R[0])


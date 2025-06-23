import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constants:
#   pi: mathematical constant π (circumference to diameter ratio)
#   catalan: Catalan's constant G (mathematical constant)
pi = mp.pi
catalan = mp.catalan

# Compute the expression: 4 * π * G
# Where G is interpreted as the Catalan constant
result = 4 * pi * catalan

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
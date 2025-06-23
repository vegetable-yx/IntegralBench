import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the mathematical constant pi
# Assign the value of pi to the result variable
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
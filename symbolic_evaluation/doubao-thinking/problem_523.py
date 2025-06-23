import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2 using mpmath
result = mp.log(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
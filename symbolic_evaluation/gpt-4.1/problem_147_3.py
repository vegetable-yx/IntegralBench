import mpmath as mp

# Set internal decimal places of precision to 15
mp.dps = 15

# Assign the constant π to the variable 'result'
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
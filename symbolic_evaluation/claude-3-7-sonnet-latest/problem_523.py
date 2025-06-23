import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute natural logarithm of 2 using mpmath
result = mp.log(2)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
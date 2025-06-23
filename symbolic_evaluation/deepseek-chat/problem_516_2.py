import mpmath as mp

# Set decimal places of precision to 15 for intermediate calculations
mp.dps = 15

# Define the constant for which we compute the natural logarithm
x = mp.mpf(2)

# Compute natural logarithm of 2 using mpmath's log function
result = mp.log(x)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
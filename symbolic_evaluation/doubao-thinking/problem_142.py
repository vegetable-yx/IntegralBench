import mpmath as mp
mp.dps = 15

# Compute the hyperbolic sine integral of 2
shi_2 = mp.shi(2)

# Calculate the final result by dividing by 2
result = shi_2 / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
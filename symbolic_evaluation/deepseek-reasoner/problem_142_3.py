import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate hyperbolic sine integral of 2
shi_value = mp.shi(2)

# Multiply by 1/2 to get final result
result = 0.5 * shi_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
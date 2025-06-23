import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the hyperbolic sine integral Shi(2)
shi_value = mp.shi(2)

# Divide by 2 to get the final result
result = shi_value / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
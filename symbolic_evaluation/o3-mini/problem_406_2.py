import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# Calculate the argument for the inverse sine function
numerator = mp.sqrt(3) - 1  # Compute √3 and subtract 1
arg = numerator / 2          # Divide by 2 to get (√3 - 1)/2

# Compute the inverse sine (arcsine) of the argument
asin_val = mp.asin(arg)

# Multiply the result by 2
result = 2 * asin_val

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))
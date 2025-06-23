import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the numerator: 13 * pi
numerator = 13 * mp.pi

# Calculate the fourth root of 3: 3^(1/4)
root3 = mp.root(3, 4)

# Calculate the denominator: 6 * root3
denominator = 6 * root3

# Compute the result: numerator / denominator
result = numerator / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the sine integral at 3: Si(3)
si_val = mp.si(3)

# Retrieve Catalan's constant
catalan = mp.catalan

# Compute the result: Si(3) * Catalan's constant
result = si_val * catalan

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
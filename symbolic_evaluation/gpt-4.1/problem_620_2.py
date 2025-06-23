import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi/8 * ln(2)
term1 = (mp.pi / 8) * mp.log(2)

# Get Catalan's constant
catalan = mp.catalan

# Combine the terms: result = (pi/8)*ln(2) - G
result = term1 - catalan

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
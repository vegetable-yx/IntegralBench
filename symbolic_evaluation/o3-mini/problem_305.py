import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the golden ratio and related constants
a = (mp.sqrt(5) + 1) / 2  # (√5 + 1)/2
b = (mp.sqrt(5) - 1) / 2  # (√5 - 1)/2

# Calculate natural logarithm of the golden ratio
ln_a = mp.log(a)

# Compute the squared logarithm term
term1 = ln_a ** 2

# Compute the logarithmic term multiplied by -2π
term2 = -2 * mp.pi * ln_a

# Calculate dilogarithm terms
# Note: (1 - √5)/2 = -b, and (√5 - 1)/2 = b
term3 = 4 * mp.polylog(2, -b)  # 4 * Li₂((1 - √5)/2)
term4 = -4 * mp.polylog(2, b)  # -4 * Li₂((√5 - 1)/2)

# Combine all terms and divide by 8
result = (term1 + term2 + term3 + term4) / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
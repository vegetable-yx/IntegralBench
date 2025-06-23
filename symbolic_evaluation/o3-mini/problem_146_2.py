import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 4th power
gamma_fourth = gamma_val**4

# Compute the denominator: 16 * sqrt(2*pi)
denominator = 16 * mp.sqrt(2 * mp.pi)

# Divide numerator by denominator
result = gamma_fourth / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))
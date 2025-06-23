import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise the result to the 4th power
gamma_power = gamma_val**4

# Divide by 32
result = gamma_power / 32

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp
mp.dps = 15

# Compute Gamma(1/4) using mpmath's gamma function
gamma_value = mp.gamma(mp.mpf(1)/4)

# Raise the gamma value to the 4th power
gamma_power = gamma_value ** 4

# Divide by 64 to get the final result
result = gamma_power / 64

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
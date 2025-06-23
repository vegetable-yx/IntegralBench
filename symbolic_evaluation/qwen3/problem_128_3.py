import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 2^(3/4) using mpmath power function
two_power = mp.power(2, mp.mpf(3)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate Gamma(5/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Combine components to compute the final result
numerator = two_power * sqrt_pi * gamma_3_4
result = numerator / gamma_5_4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
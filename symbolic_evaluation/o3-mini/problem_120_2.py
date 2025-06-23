import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Compute pi squared
pi_sq = mp.pi**2

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the denominator: 2560 * sqrt(2) * pi^2
denominator = 2560 * sqrt2 * pi_sq

# Divide gamma_power by denominator to get the result
result = gamma_power / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
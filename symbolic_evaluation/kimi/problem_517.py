import mpmath as mp
mp.dps = 15

# Calculate the exponent term 1/8
exponent = mp.mpf(1)/8

# Compute e^(1/8) using mpmath exponential
e_power = mp.exp(exponent)

# Calculate sqrt(π/2) using mpmath constants and sqrt
sqrt_pi_half = mp.sqrt(mp.pi/2)

# Multiply components to get final result
result = e_power * sqrt_pi_half

print(mp.nstr(result, n=10))
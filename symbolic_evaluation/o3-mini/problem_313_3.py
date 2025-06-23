import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 8th power
gamma_power = gamma_val**8

# Compute pi^4 and pi^3
pi = mp.pi
pi4 = pi**4
pi3 = pi**3

# Calculate the numerator: Γ(1/4)^8 + 64π^4
numerator = gamma_power + 64 * pi4

# Calculate the denominator: 512π^3
denominator = 512 * pi3

# Final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Calculate sqrt(2 * pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Divide by 2 to get sqrt(2*pi)/2
divided_term = sqrt_2pi / 2

# Calculate exponential term e^(1/8)
exp_term = mp.exp(1/8)

# Multiply the two terms to get the final result
result = divided_term * exp_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
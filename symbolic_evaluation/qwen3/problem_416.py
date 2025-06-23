import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate e^(π/4)
exp_pi_over_4 = mp.exp(pi_over_4)

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate numerator: sqrt(2) * e^(π/4) - 1
numerator = sqrt_2 * exp_pi_over_4 - 1

# Calculate final result by dividing numerator by 2
result = numerator / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp
mp.dps = 15

# Calculate pi divided by 4
pi_over_4 = mp.pi / 4

# Compute e^(pi/4)
exp_pi_over_4 = mp.exp(pi_over_4)

# Compute square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate the numerator: sqrt(2) * e^(pi/4) - 1
numerator = sqrt_2 * exp_pi_over_4 - 1

# Divide by 2 to get the final result
result = numerator / 2

print(mp.nstr(result, n=10))
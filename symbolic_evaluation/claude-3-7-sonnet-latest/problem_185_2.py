import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi^(3/2) = pi * sqrt(pi)
pi_val = mp.pi
sqrt_pi = mp.sqrt(pi_val)  # Compute square root of pi
pi_power = pi_val * sqrt_pi  # pi^(3/2)

# Calculate the factor (3 - sqrt(8))
sqrt8 = mp.sqrt(8)  # Compute square root of 8
factor = 3 - sqrt8  # (3 - sqrt(8))

# Multiply pi^(3/2) by the factor
numerator = pi_power * factor

# Divide by 2 to get the final result
result = numerator / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
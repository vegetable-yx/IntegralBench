import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Compute π cubed
pi_cubed = pi_val ** 3

# Divide by 24 to obtain the result
result = pi_cubed / 24

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
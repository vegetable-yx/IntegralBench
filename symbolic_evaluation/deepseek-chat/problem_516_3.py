import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) using mpmath's constant
pi_value = mp.pi

# Divide π by 2
half_pi = pi_value / 2

# Subtract 1 from π/2
result = half_pi - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
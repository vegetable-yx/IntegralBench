import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Divide pi by 2 to get π/2
half_pi = pi_val / 2

# Apply negative sign to obtain -π/2
result = -half_pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
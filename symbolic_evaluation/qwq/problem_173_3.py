import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 576 to get final result
result = pi_cubed / 576

print(mp.nstr(result, n=10))
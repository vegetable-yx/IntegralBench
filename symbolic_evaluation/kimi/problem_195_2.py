import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant 2 as an mpmath floating-point number
two = mp.mpf(2)

# Compute π/2 using mpmath's pi constant
half_pi = mp.pi / 2

# Subtract π/2 from 2 to get the result
result = two - half_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
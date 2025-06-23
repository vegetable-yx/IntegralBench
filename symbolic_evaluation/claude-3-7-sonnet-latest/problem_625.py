import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute π/2 using mpmath's constant for pi
result = mp.pi / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
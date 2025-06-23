import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the trilogarithm term Li_3(1/4)
trilog_term = mp.polylog(3, 1/4)

# Multiply by π and divide by 8
pi = mp.pi
result = (pi * trilog_term) / 8

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))
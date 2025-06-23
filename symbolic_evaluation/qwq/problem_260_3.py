import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 1 + sqrt(2)
sqrt_2 = mp.sqrt(2)
sum_term = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(sum_term)

# Multiply by pi/2 to get final result
pi_half = mp.pi / 2
result = pi_half * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
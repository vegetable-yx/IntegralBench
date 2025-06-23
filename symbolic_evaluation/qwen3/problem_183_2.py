import mpmath as mp
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (2 + sqrt(5)) term
sum_term = 2 + sqrt5

# Calculate natural logarithm of the sum term
log_term = mp.log(sum_term)

# Compute π/4 factor
pi_quarter = mp.pi / 4

# Multiply components to get final result
result = pi_quarter * log_term

print(mp.nstr(result, n=10))
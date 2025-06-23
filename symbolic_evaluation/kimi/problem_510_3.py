import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath constant
pi = mp.pi

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Multiply π and sqrt(3)
pi_times_sqrt3 = mp.fmul(pi, sqrt3)

# Divide by 9 to get final result
result = mp.fdiv(pi_times_sqrt3, 9)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
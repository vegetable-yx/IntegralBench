import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for intermediate calculations

# Compute cos(2) using mpmath
cos_2 = mp.cos(2)

# Calculate numerator (1 - cos(2))
numerator = mp.fsub(1, cos_2)

# Compute final result by dividing by 8
result = mp.fdiv(numerator, 8)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
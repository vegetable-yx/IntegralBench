import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute 2^(4/3) using mpmath for high precision
base = mp.mpf(2)
exponent = mp.mpf(4)/mp.mpf(3)  # 4/3 as a fraction
numerator = mp.power(base, exponent)  # 2^(4/3)

# Divide by 4 to get the final result
denominator = mp.mpf(4)
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))
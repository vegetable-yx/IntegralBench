import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate 2^(1/4) using power function
fourth_root_2 = mp.power(2, mp.mpf(1)/4)

# Compute the difference between square root and fourth root terms
difference = sqrt2 - fourth_root_2

# Multiply by pi to get final result
result = mp.pi * difference

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
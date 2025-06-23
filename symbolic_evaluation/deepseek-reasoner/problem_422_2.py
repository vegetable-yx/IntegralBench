import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate cube root of 2
cube_root_2 = mp.power(2, mp.mpf(1)/3)

# Divide by 2 to get final result
result = cube_root_2 / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
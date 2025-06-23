import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate arcsin(1/3)
x = mp.mpf(1)/3
arcsin_val = mp.asin(x)

# Multiply by pi to get the final result
result = mp.pi * arcsin_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
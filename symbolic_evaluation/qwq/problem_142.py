import mpmath as mp
mp.dps = 15

# Compute the hyperbolic sine integral Shi(4) and its special function implementation
shi_value, _ = mp.shichi(4)  # shichi returns (Shi, Chi) pair

# Calculate the final value by multiplying with 1/4
result = shi_value * mp.mpf(1)/4

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))
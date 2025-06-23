import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^4 using intermediate steps
pi_value = mp.pi
pi_squared = mp.power(pi_value, 2)  # Compute π²
pi_fourth = mp.power(pi_squared, 2)  # Square π² to get π⁴

# Divide π⁴ by 64 to get final result
result = mp.fdiv(pi_fourth, 64)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
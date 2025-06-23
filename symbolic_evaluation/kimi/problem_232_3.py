import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15
# Calculate pi constant from mpmath
pi_value = mp.pi
# Multiply by 2 to get final result
result = 2 * pi_value
# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate pi/4 using mpmath's constant
pi_value = mp.pi
result = pi_value / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
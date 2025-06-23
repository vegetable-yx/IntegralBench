import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Get the mathematical constant pi from mpmath
pi_constant = mp.pi

# Calculate the result by dividing pi by 16
result = pi_constant / 16

# Print the final value with 10 decimal precision
print(mp.nstr(result, n=10))
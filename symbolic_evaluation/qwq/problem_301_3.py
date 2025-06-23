import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate (ln 2)^2 component
ln2 = mp.log(2)
ln2_squared = ln2 ** 2
term1 = 4 * ln2_squared

# Calculate (5*pi^2)/6 component
pi_squared = mp.pi ** 2
term2 = (5 * pi_squared) / 6

# Combine all components
result = 8 - term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
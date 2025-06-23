import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function J1(2)
j1_value = mp.besselj(1, 2)

# Square the Bessel function result
j1_squared = mp.power(j1_value, 2)

# Divide by 4 to get the final result
result = mp.fdiv(j1_squared, 4)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
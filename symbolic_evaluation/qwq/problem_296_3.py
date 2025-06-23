import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the π value
pi_squared = mp.power(pi_value, 2)

# Multiply by 3
numerator = mp.fmul(3, pi_squared)

# Divide by 32 to get final result
result = mp.fdiv(numerator, 32)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
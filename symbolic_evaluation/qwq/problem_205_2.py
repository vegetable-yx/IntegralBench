import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute π multiplied by sqrt(2)
pi_times_sqrt2 = mp.pi * sqrt2

# Divide by 4 to get the coefficient term
coefficient = pi_times_sqrt2 / 4

# Calculate the Bessel function of the first kind J_1 at 1
bessel_j1_1 = mp.besselj(1, 1)

# Multiply coefficient by Bessel function result
result = coefficient * bessel_j1_1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))
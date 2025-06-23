import mpmath as mp
mp.dps = 15

# Calculate 2^(1/4) using mpmath power function
two_power = mp.power(2, 0.25)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Bessel function of the first kind at order -1/4 and argument 1
bessel_term = mp.besselj(-0.25, 1)

# Combine all components to get final result
result = two_power * sqrt_pi * bessel_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
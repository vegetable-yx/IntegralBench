import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute e^{1/2} = sqrt(e)
exp_half = mp.exp(0.5)

# Compute the modified Bessel function of the second kind at order 3/4 and argument 1/2
bessel_val = mp.besselk(0.75, 0.5)  # Note: 3/4 = 0.75

# Multiply by pi and the exponential factor
result = mp.pi * exp_half * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define constants
a = 2.0
c = 1.0

# Compute the analytical expression components
# The expression is: 4 * mp.pi * mp.exp(-1) * (mp.besselj(0, 1) + mp.besselj(1, 1))
# Step-by-step calculation:

# Compute mp.exp(-1)
exp_neg1 = mp.exp(-1)

# Compute Bessel functions at 1
j0_1 = mp.besselj(0, 1)
j1_1 = mp.besselj(1, 1)

# Sum the Bessel functions
bessel_sum = j0_1 + j1_1

# Multiply by 4*pi*exp(-1)
result = 4 * mp.pi * exp_neg1 * bessel_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the integral: \int_0^1 \frac{x(2x-1)}{x^4 - 2x^3 + 3x^2 - 2x + 2} dx
# The integral is broken into two parts using partial fractions.

# Part 1: \int_0^1 \frac{-x}{x^2 + 1} dx
# Antiderivative: F1(x) = -0.5 * log(x^2 + 1)
# Evaluate at upper bound x=1: F1(1) = -0.5 * log(1^2 + 1)
F1_upper = -0.5 * mp.log(1**2 + 1)
# Evaluate at lower bound x=0: F1(0) = -0.5 * log(0^2 + 1)
F1_lower = -0.5 * mp.log(0**2 + 1)
# Compute integral1 = F1(1) - F1(0)
integral1 = F1_upper - F1_lower

# Part 2: \int_0^1 \frac{x}{x^2 - 2x + 2} dx
# Antiderivative: F2(x) = 0.5 * log(x^2 - 2x + 2) + atan(x - 1)
# Evaluate at upper bound x=1: F2(1) = 0.5 * log(1^2 - 2*1 + 2) + atan(1 - 1)
F2_upper = 0.5 * mp.log(1**2 - 2*1 + 2) + mp.atan(1 - 1)
# Evaluate at lower bound x=0: F2(0) = 0.5 * log(0^2 - 2*0 + 2) + atan(0 - 1)
F2_lower = 0.5 * mp.log(0**2 - 2*0 + 2) + mp.atan(0 - 1)
# Compute integral2 = F2(1) - F2(0)
integral2 = F2_upper - F2_lower

# Combine the two integrals
total_integral = integral1 + integral2

# The expression: π/4 minus the integral
term = mp.pi / 4
result = term - total_integral

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
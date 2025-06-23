import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function terms
J0_1 = mp.besselj(0, 1)  # J₀(1)
J2_1 = mp.besselj(2, 1)  # J₂(1)
bessel_diff = J0_1 - J2_1  # J₀(1) - J₂(1)

# Calculate the first term with π/2 factor
pi_term = mp.pi / 2
term1 = pi_term * bessel_diff

# Calculate trigonometric components
sin1 = mp.sin(1)
cos1 = mp.cos(1)
trig_combination = sin1 + cos1 - 1  # sin(1) + cos(1) - 1

# Calculate the second term with 4 multiplier
term2 = 4 * trig_combination

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the exponential integral Ei(2)
ei_positive = mp.ei(2)

# Compute the exponential integral Ei(-2)
ei_negative = mp.ei(-2)

# Multiply each Ei result by 4
four_ei_positive = 4 * ei_positive
four_ei_negative = 4 * ei_negative

# Compute the numerator: 4*Ei(2) - 4*Ei(-2) - pi
numerator = four_ei_positive - four_ei_negative - mp.pi

# Multiply by e^{-2}
exp_factor = mp.exp(-2)
scaled_numerator = exp_factor * numerator

# Divide by 16 to get the final result
result = scaled_numerator / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
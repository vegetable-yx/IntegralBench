import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 2^13 * (Gamma(4))^8
# First compute Gamma(4)
gamma4 = mp.gamma(4)
# Raise to the 8th power
gamma4_8 = mp.power(gamma4, 8)
# Compute 2^13
two_13 = mp.power(2, 13)
# Multiply to get numerator
numerator = two_13 * gamma4_8

# Calculate the denominator: (Gamma(8))^4
gamma8 = mp.gamma(8)
# Raise to the 4th power
gamma8_4 = mp.power(gamma8, 4)
denominator = gamma8_4

# Compute the fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
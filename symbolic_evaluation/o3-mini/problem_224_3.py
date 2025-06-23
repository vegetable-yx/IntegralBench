import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate ln(2) and then square it to get ln^2(2)
ln2 = mp.log(2)
ln2_squared = ln2**2

# Compute (1 - π/4)
pi_term = 1 - mp.pi / 4

# First term: ln^2(2) * (1 - π/4)
first_term = ln2_squared * pi_term

# Compute the dilogarithm values
li2_half = mp.polylog(2, 0.5)   # Li_2(1/2)
li2_minus_half = mp.polylog(2, -0.5)  # Li_2(-1/2)

# Second term: (1/2) * (Li_2(1/2) - Li_2(-1/2))
second_term = 0.5 * (li2_half - li2_minus_half)

# Combine both terms to get the final result
result = first_term + second_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
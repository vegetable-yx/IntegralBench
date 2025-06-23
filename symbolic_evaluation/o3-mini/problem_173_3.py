import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the first hypergeometric term
gamma1 = mp.gamma(3/4) / mp.gamma(11/4)
hyp1 = mp.hyp2f1(0.5, 0.25, 11/4, 0.25)
part1 = gamma1 * hyp1

# Compute the second hypergeometric term
gamma2 = 2 * mp.gamma(7/4) / mp.gamma(5/4)
hyp2 = mp.hyp2f1(0.5, -0.25, 5/4, 0.25)
part2 = gamma2 * hyp2

# Combine the hypergeometric parts
inner_sum = part1 + part2

# Compute the multiplicative factor: π^(3/2) / 64
pi_factor = mp.pi**(1.5) / 64
combined_term = pi_factor * inner_sum

# Compute the subtraction term: π^3 / 144
subtract_term = (mp.pi**3) / 144

# Final result
result = combined_term - subtract_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
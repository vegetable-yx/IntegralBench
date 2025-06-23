import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute fundamental constants and logarithms
pi = mp.pi
ln2 = mp.ln(2)

# Calculate each term inside the parentheses separately
# Term 1: π³ / 12
term1 = pi**3 / 12

# Term 2: -(π/4) * (ln(2))²
term2 = -(pi / 4) * (ln2**2)

# Term 3: ln(2) * Li₂(1/2)
term3 = ln2 * mp.polylog(2, 0.5)

# Term 4: -Li₃(1/2)
term4 = -mp.polylog(3, 0.5)

# Term 5: 2 * Li₃(1/√2)
# First compute 1/√2
inv_sqrt2 = 1 / mp.sqrt(2)
term5 = 2 * mp.polylog(3, inv_sqrt2)

# Sum all terms inside the parentheses
inner_sum = term1 + term2 + term3 + term4 + term5

# Multiply by √2 to get final result
result = mp.sqrt(2) * inner_sum

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))
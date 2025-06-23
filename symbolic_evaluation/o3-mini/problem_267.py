import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constants
pi = mp.pi
ln2 = mp.log(2)

# Compute polylogarithm terms
li2 = mp.polylog(2, 0.25)  # Dilogarithm Li₂(1/4)
li3 = mp.polylog(3, 0.25)  # Trilogarithm Li₃(1/4)

# Calculate first major term: (π/96)[π² - 6·Li₂(1/4)]
inner1 = pi**2 - 6 * li2
term1 = (pi / 96) * inner1

# Calculate second major term: (1/32)[π·ln²2 + 4·ln2·Li₂(1/4) - 8·Li₃(1/4)]
inner2 = pi * ln2**2 + 4 * ln2 * li2 - 8 * li3
term2 = inner2 / 32

# Combine terms: term1 - term2
result = term1 - term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))
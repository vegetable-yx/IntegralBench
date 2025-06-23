import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute term1: π^3 / 192
term1 = mp.pi**3 / 192

# Compute term2: (π * (ln(2))^2) / 16
term2 = mp.pi * (mp.log(2))**2 / 16

# Compute term3: -(π * Catalan's constant) / 4
term3 = - (mp.pi * mp.catalan) / 4

# Compute the complex argument for the polylog term: (1+i)/2
c_arg = 0.5 + 0.5j

# Compute term4: (1/2) * Imaginary part of Li₂((1+i)/2)
li2_val = mp.polylog(2, c_arg)
term4 = 0.5 * mp.im(li2_val)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
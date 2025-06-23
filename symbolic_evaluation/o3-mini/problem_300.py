import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the prefactor: sqrt(pi) / (2^(13/2))
prefactor = mp.sqrt(mp.pi) / mp.power(2, 13/2)

# Compute trigamma values:
# ψ₁(1) - polygamma(1,1)
trigamma1 = mp.polygamma(1, 1)
# ψ₁(3/2) - polygamma(1, 3/2)
trigamma3_2 = mp.polygamma(1, 3/2)

# Compute digamma values:
# ψ(1) - digamma(1)
digamma1 = mp.digamma(1)
# ψ(3/2) - digamma(3/2)
digamma3_2 = mp.digamma(3/2)

# Calculate the expression inside the square brackets: [ψ(1) - ψ(3/2) - ln(2)]
inner_diff = digamma1 - digamma3_2 - mp.log(2)
# Square the inner difference
inner_square = inner_diff**2

# Combine all components: 2ψ₁(1) - 2ψ₁(3/2) + [inner_square]
combined = 2*trigamma1 - 2*trigamma3_2 + inner_square

# Multiply by the prefactor
result = prefactor * combined

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
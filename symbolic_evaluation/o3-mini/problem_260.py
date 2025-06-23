import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the sine integral at 1
si_val = mp.si(1)

# Compute Bessel function of the first kind, order 0 at 1
j0_val = mp.besselj(0, 1)

# Compute Struve H function, order 1 at 1
h1_val = mp.struveh(1, 1)

# Compute Bessel function of the first kind, order 1 at 1
j1_val = mp.besselj(1, 1)

# Compute Struve H function, order 0 at 1
h0_val = mp.struveh(0, 1)

# Calculate the expression inside the parentheses: J0(1)*H1(1) - J1(1)*H0(1)
inner_expr = j0_val * h1_val - j1_val * h0_val

# Multiply the inner expression by 1/2
scaled_inner = 0.5 * inner_expr

# Combine with sine integral term
result = si_val + scaled_inner

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
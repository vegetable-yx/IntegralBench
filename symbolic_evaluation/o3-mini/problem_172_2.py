import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Compute gamma(1/4)
gamma_14 = mp.gamma(1/4)

# Step 2: Compute the hypergeometric function 2F1(-1/2, 1/4; 3/4; 1/2)
hyp2f1_val = mp.hyp2f1(-0.5, 0.25, 0.75, 0.5)

# Step 3: Compute 8 * sqrt(pi) * hypergeometric result
term1 = 8 * mp.sqrt(mp.pi) * hyp2f1_val

# Step 4: Compute [gamma(1/4)]^2
gamma_sq = gamma_14**2

# Step 5: Compute the expression inside the brackets: term1 - gamma_sq
bracket = term1 - gamma_sq

# Step 6: Compute the denominator: 64 * sqrt(2 * pi)
denom = 64 * mp.sqrt(2 * mp.pi)

# Step 7: Compute the entire expression: [gamma(1/4)^2 / denom] * bracket
result = (gamma_sq / denom) * bracket

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))
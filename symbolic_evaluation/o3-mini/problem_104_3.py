import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the hypergeometric function ₂F₁(1/2, 1/2; 3/2; 1/16)
hyp_val = mp.hyp2f1(mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf('1.5'), mp.mpf('1/16'))

# Multiply the hypergeometric result by π/16
result = (mp.pi / 16) * hyp_val

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))
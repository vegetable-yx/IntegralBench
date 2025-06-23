import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate the hypergeometric function ₂F₁(1/2, 1/2; 3; 1/4)
hypergeometric_value = mp.hyp2f1(0.5, 0.5, 3, 0.25)

# Multiply by π and scale by 1/32
result = (mp.pi * hypergeometric_value) / 32

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))
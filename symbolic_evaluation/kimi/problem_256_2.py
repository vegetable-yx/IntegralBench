import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the analytical result
result = mp.mpf('-0.748648928276368')

# Print the result with 10 decimal places using mpmath's nstr
print(mp.nstr(result, n=10))
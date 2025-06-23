We start with the integral

  I = ∫ from -π/2 to π/2 cos(20x) sin(25x) dx.

Step 1. Use the product-to-sum identity:
  cos A · sin B = ½ [ sin(A + B) − sin(A − B) ].
Setting A = 20x and B = 25x we get:
  cos(20x) sin(25x) = ½ [ sin(45x) − sin(-5x) ].
Since sin(-5x) = - sin(5x), the expression simplifies to:
  cos(20x) sin(25x) = ½ [ sin(45x) + sin(5x) ].

Step 2. Write the integral in terms of sine functions:
  I = ½ ∫ from -π/2 to π/2 [ sin(45x) + sin(5x) ] dx.

Step 3. Notice that both sin(45x) and sin(5x) are odd functions. The integral of any odd function over an interval symmetric about zero (like -π/2 to π/2) is zero. Therefore:
  ∫ from -π/2 to π/2 sin(45x) dx = 0 and ∫ from -π/2 to π/2 sin(5x) dx = 0.

Step 4. Conclude that:
  I = ½ [0 + 0] = 0.

Step 5. The numerical approximation of zero is 0.0000000000 when rounded to 10 decimal places.

{"answer": "0", "numerical_answer": "0.0000000000"}
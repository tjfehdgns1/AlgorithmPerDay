function gcd(a, b)
    while b ~= 0 do
        a, b = b, a % b
    end
    return a
end

function simplify_fraction(A, B)
    C = gcd(A, B)
    simple_a = A // C
    simple_b = B // C
    return simple_a, simple_b
end

local a, b = io.read("*n", "*n")
local c, d = io.read("*n", "*n")

A, B = a * d + c * b, d * b
x, y = simplify_fraction(A, B)
print(x .. ' ' .. y)
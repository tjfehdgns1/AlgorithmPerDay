function sol(n, r, c)
    local result = 0
    
    while n ~= 0 do
        n = n - 1
        
        if r < 2 ^ n and c < 2 ^ n then
            result = result + (2 ^ n) * (2 ^ n) * 0
        elseif r < 2 ^ n and c >= 2 ^ n then
            result = result + (2 ^ n) * (2 ^ n) * 1
            c = c - (2 ^ n)
        elseif r >= 2 ^ n and c < 2 ^ n then
            result = result + (2 ^ n) * (2 ^ n) * 2
            r = r - (2 ^ n)
        else
            result = result + (2 ^ n) * (2 ^ n) * 3
            c = c - (2 ^ n)
            r = r - (2 ^ n)
        end
    end

    return result
end

function main()
    local n, r, c = io.read("n", "n", "n")
    local result = sol(n, r, c)
    print(math.floor(result))
end

main()
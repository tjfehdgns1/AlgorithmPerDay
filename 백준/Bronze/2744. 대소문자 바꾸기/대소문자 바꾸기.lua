function swapCase(input)
    local result = ""
    for i = 1, string.len(input) do
        local char = string.sub(input, i, i)
        if string.upper(char) == char then
            result = result .. string.lower(char)
        else
            result = result .. string.upper(char)
        end
    end
    return result
end

local userInput = io.read()

local swappedString = swapCase(userInput)

print(swappedString)

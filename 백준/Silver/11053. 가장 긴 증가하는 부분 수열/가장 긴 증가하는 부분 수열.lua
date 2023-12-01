n = io.read("*n")
input_str = io.read("a")


a = {}
for num in string.gmatch(input_str, "%S+") do
    table.insert(a, tonumber(num))
end


dp = {}
for i = 1, n do
    table.insert(dp, 1)
end

for i = 2, n do
    for j = 1, i do
        if a[i] > a[j] then
            dp[i] = math.max(dp[i], dp[j] + 1)
        end
    end
end

max_length = 1
for _, value in ipairs(dp) do
    max_length = math.max(max_length, value)
end

print(max_length)

local n = io.read("n")
local given = {}
for _ = 1, n do
    s, e = io.read("n", "n")
    table.insert(given, {s, e})
end

table.sort(given, function(a, b)
    if a[2] == b[2] then
        return a[1] < b[1]
    end
    return a[2] < b[2]
end)

local count = 1
local end_time = given[1][2]

for i = 2, n do
    local s, e = given[i][1], given[i][2]

    if s >= end_time then
        end_time = e
        count = count + 1
    end
end

print(count)

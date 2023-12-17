-- Function to find the maximum sum using dynamic programming
function sol(n, dp)
    for i = 2, n do
        if i == 2 then
            dp[1][2] = dp[1][2] + dp[2][1]
            dp[2][2] = dp[2][2] + dp[1][1]
        else
            dp[1][i] = dp[1][i] + math.max(dp[2][i - 1], dp[2][i - 2])
            dp[2][i] = dp[2][i] + math.max(dp[1][i - 1], dp[1][i - 2])
        end
    end

    -- Print the maximum result for the last column
    print(math.max(dp[1][n], dp[2][n]))
end

-- Read the number of test cases
local T = tonumber(io.read())

-- Process each test case
for _ = 1, T do
    -- Read the value of n for the current test case
    local n = tonumber(io.read())

    -- Initialize the dp array
    local dp = {}
    for i = 1, 2 do
        dp[i] = {}
        -- Read the input numbers for each row of the dp array
        local inputstr = io.read()
        for num in inputstr:gmatch("%S+") do
            table.insert(dp[i], tonumber(num))
        end
    end

    -- Call the sol function for the current test case
    sol(n, dp)
end

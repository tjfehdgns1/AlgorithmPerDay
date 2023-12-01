local function backTrack(stack, start, n, m)
    if #stack == m then
        print(table.concat(stack, ' '))
        return
    end

    for i = start, n do
       table.insert(stack, i) 
       backTrack(stack, i, n, m)
       table.remove(stack)
    end
end


n, m = io.read("*n", "*n")
s = {}

backTrack(s, 1, n, m)
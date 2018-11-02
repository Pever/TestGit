
function funa()
	print("funa ex")
end

function funb()
	print("funb ex")
end



--local array = { 1,2,3,4,5,x = funb(),y = funa(),[7] = 6}

--local array2 = { [1] = 1,[2] = 2,[3] = 3,[4] = 4,[5] = 5,x = "xxxx",y = "yyyy",[6] = 6}
local array2 = {[1]=1, [2]=2,[3]=3,[4]=4,[5]=5,[6]=6,[7]=7,[8] = 8,[9] = 9,[11] = 11 }
--local array2 = { 1,2,3,4,5,x = "xxxx",y = "yyyy",6}


local array3 = { 1,2,3,4,5,6}

print(#array2)

for i,v in ipairs(array2) do
	print(i,v)
end



---main test 1
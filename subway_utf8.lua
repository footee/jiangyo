

-- load the http module
local io = require("io")
local ltn12 = require("ltn12")
local icu = require("icu")
local ustring = require("icu.ustring")
local utf8 = require("icu.utf8")
local uregex = require("icu.regex")
local sqlite3 = require("luasql.sqlite3")
local env = assert(luasql.sqlite3())
local con = assert(env:connect("anjuke.db"))


function DB_ERROR(res, message)
	if res == nil or res == false then
		print("ERROR: sqlite3 DB: anjuke.db "..message)
	end
end

function PARSE_ERROR(res, message)
	if res == nil or res == false then
		print("ERROR: PARSE "..message)
	end
end


action = "CREATE TABLE IF NOT EXISTS subway (id INTEGER PRIMARY KEY ASC, name TEXT, station TEXT, latitude NUMERIC, longitude NUMERIC)"
res = con:execute(action)
DB_ERROR(res, "TABLE: subway ACTION: "..action)


local file = io.open("subway_data.txt", "r")

for line in file:lines() do 
	local a,b = string.match(line, "(%S+)%s+(%S+)%s+")

	if a ~= nil then
		
		a = icu.convert(a, nil, "utf-8")
		b = icu.convert(b, nil, "utf-8")
		print(a,b)


		local pos = {}
		for c in string.gmatch(line, "(%d+%.%d+)") do
			table.insert(pos, c)
		end

		print(pos[1], pos[2])

		action = string.format([[INSERT INTO subway VALUES (NULL, '%s', '%s', %.15f, %.15f)]], a, b, pos[1], pos[2])
		res = con:execute(action)
		DB_ERROR(res, "TABLE: subway ACTION: "..action)
	end
end

file:close()
con:close()
env:close()



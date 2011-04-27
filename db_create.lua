

-- load the http module
local io = require("io")
local http = require("socket.http")
local ltn12 = require("ltn12")
local icu = require("icu")
local ustring = require("icu.ustring")
local utf8 = require("icu.utf8")
local uregex = require("icu.regex")
local sqlite3 = require("luasql.sqlite3")
local env = assert(luasql.sqlite3())
local con = assert(env:connect("test.db"))

--local file = io.open("anjuke_zone.html","w")
--file:write(upage)
--file:close()



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


action = "CREATE TABLE IF NOT EXISTS area (id INTEGER PRIMARY KEY ASC, url TEXT, name TEXT, community INTEGER)"
res = con:execute(action)
DB_ERROR(res, "TABLE: area ACTION: "..action)

-- fix information of community
action = "CREATE TABLE IF NOT EXISTS community_info (id INTEGER PRIMARY KEY ASC, url INTEGER, name TEXT, latitude NUMERIC, longitude NUMERIC, location TEXT, sale_trends TEXT, rental_trends TEXT, houses NUMERIC, pack TEXT, developer TEXT, tenement TEXT, tenement_type TEXT, building_date TEXT, plot_ratio NUMERIC, afforest NUMERIC, area TEXT, timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)"
res = con:execute(action)
DB_ERROR(res, "TABLE: area ACTION: "..action)

-- price information of community
action = "CREATE TABLE IF NOT EXISTS community_price (id INTEGER PRIMARY KEY ASC, info INTEGER, price NUMERIC, sales NUMERIC, sale_1 NUMERIC, sale_2 NUMERIC, sale_3 NUMERIC, sale_4 NUMERIC, sale_5 NUMERIC, sale_6 NUMERIC, rental NUMERIC, rents NUMERIC, timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(info) REFERENCES community_info(id))"
res = con:execute(action)
DB_ERROR(res, "TABLE: area ACTION: "..action)



con:close()
env:close()



-- load the http module
local io = require("io")
local http = require("socket.http")
local ltn12 = require("ltn12")
local icu = require("icu")
local ustring = require("icu.ustring")
local utf8 = require("icu.utf8")
local uregex = require("icu.regex")
local sqlite3 = require("luasql.sqlite3")
local json = require("json")

local env = assert(luasql.sqlite3())
local con = assert(env:connect("anjuke.db"))


function httpwget(url)
    -- get the community link and name
    -- a simplified http.get function
    local t = {}
    local response = http.request{
        url = url,
        sink = ltn12.sink.table(t)
    }

    if response == nil then
        return
    end

    local page = table.concat(t)
    local upage = icu.convert(page, nil, "utf-8")

    return page, upage
end


function rows(connection, sql_statement)
	local cursor = assert(connection:execute(sql_statement))
	return function ()
		return cursor:fetch()
	end
end

local page
local upage
action = "SELECT * from community_info where longitude is NULL"
for id,url,name,lat,lng,address,sale_trends,rental_trends,houses,pack,developer,tenement,tenement_type,building_date,plot_ratio,afforest,area,timestamp  in rows(con, action) do 
	
	print(id, name, address, area)
		
	repeat 
		page, upage = httpwget("http://ditu.google.cn/maps/geo?output=json&sensor=false&q=".."北京市"..address) 
	until page ~= nil

	data = json.decode(page)
	
	if data['Placemark'] == nil then
		page, upage = httpwget("http://ditu.google.cn/maps/geo?output=json&sensor=false&q=".."北京市"..address)
	end
	data = json.decode(page)

	lng = data['Placemark'][1]['Point']['coordinates'][1]
	lat = data['Placemark'][1]['Point']['coordinates'][2]

	if lat ~= 39.904214 then
		print(lat, lng)
		action = string.format([[UPDATE community_info SET latitude=%.15f , longitude=%.15f where id=%s]], lat, lng, id)
	else
		print("NULL, NULL")
		action = string.format([[UPDATE community_info SET latitude=NULL , longitude=NULL where id=%s]], id)
	end
	
	res = con:execute(action)
end



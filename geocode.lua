
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

local page, upage = httpwget("http://ditu.google.cn/maps/geo?output=json&sensor=false&q=瑞丽家园")

data = json.decode(page)

lng = data['Placemark'][1]['Point']['coordinates'][1]
lat = data['Placemark'][1]['Point']['coordinates'][2]

print(lat, lng)



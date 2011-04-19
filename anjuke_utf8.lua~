
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
local con = assert(env:connect("anjuke.db"))

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

function parseCommunityMain(id)

	-- get the page
	local page, upage
	repeat 
		page, upage = httpwget("http://beijing.anjuke.com/v2/community/view/"..id) 
	until page ~= nil
	
	-- latitude and longitude: <a href="/v2/map/sale/#l1=39.8897641521133&l2=116.479679346085&l3=16&flag=1&flagname=
	local latitude, longitude = utf8.match(upage, "\<a href=\"/v2/map/sale/#l1=(%d+%.%d+)&l2=(%d+%.%d+)&")
	PARSE_ERROR(latitude, id.." latitude")
	PARSE_ERROR(longitude, id.." longitude")
	if latitude == nil then
		latitude = 0
	end
	if longitude == nil then
		longitude = 0
	end

	-- price:  均价<em>34499元/平米</em>
	local price = utf8.match(page, "\<em\>(%d+)元/平米\</em\>")
	PARSE_ERROR(price, id.." price")
	if price == nil then
		price = 0
	end
	
	-- price trends link
	-- <a href="http://beijing.anjuke.com/v2/community/trends/55031W0QQmonthZ6"
	local trends = utf8.match(upage, "\<a href=\"http://beijing%.anjuke%.com/v2/community/trends/(%w-)\"")
	PARSE_ERROR(trends, id.." sale_trends")
	if trends == nil then
		trends = "none"
	end

	-- building time
	-- <li class="short">竣工日期：2009-10-15</li>
	local building_date = utf8.match(page, "竣工日期：(%d%d%d%d%-%d%d%-%d%d)")
	if building_date == nil then
		building_date = utf8.match(page, "竣工日期：(%d%d%d%d%-%d%d)")
	end
	if building_date == nil then
		building_date = utf8.match(page, "竣工日期：(%d%d%d%d)")
	end
	PARSE_ERROR(building_date, id.." bulding_date")
	if building_date == nil then
		building_date = "0000-00-00"
	end

	-- sale number
	-- href="http://beijing.anjuke.com/v2/community/props/sale/55031" _soj="baseinfo" class="prop">3310
	local sales = utf8.match(upage, "anjuke%.com/v2/community/props/sale/%d+\" _soj=\"baseinfo\" class=\"prop\"\>(%d+)")
	PARSE_ERROR(sales, id.." sales")
	if sales == nil then
		sales = 0
	end
	
	-- rent number
	-- <a id="comm_rent_qt_1" href="http://beijing.anjuke.com/v2/community/props/rent/55031" _soj="baseinfo" class="prop">1234
	local rents = utf8.match(upage, "http://beijing%.anjuke%.com/v2/community/props/rent/%d+\" _soj=\"baseinfo\" class=\"prop\"\>(%d+)")
	PARSE_ERROR(rents, id.." rents")
	if rents == nil then
		rents = 0
	end

	local sale_1 = utf8.match(page, "一室%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_1 == nil then
		sale_1 = 0
	end
	local sale_2 = utf8.match(page, "二室%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_2 == nil then
		sale_2 = 0
	end
	local sale_3 = utf8.match(page, "三室%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_3 == nil then
		sale_3 = 0
	end
	local sale_4 = utf8.match(page, "四室%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_4 == nil then
		sale_4 = 0
	end
	local sale_5 = utf8.match(page, "五室%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_5 == nil then
		sale_5 = 0
	end
	local sale_6 = utf8.match(page, "五室以上%s*%(\<a href=\"http://beijing%.anjuke%.com/v2/community/props/sale/%w-\"\>(%d-)套\</a\>")
	if sale_6 == nil then
		sale_6 = 0
	end

	local ans = {}
	ans['latitude'] = latitude
	ans['longitude'] = longitude
	ans['price'] = price
	ans['trends'] = trends
	ans['sales'] = sales
	ans['rents'] = rents
	ans['building_date'] = building_date
	ans['sale_1'] = sale_1
	ans['sale_2'] = sale_2
	ans['sale_3'] = sale_3
	ans['sale_4'] = sale_4
	ans['sale_5'] = sale_5
	ans['sale_6'] = sale_6
	
	--for m,n in pairs(ans) do
	--	print(m,n)
	--end

	return ans
end

function parseCommunityDetail(id)

	local page, upage
	repeat 
		page, upage = httpwget("http://beijing.anjuke.com/v2/community/details/"..id) 
	until page ~= nil
	
	-- location
	-- 	<td class="bg0">小区地址</td>
	--	<td colspan="3">西大望路甲23号</td>
	local location = string.match(page, "地址\</td\>\r\n%s*\<td colspan=\"3\"\>(.-)\</td\>")
	PARSE_ERROR(location, id.." location")
	if location == nil then
		location = "暂无资料"
	end
	location = icu.convert(location, nil, "utf-8")

	-- house
	--	<td class="bg0">总户数</td>
	--	<td>4200套</td>
	local houses = string.match(page, "总户数\</td\>\r\n%s*\<td\>(%d+)")
	PARSE_ERROR(houses, id.." houses")
	if houses == nil then
		houses = 0
	end
	
	-- pack
	--	<td class="bg0">停车位</td>
	--	<td>4200套</td>
	local pack = string.match(page, "停车位\</td\>\r\n%s*\<td\>(%S+)\</td\>")
	PARSE_ERROR(pack, id.." pack")
	if pack == nil then
		pack = "暂无资料"
	end
	pack = icu.convert(pack, nil, "utf-8")

	-- developer
	--	<td class="bg0">开发商</td>
	--	<td>北京合生北方房地产开发有限公司</td>
	local developer = string.match(page, "开发商\</td\>\r\n%s*\<td\>(%S+)\</td\>")
	PARSE_ERROR(developer, id.." developer")
	if developer == nil then
		developer = "暂无资料"
	end
	developer = icu.convert(developer, nil, "utf-8")

	-- plot_ratio
	--	<td class="bg0">容积率</td>
	--	<td>2.890</td>
	local plot_ratio = string.match(page, "容积率\</td\>\r\n%s*\<td\>(%d+%.?%d*)")
	PARSE_ERROR(plot_ratio, id.." plot_ratio")
	if plot_ratio == nil then
		plot_ratio = 0 
	end
	
	-- tenement
	--	<td class="bg0">物业类型</td>
	--	<td>公寓</td>
	local tenement_type = string.match(page, "物业类型\</td\>\r\n%s*\<td\>(%S+)\</td\>")
	PARSE_ERROR(tenement_type, id.." tenement_type")
	if tenement_type == nil then
		tenement_type = "暂无资料"
	end
	tenement_type = icu.convert(tenement_type, nil, "utf-8")

	-- tenement
	--	<td class="bg0">物业公司</td>
	--	<td>康景物业管理集团</td>
	local tenement = string.match(page, "物业公司\</td\>\r\n%s*\<td\>(%S+)\</td\>")
	PARSE_ERROR(tenement, id.." tenement")
	if tenement == nil then
		tenement = "暂无资料"
	end
	tenement = icu.convert(tenement, nil, "utf-8")

	-- afforest 
	--	<td class="bg0">绿化率</td>
	--	<td>37.00%</td>
	local afforest = string.match(page, "绿化率\</td\>\r\n%s*\<td\>(%d%d%.?%d*)")
	PARSE_ERROR(afforest, id.." afforest")
	if afforest == nil then
		afforest = 0 
	end

	local ans={}
	ans['location'] = location
	ans['houses'] = houses
	ans['pack'] = pack
	ans['developer'] = developer
	ans['plot_ratio'] = plot_ratio
	ans['tenement'] = tenement
	ans['tenement_type'] = tenement_type
	ans['afforest'] = afforest
	
	--for m,n in pairs(ans) do
	--	print(m,n)
	--end

	return ans
end


function parseCommunityRents(id)

	local page, upage
	repeat 
		page, upage = httpwget("http://beijing.haozu.com/compound/"..id) 
	until page ~= nil
	
	-- rental
        --<h2 class="communityH2Title">本月参考均价：
        --<span class="yellow">981</span>元/套
	local rental = utf8.match(page, "本月参考均价：\n%s*\<span class=\"yellow\"\>(%d+)\</span\>元")
	PARSE_ERROR(rental, id.." rental")
	if rental == nil then
		rental = 0
	end

	-- trends
	-- <a href="/compound/trend/W0QQcZ76734" title="查看租金走势">
	local trends = utf8.match(page, "/compound/trend/(%w-)\" title=\"查看租金走势\"")
	PARSE_ERROR(trends, id.." rent_trends")

	-- agent rent
        -- 经纪人房源：<a href="http://beijing.haozu.com/compound/broker/W0QQcZ76743?from=from-index-broker-count" _soj="from-index-broker-count" title="17套">
	local agent = utf8.match(page, "经纪人房源：.- _soj=\"from%-index%-broker%-count\" title=\"(%d+)套\"\>")
	PARSE_ERROR(agent, id.." agent")

	-- individual rent
	-- 个人房源：<a href="http://beijing.haozu.com/compound/landlord/W0QQcZ76743?from=from-index-landlord-count" _soj="from-index-landlord-count" title="0套">0套</a>
	local personal = utf8.match(page, "个人房源：.- _soj=\"from%-index%-landlord%-count\" title=\"(%d+)套\"\>")
	PARSE_ERROR(personal, id.." personal")

	local ans = {}
	ans['rental'] = rental
	ans['trends'] = trends
	ans['rents'] = agent + personal
	
	--for m,n in pairs(ans) do
	--	print(m,n)
	--end

	return ans
end


-- rowid: db table rowid   url: community htmlpage linkid  name: community name
function insertToDb(rowid, url, name, area)

	local main = parseCommunityMain(url)
	local detail = parseCommunityDetail(url)
	local rent = parseCommunityRents(url)

	local action = string.format(
	[[INSERT INTO community_info (id, url, name, latitude, longitude, location, sale_trends, rental_trends, houses, pack, developer, tenement, tenement_type, building_date, plot_ratio, afforest, area) VALUES (NULL, %d, "%s", %.15f, %.15f, "%s", "%s", "%s", %d, "%s", "%s", "%s", "%s", "%s", %.3f, %.3f, "%s")]],
	url, name,
	main['latitude'], main['longitude'], detail['location'],
	main['trends'],
	rent['trends'],
	detail['houses'], detail['pack'],
	detail['developer'], detail['tenement'], detail['tenement_type'], main['building_date'],
	detail['plot_ratio'], detail['afforest'], 
	area)

	res = con:execute(action)
	DB_ERROR(res, "TABLE: community ACTION: "..action)

	action = string.format(
	[[INSERT INTO community_price (id, info, price, sales, sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, rental, rents) VALUES (NULL, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)]],
	rowid,
	main['price'], main['sales'], main['sale_1'], main['sale_2'], main['sale_3'], main['sale_4'], main['sale_5'], main['sale_6'],
	rent['rental'], rent['rents'])

	res = con:execute(action)
	DB_ERROR(res, "TABLE: community ACTION: "..action)

end

--insertToDb(91, 76342, "原因元小区", "西城")


-- get the area url and name
local temp = {}
local area = {}
local page = httpwget("http://beijing.anjuke.com")
-- <div class="tab" id="nav_tab_1_apf_id_15" ><a target="_blank" href="http://beijing.anjuke.com/v2/community/list/W0QQp1Z601"></a></div>
for url, name in utf8.gmatch(page, "href=\"http://beijing%.anjuke%.com/v2/community/list/(%w-)\"\>(.-)\</a\>\</div\>") do 
    table.insert(area, {['url']=url, ['name']=name})
end

-- i = 3
-- all area in beijing
for i,v in ipairs(area) do

	-- get the first page community url and name
	area[i]['community'] = {}
	repeat 
		page = httpwget("http://beijing.anjuke.com/v2/community/list/"..area[i]['url'])
	until page ~= nil

	for id, name in utf8.gmatch(page, "href=\"http://beijing%.anjuke%.com/v2/community/view/(%d+)\" target=\"_blank\"\>(.-)\</a\>") do
		if string.find(name, "%%") == nil then
			table.insert(area[i]['community'], {['id']=id, ['name']=name})
		end
	end

	-- get the next community list page
	-- <a href="http://beijing.anjuke.com/v2/community/list/W0QQp1Z601QQpZ2"><span class="nextpage">
	local nextpage = utf8.match(page, "\<a href=\"http://beijing%.anjuke%.com/v2/community/list/(%w-)\"\>\<span class=\"nextpage\"\>")
	while nextpage ~= nil do
		repeat 
			page = httpwget("http://beijing.anjuke.com/v2/community/list/"..nextpage)
		until page ~= nil

		for id, name in utf8.gmatch(page, "href=\"http://beijing%.anjuke%.com/v2/community/view/(%d-)\" target=\"_blank\"\>(.-)\</a\>") do
			-- except the good opinion degree 50% string
			if string.find(name, "%%") == nil then
				table.insert(area[i]['community'], {['id']=id, ['name']=name})
			end
		end

		nextpage = utf8.match(page, "\<a href=\"http://beijing%.anjuke%.com/v2/community/list/(%w-)\"\>\<span class=\"nextpage\"\>")
	end
end


rowid = 1
for i,v in ipairs(area) do
      print(i,v['name'])
      action = string.format([[INSERT INTO area VALUES (NULL, '%s', '%s', %d)]], v['url'], v['name'], #v['community'])
      res = con:execute(action)
      DB_ERROR(res, "TABLE: area ACTION: "..action)

      for id,value in ipairs(area[i]['community']) do

      	print(id,value['id'],value['name'])
      	insertToDb(rowid, value['id'], value['name'], v['name'])
      	rowid = rowid+1
      end

end


con:close()
env:close()


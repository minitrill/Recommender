### 目标网址
----
#### 基本用户信息

- Request URL: https://space.bilibili.com/ajax/member/GetInfo
- Request Method: POST
- Payload：
```
    {
        'mid': string of user's id,
        'csrf': '',
    }
```
- Request Header:

```
    {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'space.bilibili.com',
        'Origin': 'https://space.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' % random.randint(1,1000),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:

```
data:{mid: 176389292, name: "LouisWit", sex: "保密", rank: 5000,…}
    birthday:"01-01"
    coins:0
    face:"http://static.hdslb.com/images/member/noface.gif"
    fans_badge:false
    im9_sign:"c9dcb17600f9a9a67208ff9c5d72ccad"
    level_info:{current_level: 0}
        current_level:0
    mid:176389292
    name:"LouisWit"
    official_verify:{type: -1, desc: "", suffix: ""}
        desc:""
        suffix:""
        type:-1
    rank:5000
    regtime:1501216737
    sex:"保密"
    sign:""
    spacesta:0
    theme:"default"
    theme_preview:""
    toutu:"bfs/space/768cc4fd97618cf589d23c2711a1d1a729f42235.png"
    toutuId:1
    vip:{vipType: 0, vipStatus: 0}
        vipStatus:0
        vipType:0
status:true
```


#### 社交信息
- Request URL: https://api.bilibili.com/x/relation/stat?vmid={mid}&jsonp=jsonp&callback=__jp3
- Request Method: GET
- Request Header: 
```
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:
```
data:{mid: 176389292, following: 9, whisper: 0, black: 0, follower: 0}
```


#### 交互信息
- Request URL: https://api.bilibili.com/x/space/upstat?mid={mid}&jsonp=jsonp&callback=__jp4
- Request Method: GET
- Request Header: 
```
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:

```
data:{archive: {view: 0}, article: {view: 0}}
```


#### 提交信息
- Request URL: https://api.bilibili.com/x/space/navnum?mid={mid}&jsonp=jsonp&callback=__jp2
- Request Method: GET
- Request Header:  
```
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:
```
album:0
article:0
audio:0
bangumi:0
channel:{master: 0, guest: 0}
favourite:{master: 5, guest: 5}
playlist:0
tag:0
video:0
```


#### 收藏信息
- Request URL: https://api.bilibili.com/x/space/fav/nav?mid=176389292&jsonp=jsonp&callback=__jp12
- Request Method: GET
- Request Header:  
```
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:
```
data:{,…}
    album:0
    archive:[{fid: 1345715, mid: 176389292, name: "默认收藏夹", max_count: 100000, cur_count: 6, atten_count: 0,…},…]
        0:{fid: 1345715, mid: 176389292, name: "默认收藏夹", max_count: 100000, cur_count: 6, atten_count: 0,…}
            atten_count:0
            cover:[{aid: 9399358, pic:"http://i2.hdslb.com/bfs/archive/8e27ec58f1a577e4aa113441e269b1e52969a459.jpg"},…]
            ctime:1501216804
            cur_count:6
            favoured:0
            fid:1345715
            max_count:100000
            mid:176389292
            mtime:1503433672
            name:"默认收藏夹"
            state:0
        1:{fid: 1703979, mid: 176389292, name: "计算机", max_count: 999, cur_count: 8, atten_count: 0, favoured: 0,…}
        2:{fid: 1383506, mid: 176389292, name: "self driving", max_count: 999, cur_count: 3, atten_count: 0,…}
        3:{fid: 1345718, mid: 176389292, name: "ML", max_count: 999, cur_count: 14, atten_count: 0, favoured: 0,…}
        4:{fid: 1242972, mid: 176389292, name: "算法题", max_count: 999, cur_count: 6, atten_count: 0, favoured: 0,…}
    article:0
    movie:0
    playlist:0
    topic:0
```

#### 每个收藏信息
- Request URL: https://api.bilibili.com/x/v2/fav/video?vmid=176389292&ps=30&fid=1345718&tid=0&keyword=&pn=1&order=fav_time&jsonp=jsonp&callback=__jp16
- Request Method: GET
- Request Header:  
```
    {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'api.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```


```
data:{seid: "3825081278137739842", page: 1, pagesize: 30, pagecount: 1, total: 14, suggest_keyword: "",…}
    archives:[{aid: 12561021, videos: 72, tid: 39, tname: "演讲• 公开课", copyright: 2,…},…]
        0:{aid: 12561021, videos: 72, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        1:{aid: 13383754, videos: 19, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        2:{aid: 13153048, videos: 25, tid: 39, tname: "演讲• 公开课", copyright: 1,…}
        3:{aid: 13260183, videos: 16, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        4:{aid: 12532910, videos: 15, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        5:{aid: 9770302, videos: 25, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        6:{aid: 10590361, videos: 39, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        7:{aid: 9770190, videos: 28, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        8:{aid: 12044968, videos: 1, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        9:{aid: 9688898, videos: 1, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        10:{aid: 12211434, videos: 3, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        11:{aid: 9691070, videos: 1, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        12:{aid: 11574509, videos: 17, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
        13:{aid: 9806881, videos: 11, tid: 39, tname: "演讲• 公开课", copyright: 2,…}
    fid:1345718
    keyword:""
    mid:176389292
    order:"fav_time"
    page:1
    pagecount:1
    pagesize:30
    seid:"3825081278137739842"
    suggest_keyword:""
    tid:0
    tlist:[{tid: 36, name: "科技", count: 14}]
        0:{tid: 36, name: "科技", count: 14}
        count:14
        name:"科技"
    tid:36
    total:14
```


#### 标签
- Request URL: https://space.bilibili.com/ajax/member/getTags?mids={mid}
- Request Method: GET
- Request Header:  
```
    {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'space.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:

```
data:[{mid: 814727, tags: ["宅舞"]}]
    0:{mid: 814727, tags: ["宅舞"]}
        mid:814727
        tags:["宅舞"]
```


#### 子标签
- Request URL: https://space.bilibili.com/ajax/tags/getSubList?mid={mid}
- Request Method: GET
- Request Header:  
```
    {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'space.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' mid,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
```
- Data form:

```
data:{tags: [,…], count: 1}
    count:1
    tags:[,…]
    0:
        {name: "enolla"
```




### 建议
----
- 限制：
从b站上爬取到的数据有限，和初始所维持的数据格式有区别，比如年龄、常驻地（国省市）等信息有所欠缺，有2哥解决方法：
    1. 修改数据库的列属性；
    2. 自制数据（难度：制造数据有难度，推荐算法会推荐不准确，fake data）。
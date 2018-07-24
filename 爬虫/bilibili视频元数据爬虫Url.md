### 视频元数据

---
#### 基本信息
- Request URL: https://api.bilibili.com/x/web-interface/archive/stat?aid={}
- Request Method: GET
- Request Header:

```
{
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'api.bilibili.com',
    'Origin': 'https://www.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av27301631/?spm_id_from=333.334.home_popularize.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
```
- Data Form:

```
data:{aid: 27301631, view: 94906, danmaku: 1443, reply: 1129, favorite: 4198, coin: 15223, share: 1864,…}
    aid:27301631
    coin:15223
    copyright:1
    danmaku:1443
    favorite:4198
    his_rank:0
    like:7069
    no_reprint:1
    now_rank:0
    reply:1129
    share:1864
    view:94906
```

#### 标签信息
- Request URL: https://api.bilibili.com/x/tag/archive/tags?callback=jqueryCallback_bili_5&aid={}}&jsonp=jsonp&_={毫秒级的时间戳}
- Request Method: GET
- Request Header:

```
{
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'api.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av{}/?spm_id_from=333.334.home_popularize.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
```
- Data Form:

```
data:[{tag_id: 832569, tag_name: "美妆",…}, {tag_id: 11684, tag_name: "LISA",…},…]
    0:{tag_id: 832569, tag_name: "美妆",…}
    1:{tag_id: 11684, tag_name: "LISA",…}
    2:{tag_id: 261355, tag_name: "化妆教程", cover: "http://static.hdslb.com/images/transparent.gif",…}
    3:{tag_id: 499816, tag_name: "彩妆", cover: "http://static.hdslb.com/images/transparent.gif", content: "",…}
    4:{tag_id: 902193, tag_name: "仿妆", cover: "http://static.hdslb.com/images/transparent.gif", content: "",…}
    5:{tag_id: 1141438, tag_name: "美妆教程", cover: "http://static.hdslb.com/images/transparent.gif",…}
    6:{tag_id: 13175, tag_name: "化妆", cover: "http://static.hdslb.com/images/transparent.gif", content: "",…}
    7:{tag_id: 1749296, tag_name: "BLACKPINK", cover: "", content: "", type: 3, state: 0, ctime: 1467771301,…}
    8:{tag_id: 176488, tag_name: "产品", cover: "http://static.hdslb.com/images/transparent.gif", content: "",…}
    9:{tag_id: 982418, tag_name: "化妆技巧", cover: "http://static.hdslb.com/images/transparent.gif",…
```

#### 标签相关的视频链接

- Request URL: https://api.bilibili.com/x/web-interface/archive/related?aid={}&callback=jqueryCallback_bili_8&jsonp=jsonp&_={毫秒级的时间戳}
- Request Method: GET
- Request Header:

```
{
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'api.bilibili.com',
    'Referer': 'https://www.bilibili.com/video/av{}/?spm_id_from=333.334.home_popularize.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
```


```
data:[{aid: 8035503, videos: 1, tid: 156, tname: "舞蹈教程", copyright: 2,…},…]
    0:{aid: 8035503, videos: 1, tid: 156, tname: "舞蹈教程", copyright: 2,…}
    1:{aid: 2219954, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    2:{aid: 1706238, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    3:{aid: 7709996, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    4:{aid: 27376889, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    5:{aid: 11030737, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    6:{aid: 27324931, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    7:{aid: 27145335, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    8:{aid: 26830086, videos: 2, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    9:{aid: 22655235, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    10:{aid: 27379226, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    11:{aid: 26841184, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    12:{aid: 27105846, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    13:{aid: 27114437, videos: 1, tid: 20, tname: "宅舞", copyright: 2,…}
    14:{aid: 4356656, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    15:{aid: 15247717, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    16:{aid: 27160490, videos: 2, tid: 20, tname: "宅舞", copyright: 1,…}
    17:{aid: 27264432, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    18:{aid: 27299582, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    19:{aid: 27104186, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    20:{aid: 26859509, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    21:{aid: 16840359, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    22:{aid: 27271800, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    23:{aid: 17705362, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    24:{aid: 23345335, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    25:{aid: 27337649, videos: 2, tid: 20, tname: "宅舞", copyright: 1,…}
    26:{aid: 27291806, videos: 2, tid: 20, tname: "宅舞", copyright: 1,…}
    27:{aid: 27057377, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    28:{aid: 26276877, videos: 1, tid: 20, tname: "宅舞", copyright: 1,…}
    29:{aid: 13914408, videos: 1, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    30:{aid: 27323138, videos: 2, tid: 154, tname: "三次元舞蹈", copyright: 1,…}
    31:{aid: 27290152, videos: 2, tid: 131, tname: "Korea相关", copyright: 2,…}
```

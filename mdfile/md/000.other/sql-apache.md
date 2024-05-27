---
title: mysql serch

---
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MySQL 查詢結果</title>
    <style>
        @import url("style/mysql_show.css");
    </style>
    <script src="script/mysql_show.js"></script>
</head>
<body>
    <h1>MySQL test 可視化頁面</h1>
    <h2>SQL Query</h2>
    <textarea id ="textarea1"></textarea><br>
    <button id = "fuck" onclick="pushQuery()">輸入</button>
    <div id="table-container"></div>
    <button onclick="fetchMySQLData()" id ="mysql_btn">更新表格</button>

</body>
</html>
```
---
title: select

---

```sql=
-- 尋找title中包含'史萊姆'的
select *
from (  SELECT * FROM novel
        WHERE title LIKE '%史萊姆%'
        union
        SELECT * FROM comic
        WHERE title LIKE '%史萊姆%'
        union
        SELECT * FROM anime
        WHERE Title LIKE '%史萊姆%');

```

```sql=
-- 找出符合條件的小說中有輕改漫畫的
SELECT novel.* 
FROM novel
JOIN comic ON novel.title = comic.title
WHERE novel.title IN (
    SELECT name FROM Sugoi
    WHERE Year = '2023' AND rank < 3
) AND novel.count > 1000000;

```

```sql=
SELECT company, MAX(dailyNovelCount) AS maxDailyNovelCount
FROM (
    SELECT publisher.company, COUNT(*) AS dailyNovelCount
    FROM publisher
    JOIN novel ON publisher.company = novel.publisher_company
    WHERE novel.category = '日常系'
    GROUP BY publisher.company
) AS DailyNovelCounts;
```
```sql=

-- 找出符合條件的作者的得獎小說
SELECT novel.title, Sugoi.*
FROM novel
JOIN Sugoi ON novel.title = Sugoi.name
JOIN author ON novel.author_name = author.Name
WHERE author.age >= 50;

```
```sql=

-- 找出評論最多的幻想系輕小說
SELECT novel.title, novel.BookID, novel.heat, COUNT(*) AS commentCount
FROM novel
JOIN `group` ON novel.BookID = `group`.title
WHERE novel.category = '幻想系'
GROUP BY novel.title, novel.BookID, novel.heat
ORDER BY commentCount DESC
LIMIT 10;

```
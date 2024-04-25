---
title: chap 3 for 資料庫
tags: [資料庫]

---

# chap 3 for 資料庫
{%hackmd theme-dark %}
## Learning Resources
- A couple of interesting websites to check out, which teach SQL:
	- SQLZoo .net: 
		- http://sqlzoo.net
	- Tutorial on MySQL:
		- https://dev.mysql.com/doc/refman/8.0/en/tutorial.html

## SQL Data Definition
```sql=
instructor (
ID: string,
name: string,
dept_name: string,
salary: real
)
```
- char(n). Fixed length character string, with user-specified length n.
- varchar(n). Variable length character strings, with user-specified maximum length n.
- bit(n). Fixed length bit string, with user-specified length n.
- bit varying(n). Variable length bit string of user-specified length up to n.
- boolean. An attribute whose value is logical, including TRUE, FALSE, and UNKNOWN.
- int. Integer (a finite subset of the integers that is machine-dependent).
- smallint. Small integer (a machine-dependent subset of the integer domain type).
- numeric(p,d). Fixed point number, with user-specified precision of pdigits, with d digits to the right of decimal point. (ex., numeric(3,1), allows44.5 to be stores exactly, but not 444.5 or 0.32)
- real, double precision. Floating point and double-precision floating point numbers, with machine-dependent precision.
- float(n). Floating point number, with user-specified precision of at least ndigits
### Declaring Keys
- primary key (ID, course_id, sec_id, semester, year) 
- foreign key (ID) references student
- name varchar(20) unique
### And a Few More Relation Definitions
```sql=
create table instructor (
ID char(5) unique,
name varchar(20) not null,
dept_name varchar(20),
salary numeric(8,2),
primary key (ID),
foreign key (dept_name) references department)
```
### Updates to tables
-  Drop Table
	-  Delete a relation r
		-  drop table r
-  Alter Table
	-  alter table r add A D
		-  where A is the name of the attribute to be added to relation r and  D is the domain of A.
		-  All exiting tuples in the relation are assigned null as the value for  the new attribute. 
	- alter table r drop A 
		-  where A is the name of an attribute of relation r
		-  Dropping of attributes not supported by many databases
## Basic Query Structure of SQL Queries
```sql=
select A1, A2, ..., An
from r1, r2, ..., rm
where P;
```
```sql=
select *
from instructor, teaches;
```
```sql=
select distinct T.name
from instructor as T, instructor as S
where T.salary > S.salary and S.dept_name = 'Comp. Sci.’;

```
### String Operations (Cont.)

在資料庫中，我們可以使用不同的模式來進行字串比對。以下是一些範例：

1. `'Intro%'` 匹配以 "Intro" 開頭的任何字串。
2. `'%Comp%'` 匹配包含子字串 "Comp" 的任何字串。
3. `'_ _ _'` 匹配正好三個字元的任何字串。
4. `'_ _ _ %'` 匹配至少三個字元的任何字串。

在SQL中，我們可以進行各種字串操作，例如：

1. 連接字串（使用 "\||" 運算子）：
	 ```sql=
	 SELECT FirstName || ' ' || LastName AS FullName 
	 FROM Users;
	 ```
3. 將字串轉換為大寫或小寫：
	- 大寫
		```sql=
		SELECT UPPER(ColumnName) 
		FROM TableName;
		``` 
	- 小寫
		```sql=
		SELECT LOWER(ColumnName) 
		FROM TableName;
		``` 
5. 取得字串長度：
	 ```sql=
	 SELECT LENGTH(ColumnName) 
	 FROM TableName;```
7. 提取子字串：
	 ```sql=
	 SELECT SUBSTRING(ColumnName, start, length) 
	 FROM TableName;```

這些操作讓我們可以靈活地處理和比對字串，以滿足不同的資料需求。

### Ordering the Display of Tuple
#### 降序
```sql=
select * 
from novel
where novel.title in (select title from sugoi)
order by title desc
```
#### 升序
```sql=
select * 
from novel
where novel.title in (select title from sugoi)
order by title asc
```

## Additional Basic Operations

## Set Operations

## Default Values

## Null Values

## Aggregate Functions

## Nested Subqueries

## Modification of the Database





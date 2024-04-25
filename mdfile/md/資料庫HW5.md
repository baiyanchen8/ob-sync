---
title: 資料庫HW5
tags: [資料庫]

---



### 1-1
#### a
A ↠ B , A ↠ C,A ↠BC(違反4nf)
#### b
𝐴 ↠ 𝐵 and 𝐵 ↠ 𝐶𝐷.
𝐴 ↠ 𝐵CD(符合)
B ↠ CD(違反4nf)

### 1-2
#### a
R(A,C)R(A,B)R(A,D)
#### b
R(A,B),R(A,C,D)
## 2
### a
C → D、C → A
D → A
AB → C、AB → D
CB → D、CB → A
DB → C、DB → A
CD → A、AC → D
ACB → D
ADB → C
BCD → A
### b
AB → CD
C → A	,CB → AD
D → A ,BD → AC
candidate key={AB,BC,BD} 
### c
super key={ABC,ABD,BCD,ABCD}
## 3
### a
𝑅(𝐴, 𝐵, 𝐶,𝐷) with FDs 𝐴𝐵 → 𝐶, 𝐶 → 𝐷, and 𝐷 → 𝐴.
candidate key={AB,BC,BD} 
AB → CD
C → AD(不符合)
D → A(不符合)
R(B,C)R(A,C)R(A,D)
### b
𝑅(𝐴, 𝐵, 𝐶,𝐷) with FDs 𝐵 → 𝐶 and 𝐵 → D
AB → ACD
super key={AB,ABC,ABD,ABCD}
B → CD (不合格)
R(B,C,D)R(A,B)
### c
𝑅(𝐴, 𝐵, 𝐶,𝐷) with FDs 𝐴𝐵 → 𝐶, 𝐵𝐶 → 𝐷, 𝐶𝐷 → 𝐴, and 𝐴𝐷 → 𝐵.
super key={AB,BC,CD,AD}
合格

## 4
### a
```htmlmixed=
<?xml version="1.0" encoding="utf-8" standalone ="yes" ?>
<StarMovieData>
	<Star starID = "cf" starredIn = "sw esb rotj">	
		<Name>Carrie Fisher</Name>
		<Address>
			<Street>123 Maple St.</Street>
			<City>Hollywood</City>
		</Address>
		<Address>
			<Street>5 Locust Ln.</Street>
			<City>Malibu</City>
		</Address>
	</Star>
	<Star starID = "mh" starred In = "sw esb rotj">
		<Name>Mark Hamill</Name>
		<Address>
			<Street>456 Oak Rd. </Street>
			<City>Brentwood</City>
		</Address>
	</Star>
	<Movie movieID = "sw" starsOf = "cf mh">
		<Title>Star Wars</Title>
		<Year>1977</Year>
	</Movie>
	<Movie movieID="esb" starsOf="cf mh">
    <Title>The Empire Strikes Back</Title>
    <Year>1980</Year>
	</Movie>
	<Movie movieID="rotj" starsOf="cf mh">
			<Title>Return of the Jedi</Title>
			<Year>1983</Year>
	</Movie>
</StarMovieData>
```
### b
```htmlmixed=
<?xml version="1.0" encoding="utf-8" standalone ="yes" ?>
<StarMovieData>
	<Star starID = "cf" starredIn = "sw esb rotj">	
		<Name>Carrie Fisher</Name>
		<Address>
			<Street>123 Maple St.</Street>
			<City>Hollywood</City>
		</Address>
	<Address>
		<Street>5 Locust Ln.</Street>
		<City>Malibu</City>
	</Address>
	</Star>
	<Star starID = "mh" starred In = "sw esb rotj">
		<Name>Mark Hamill</Name>
		<Address>
			<Street>456 Oak Rd. </Street>
			<City>Brentwood</City>
		</Address>
	</Star>
	<Star starID="hf" starredIn="sw esb rotj">
		<Name>Harrison Ford</Name>
	</Star>	
	<Movie movieID = "sw" starsOf = "cf mh">
		<Title>Star Wars</Title>
		<Year>1977</Year>
	</Movie>
	<Movie movieID="esb" starsOf="cf mh">
    <Title>The Empire Strikes Back</Title>
    <Year>1980</Year>
	</Movie>
	<Movie movieID="rotj" starsOf="cf mh">
			<Title>Return of the Jedi</Title>
			<Year>1983</Year>
	</Movie>
	<Movie movieID="firewall" starsOf="hf">
			<Title>Firewall</Title>
			<Year>2006</Year>
	</Movie>
</StarMovieData>
```
### c
```htmlmixed=
<?xml version="1.0" encoding="utf-8" standalone ="yes" ?>
<StarMovieData>
	<Star starID = "cf" starredIn = "sw esb rotj hhs">	
		<Name>Carrie Fisher</Name>
		<Address>
			<Street>123 Maple St.</Street>
			<City>Hollywood</City>
		</Address>
		<Address>
			<Street>5 Locust Ln.</Street>
			<City>Malibu</City>
		</Address>
	</Star>
	<Star starID = "mh" starred In = "sw esb rotj">
		<Name>Mark Hamill</Name>
		<Address>
			<Street>456 Oak Rd. </Street>
			<City>Brentwood</City>
		</Address>
	</Star>
	<Star starID="hf" starredIn="sw esb rotj">
		<Name>Harrison Ford</Name>
	</Star>	
	<Movie movieID = "sw" starsOf = "cf mh">
		<Title>Star Wars</Title>
		<Year>1977</Year>
	</Movie>
	<Movie movieID="esb" starsOf="cf mh">
		<Title>The Empire Strikes Back</Title>
		<Year>1980</Year>
	</Movie>
	<Movie movieID="rotj" starsOf="cf mh">
		<Title>Return of the Jedi</Title>
		<Year>1983</Year>
	</Movie>
	<Movie movieID="firewall" starsOf="hf">
		<Title>Firewall</Title>
		<Year>2006</Year>
	</Movie>
	<Movie movieID="hhs" starsOf="cf">
		<Title>Hannah and Her Sisters</Title>
		<Year>1985</Year>
	</Movie>
</StarMovieData>
```

### d

```htmlmixed=
<?xml version="1.0" encoding="utf-8" standalone ="yes" ?>
<StarMovieData>
	<Star starID = "cf" starredIn = "sw esb rotj hhs">	
		<Name>Carrie Fisher</Name>
		<Address>
			<Street>123 Maple St.</Street>
			<City>Hollywood</City>
		</Address>
	<Address>
		<Street>5 Locust Ln.</Street>
		<City>Malibu</City>
	</Address>
	</Star>
	<Star starID = "mh" starred In = "sw esb rotj">
		<Name>Mark Hamill</Name>
		<Address>
			<Street>456 Oak Rd. </Street>
			<City>Brentwood</City>
		</Address>
	</Star>
	<Star starID="hf" starredIn="sw esb rotj">
		<Name>Harrison Ford</Name>
	</Star>	
	<Star starID="md" starredIn="bourne">
		<Name>Matt Damon</Name>
	</Star>	
	<Movie movieID = "sw" starsOf = "cf mh">
		<Title>Star Wars</Title>
		<Year>1977</Year>
	</Movie>
	<Movie movieID="esb" starsOf="cf mh">
		<Title>The Empire Strikes Back</Title>
		<Year>1980</Year>
	</Movie>
	<Movie movieID="rotj" starsOf="cf mh">
			<Title>Return of the Jedi</Title>
			<Year>1983</Year>
	</Movie>
	<Movie movieID="firewall" starsOf="hf">
			<Title>Firewall</Title>
			<Year>2006</Year>
	</Movie>
	<Movie movieID="hhs" starsOf="cf">
		<Title>Hannah and Her Sisters</Title>
		<Year>1985</Year>
	</Movie>
	<Movie movieID="bourne" starsOf="md">
			<Title>The Bourne Identity</Title>
			<Year>2002</Year>
	</Movie>
</StarMovieData>
```
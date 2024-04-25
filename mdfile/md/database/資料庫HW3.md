---
title: 資料庫HW3
tags: [資料庫]

---

# 資料庫HW3

1. Here are two relations:

    𝑅(𝐴, 𝐵): {(0,1), (2,3), (0,1), (2,4), (3,4)}

    𝑆(𝐵, 𝐶): {(0,1), (2,4), (2,5), (3,4), (0,2),(3,4)}

    Compute the following:

(a) $𝜋_{𝐴+𝐵,𝐴^2,B^2}(R)$

| A,B   | A+B | $A^2$ | $B^2$ |
| :---- | :-- | :---- | ----- |
| (0,1) | 1   | 0     | 1     |
| (2,3) | 5   | 4     | 9     |
| (0,1) | 1   | 0     | 1     |
| (2,4) | 6   | 4     | 16    |
| (3,4) | 7   | 9     | 16    |
ANS $𝐴+𝐵,𝐴^2,B^2$   ={(1, 0, 1), (5, 4, 9), (1, 0, 1), (6, 4, 16), (7, 9, 16)}

(b) $𝜋_{𝐵+1,𝐶−1}(𝑆)$ 

| B,C   | B+1 | C-1 |
|:----- |:--- |:----- |
| (0,1) | 1   | 0     |
| (2,4) | 3   | 3     |
| (2,5) | 3   | 4     |
| (3,4) | 4   | 3     |
| (0,2) | 1   | 1     |
| (3,4) | 4   | 3     |

ANS(𝐵+1,𝐶−1)={(1, 0), (3, 3), (3, 4), (4, 3), (1, 1), (4, 3)}

(c ) 𝑅⟕𝑆 

| R(A,B) | S(B,C) | 𝑅⟕𝑆(A,B,C) |
| ------ | ------ |:---------- |
| (0,1)  | NULL   | (0,1,NULL) |
| (2,3)  | (3,4)  | (2,3,4)    |
| (2,4)  | NULL   | (2,4,NULL) |
| (3,4)  | NULL   | (3,4,NULL) |

ANS(A,B,C)={(0,1,NULL), (2,3,4), (2,4,NULL), (3,4,NULL)}

(d) 𝑅⟖𝑆 

| S(B,C) | R(A,B) | 𝑅⟖𝑆(A,B,C) |
|:------ |:------ |:---------- |
| (0,1)  | NULL   | (NULL,0,1) |
| (2,4)  | NULL   | (NULL,2,4) |
| (2,5)  | NULL   | (NULL,2,5) |
| (3,4)  | (2,3)  | (2,3,4)    |
| (0,2)  | NULL   | (NULL,0,2) |


ANS(A,B,C)={(NULL,0,1),(NULL,2,4),(NULL,2,5),(2,3,4),(NULL,0,2)}

(e) 𝑅⟗S 

| R.A  | R.B  | S.B  | S.C  |
| ---- | ---- | ---- | ---- |
| 0    | 1    | null | null |
| 2    | 3    | 3    | 4    |
| 2    | 4    | null | null |
| 3    | 4    | null | null |
| null | null | 0    | 1    |
| null | null | 2    | 4    |
| null | null | 2    | 5    |
| null | null | 0    | 3    |

ANS(A,B,C)={(0,1,null),(2,3,4),(2,4,null),(3,4,null),(null,0,1),(null,2,4),(null,2,5),(null,0,3)}
1. The following running example of movie database has keys defined for all itsrelations.

    Movies(title, year, length, genre, studioName, producerC#)

    StarsIn(movieTitle, movieYear, starName)

    MovieStar(name, address, gender, birthdate)

    MovieExec(name, address, cert#, netWorth)

    Studio(name, address, presC#)

    Declare the following referential integrity constraints for the movie database as in this exercise.

    (a) A movie that appears in StarsIn must also appear in Movie. Handle violationsby rejecting the modification. (10%)

        出現在 Stars In 中的電影也必須出現在 Movie 中。 透過拒絕修改來處理違規行為。
    ```sql=1
    CREATE TABLE StarsIn (
        movieTitle char(255),
        movieYear INT,
        starName char(255),
        FOREIGN KEY (movieTitle, movieYear) REFERENCES Movies(title, year)
    );
    ```
    (b) A star appearing in StarsIn must also appear in MovieStar. Handle violations by deleting violating tuples

        出現在 StarsIn 中的明星也必須出現在 MovieStar 中。 透過刪除違規元組來處理違規行為
    ```sql=1
    create table starsIn(
        MovieTitle char(255),
        MovieYear int,
        StarName char(255),
        PRIMARY KEY(MovieTitle,MovieYear,StarName),
        FOREIGN KEY(StarName) REFERENCES movieStar(name) 
        ON DELETE CASCADE
    );
    ```
3. Write the following constraint for attributes of the relation.

    Movies(title, year, length, genre, studioName, producerC#)

    The studio name can only be Disney, Fox, MGM, or Paramount. (10%)
     ```sql=1
    create table Movies(
        title char(255),
        year int,
        length int,
        genre char(255),
        studioName char(255) ,
        producerC# int,
        CHECK (studioName IN ('Disney', 'Fox', 'MGM', 'Paramount'))
        );
    ```
4. Write the following constraints as tuple-based CHECK constraints on one of therelations of our running movies example:

    Movies(title, year, length, genre, studioName, producerC#)

    StarsIn(movieTitle, movieYear, starName)

    MovieStar(name, address, gender, birthdate)

    MovieExec(name, address, cert#, netWorth)

    Studio(name, address, presC#)

    If the constraint actually involves two relations, then you should put constraints in both relations so that whichever relation changes, the constraint will be checkedon insertions and updates. Assume no deletions; it is not always possible to maintain tuple-based constraints in the face of deletions

    (a) A name that appears in MovieStar must not also appear in MovieExec. (10%)
    ```sql=1
    ALTER TABLE MovieStar
    ADD CONSTRAINT Check_MovieExec
    CHECK (name not in (select DISTINCT name FROM MovieExec));
    
    ALTER TABLE MovieExec
    ADD CONSTRAINT Check_MovieStar
    CHECK (name not in (select DISTINCT name FROM MovieStar));
    ```
    (b) A Studio name that appears in Studio must also appear in at least one Movies tuple. (10%)
    ```sql=1
    ALTER TABLE Studio
    ADD CONSTRAINT Check_Movies
    CHECK (name IN (SELECT DISTINCT studioName FROM Movies));
    
    ALTER TABLE Movies
    ADD CONSTRAINT Check_Studio
    CHECK (studioName IN (SELECT DISTINCT Name FROM Studio));
    ```
5. Write the assertions for the following database schemas:

    Product(maker, model, type)

    PC(model, speed, ram, hd, price)

    Laptop(model, speed, ram, hd, screen, price)

    Printer(model, color, type, price)

    (a) If a laptop has a larger main memory than a PC, then the laptop must also have a higher price than the PC. (10%)
    ```mermaid 
    graph LR;
    A[PC.ram < Laptop.ram]-->B[Laptop.price > PC.price];
    ```
    ```sql=1
    create assertion check_laptop_pc_price
    check (not exists(
        select *   
        from  PC,Laptop
        where PC.ram<Laptop.ram and Laptop.price < PC.price;
    ));
    ```
    (b) If the relation Product mentions a model and its type, then this model must appear in the relation appropriate to that type. (10%)
    ```sql=1
    create assertion check_product
    check (not exists(
        select *   
        from  Product
        where (type ='PC' and model not in (select model from PC))
            or (type ='Laptop' and model not in (select model from Laptop))
            or (type ='Printer' and model not in (select model from Printer))
    ));
    ```
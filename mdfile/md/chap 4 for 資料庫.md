---
title: chap 4 for 資料庫

---

# chap 4 for 資料庫
{%hackmd theme-dark %}
### Cascading Actions in Referential Integrity
當違反參照完整性約束時，通常的程序是拒絕導致違規的操作。然而，在刪除或更新的情況下，有一種替代方法叫做「級聯（Cascade）」。

假設有一個 `course` 表格，其中的 `dept_name` 列是一個參照 `department` 表格的外部鍵，我們可以使用 `ON DELETE CASCADE` 和 `ON UPDATE CASCADE` 來定義級聯動作，以確保在 `department` 表格中相應的部門記錄被刪除或更新時，相應的 `course` 表格中的記錄也被處理。

以下是一個示例：

```sql
CREATE TABLE course (
  -- 其他列的定義...
  dept_name VARCHAR(20),
  FOREIGN KEY (dept_name) REFERENCES department(dept_name)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
```

在這個例子中，`dept_name` 列參照了 `department` 表格的 `dept_name` 列。使用 `ON DELETE CASCADE` 和 `ON UPDATE CASCADE` 表示，當參照的部門被刪除或更新時，相應的 `course` 表格中的記錄也將被刪除或更新。

另外，還有其他替代的動作，例如：

- `ON DELETE SET NULL`：當參照的部門被刪除時，將 `dept_name` 列設為 NULL。
- `ON DELETE SET DEFAULT <value>`：當參照的部門被刪除時，將 `dept_name` 列設為指定的默認值。

這些動作允許在違反參照完整性約束時，以不同的方式處理相關的記錄。

### Referential Integrity Violation
在考慮資料庫表格中的參照完整性約束時，有時可能需要在不觸發約束違規的情況下插入記錄。特別是當表格中的某些外部鍵參照相同表格中的其他記錄時，這種情況可能會發生。

舉例來說，考慮以下的 `person` 表格：

```sql
CREATE TABLE person (
  ID CHAR(10),
  name CHAR(40),
  mother CHAR(10),
  father CHAR(10),
  PRIMARY KEY (ID),
  FOREIGN KEY (father) REFERENCES person(ID),
  FOREIGN KEY (mother) REFERENCES person(ID)
);
```

在這裡，`father` 和 `mother` 列都是參照 `person` 表格中的 `ID` 列的外部鍵。如果我們想要插入一條記錄，而且希望避免參照完整性違規，可以採取以下方法：

1. **初始設置為 NULL：** 在插入記錄時，將 `father` 和 `mother` 的初始值設置為 NULL。這樣，一開始就不會違反參照完整性約束。然後，當所有人員記錄都已插入後，再進行相應的更新。

    ```sql
    -- 初始插入
    INSERT INTO person (ID, name, mother, father) VALUES ('1', 'John', NULL, NULL);

    -- 插入其他人員記錄...

    -- 後續更新
    UPDATE person SET father = 'A' WHERE ID = '1';
    UPDATE person SET mother = 'B' WHERE ID = '1';
    ```

2. **延遲約束檢查：** 在某些資料庫系統中，可以使用一種稱為延遲約束檢查的功能，允許在完成所有插入操作後才檢查約束。這樣，即使在插入時存在暫時的不一致性，系統也允許這種情況。

    詳細的語法和支持程度可能因資料庫系統而異，請查閱相應的資料庫文檔。
		
### Date and Time Types in SQL
在SQL中，有幾種不同的日期和時間類型，它們分別是：`date`、`time`、`timestamp`和`interval`。

1. **date（日期）:**
   - 存儲年、月、日信息。
   - 例子：`date '2005-07-27'`

2. **time（時間）:**
   - 存儲一天中的時間，包括時、分、秒。
   - 例子：`time '09:00:30'` 或 `time '09:00:30.75'`（包括毫秒）

3. **timestamp（日期和時間）:**
   - 存儲日期和時間信息。
   - 例子：`timestamp '2005-07-27 09:00:30.75'`

4. **interval（時間間隔）:**
   - 存儲一段時間的間隔。
   - 例子：`interval '1' day` 表示一天的時間間隔。

在進行日期、時間和時間戳的運算時，可以使用這些類型之間的運算。例如，將一個日期加上一個時間間隔，或是減去一個日期得到一個時間間隔。這樣的操作可以方便地處理時間相關的計算。

下面是一些操作的例子：

```sql
-- 將一個日期加上一個時間間隔
SELECT DATE '2023-01-01' + INTERVAL '3' month;

-- 減去一個日期得到一個時間間隔
SELECT TIMESTAMP '2023-01-01 12:00:00' - TIMESTAMP '2022-12-01 10:00:00';
```

這樣的特性使得在SQL中進行日期和時間相關的計算更加方便。


### Large-Object Types
在許多資料庫應用中，有時需要存儲大型數據項目，例如照片、視頻、CAD文件等。為了處理這樣的數據，資料庫系統提供了大型對象（Large Object，LOB）類型，其中包括 `blob` 和 `clob` 兩種。

1. **blob（二進制大對象）:**
   - 存儲大量未解釋的二進制數據。
   - 對於資料庫系統來說，blob 僅是一個巨大的二進制數據塊，其具體解釋由資料庫外的應用程序負責。
   - 例子：
     ```sql
     image BLOB(10MB);
     movie BLOB(2GB);
     ```

2. **clob（字符大對象）:**
   - 存儲大量字符數據。
   - 例子：
     ```sql
     book_review CLOB(10KB);
     ```

當執行查詢並返回一個大對象時，實際返回的是一個指針（指向大對象），而不是大對象本身。這樣的處理方式有助於提高性能，因為不需要在查詢執行時立即擷取整個大對象的內容。

例子：

```sql
-- 插入包含大對象的數據
INSERT INTO my_table (image) VALUES (TO_BLOB('binary data'));

-- 查詢並返回大對象的指針
SELECT image FROM my_table WHERE condition;
```

這樣的大型對象類型為資料庫應用提供了有效存儲和檢索大量二進制或字符數據的方法。

### User-Defined Types
在 SQL 中，使用 `CREATE TYPE` 語句可以創建用戶自定義的數據類型。以下是一個創建名為 "Dollars" 的數據類型的例子：

```sql
CREATE TYPE Dollars AS NUMERIC(12,2) FINAL;
```

這個數據類型 "Dollars" 定義為 NUMERIC，精度為 12 位，小數位為 2 位，並使用 FINAL 關鍵字表示它是最終的，即不能再進行繼承。

接下來，你可以在表格中使用這個自定義類型，例如：

```sql
CREATE TABLE department (
  dept_name VARCHAR(20),
  building VARCHAR(15),
  budget Dollars
);
```

在這個例子中，"department" 表格中的 "budget" 列使用了剛才定義的 "Dollars" 數據類型，確保存儲的數值具有指定的精度和小數位。

使用自定義數據類型的好處之一是它可以提高代碼的可讀性和重用性。例如，如果多個表格都需要存儲財務數據，可以使用相同的 "Dollars" 數據類型，而不必在每個表格中都重複相同的數據類型定義。
### User-Defined Domains
在 SQL-92 中，使用 `CREATE DOMAIN` 構造可以創建用戶自定義的域（domain）類型。域是一種用來定義數據類型和相關約束的結構。

以下是一個創建名為 "person_name" 的域類型的例子：

```sql
CREATE DOMAIN person_name CHAR(20) NOT NULL;
```

這個域類型 "person_name" 定義為 `CHAR(20)`，並帶有 `NOT NULL` 約束，表示這個域的值不能為空。

另外，域和類型在某種程度上是相似的，但域可以具有約束，例如 `NOT NULL`，這使得域更加靈活。

以下是一個創建名為 "degree_level" 的域類型的例子：

```sql
CREATE DOMAIN degree_level VARCHAR(10)
  CONSTRAINT degree_level_test CHECK (VALUE IN ('Bachelors', 'Masters', 'Doctorate'));
```

這個域類型 "degree_level" 定義為 `VARCHAR(10)`，同時帶有一個名為 "degree_level_test" 的約束，這個約束使用 `CHECK` 條件來確保域的值只能是 'Bachelors'、'Masters' 或 'Doctorate' 中的一個。

使用域的優勢之一是可以在域上定義一次性的約束，並在多個表格的列中重複使用這個域，提高了數據一致性和可維護性。


### Index Creation
在資料庫中，索引是一種數據結構，用於提高查詢效率。索引允許資料庫系統迅速找到擁有特定屬性值的元組，而無需遍歷所有元組。

以下是一個使用 `CREATE INDEX` 命令創建索引的例子：

```sql
CREATE INDEX idx_name ON table_name (attribute);
```

這裡的語法中：

- `idx_name` 是索引的名稱，可以是任何合法的標識符。
- `table_name` 是要創建索引的表格的名稱。
- `attribute` 是要在其上創建索引的屬性（欄位）。

舉例來說，如果有一個名為 `employees` 的表格，你可能希望在 `employee_id` 屬性上創建一個索引，以便更快地查找具有特定員工 ID 的記錄：

```sql
CREATE INDEX idx_employee_id ON employees (employee_id);
```

這樣，當你執行查詢時，資料庫系統可以使用索引快速定位符合條件的記錄，而不必掃描整個表格。

需要注意的是，儘管索引提高了查詢速度，但同時也會增加插入、更新和刪除的操作成本。因為在這些操作中，資料庫系統需要同步更新索引。因此，在選擇何時以及在哪些屬性上創建索引時，需要權衡考慮。

### Authorization
對於修改資料庫模式（schema）的授權，通常有一些特殊的權限形式。這些權限允許用戶對資料庫結構進行變更。以下是一些常見的資料庫模式修改權限形式：

1. **Index（索引）:**
   - 允許用戶創建和刪除索引，以加速查詢效率。
   - 例子：`CREATE INDEX` 和 `DROP INDEX` 權限。

2. **Resources（資源）:**
   - 允許用戶創建新的關係（表格）。
   - 例子：`CREATE TABLE` 權限。

3. **Alteration（修改）:**
   - 允許用戶對現有的關係（表格）進行結構修改，包括添加或刪除屬性（欄位）。
   - 例子：`ALTER TABLE` 權限。

4. **Drop（刪除）:**
   - 允許用戶刪除現有的關係（表格）。
   - 例子：`DROP TABLE` 權限。

以下是一個授予或撤銷這些資料庫模式修改權限的例子：

```sql
-- 授予創建索引權限
GRANT CREATE INDEX ON table_name TO user_name;

-- 授予創建新表格權限
GRANT CREATE TABLE ON database_name TO user_name;

-- 授予修改表格結構權限
GRANT ALTER TABLE ON table_name TO user_name;

-- 授予刪除表格權限
GRANT DROP TABLE ON table_name TO user_name;
```

同樣，用戶也可以通過 `REVOKE` 命令來撤銷這些資料庫模式修改權限。

```sql
-- 撤銷創建索引權限
REVOKE CREATE INDEX ON table_name FROM user_name;
```

這樣的權限控制確保了對資料庫模式的修改受到有權負責的用戶的控制，防止了意外或非授權的模式更改。

### Authorization Specification in SQL
在SQL中，使用 `GRANT` 语句来授予权限。该语句的一般形式如下：

```sql
GRANT <privilege list> ON <relation or view> TO <user list>;
```

其中：

- `<privilege list>` 表示要授予的权限列表，可以是一个或多个权限，如 `SELECT`、`INSERT`、`UPDATE`、`DELETE` 等。
- `<relation or view>` 表示要授予权限的表格或视图。
- `<user list>` 表示被授予权限的用户列表，可以是用户ID、`PUBLIC`（允许所有有效用户）、角色等。

举例来说，如果要授予用户 Amit 和 Satoshi 对 department 表的 `SELECT` 权限，可以这样写：

```sql
GRANT SELECT ON department TO Amit, Satoshi;
```

需要注意的是，在授予权限时，对视图的权限并不意味着对底层关系的权限。授予权限的用户（grantor）必须已经对指定的项拥有相应的权限，或者是数据库管理员。

此外，SQL中还涉及到角色（role）的概念，角色是一组权限的集合，可以通过将角色授予用户而不是直接将权限授予用户来简化授权管理。这使得在有多个用户时更容易维护和管理权限。

总体而言，`GRANT` 语句使得数据库管理员能够灵活地管理用户对数据库的访问权限，确保了安全性和数据完整性。

### Privileges in SQL

在 SQL 授予权限时，一些常见的权限以及其含义如下：

1. **SELECT（查询）:**
   - 允许用户读取关系的内容，或者使用视图进行查询。
   - 示例：授予用户 U1、U2 和 U3 对 instructor 关系的查询权限。
     ```sql
     GRANT SELECT ON instructor TO U1, U2, U3;
     ```

2. **INSERT（插入）:**
   - 允许用户插入新的元组。
   - 示例：授予用户插入权限。
     ```sql
     GRANT INSERT ON table_name TO user_name;
     ```

3. **UPDATE（更新）:**
   - 允许用户使用 SQL 的 UPDATE 语句进行更新操作。
   - 示例：授予用户更新权限。
     ```sql
     GRANT UPDATE ON table_name TO user_name;
     ```

4. **DELETE（删除）:**
   - 允许用户删除元组。
   - 示例：授予用户删除权限。
     ```sql
     GRANT DELETE ON table_name TO user_name;
     ```

5. **ALL PRIVILEGES（所有权限）:**
   - 用于一次性授予所有允许的权限。
   - 示例：授予用户所有权限。
     ```sql
     GRANT ALL PRIVILEGES ON table_name TO user_name;
     ```

这些权限提供了细粒度的访问控制，数据库管理员可以根据需求为不同的用户或角色分配适当的权限。这有助于确保对数据库的安全访问，并限制用户对数据的修改、删除等操作。
### Revoking Authorization in SQL
在 SQL 中，使用 `REVOKE` 语句来撤销授权。该语句的一般形式如下：

```sql
REVOKE <privilege list> ON <relation or view> FROM <user list>;
```

其中：

- `<privilege list>` 表示要撤销的权限列表，可以是一个或多个权限，如 `SELECT`、`INSERT`、`UPDATE`、`DELETE` 等。
- `<relation or view>` 表示要撤销权限的表格或视图。
- `<user list>` 表示被撤销权限的用户列表，可以是用户ID、`PUBLIC`（所有用户），角色等。

举例来说，如果要撤销用户 U1、U2 和 U3 对 student 表的 `SELECT` 权限，可以这样写：

```sql
REVOKE SELECT ON student FROM U1, U2, U3;
```

需要注意的是：

- `<privilege list>` 可以是 `ALL`，表示撤销被撤销者可能拥有的所有权限。
- 如果 `<user list>` 中包含 `PUBLIC`，那么除了明确被授予权限的用户外，所有用户都会失去该权限。
- 如果同一用户**被不同的授权者两次授予相同的权限**，那么在撤销权限后，用户可能仍然保留该权限。
- 所有依赖于被撤销权限的其他权限也会一并被撤销。

撤销权限是一种重要的安全措施，允许管理员在需要时调整用户对数据库的访问权限。这有助于确保只有合适的用户能够执行特定的操作。

### Roles
在数据库管理系统中，角色（role）是一种区分不同用户在数据库中可以访问/更新什么内容的方式。通过角色，数据库管理员可以将一组权限捆绑到一个角色上，然后将用户分配给这个角色，从而简化权限管理。

以下是在 SQL 中创建和使用角色的一般步骤：

1. **创建角色：**
   使用 `CREATE ROLE` 语句来创建一个角色，语法如下：

   ```sql
   CREATE ROLE role_name;
   ```

   例如，创建一个名为 "instructor" 的角色：

   ```sql
   CREATE ROLE instructor;
   ```

2. **分配用户给角色：**
   使用 `GRANT` 语句将用户分配给角色，语法如下：

   ```sql
   GRANT role_name TO user_name;
   ```

   例如，将用户 "U1" 分配给角色 "instructor"：

   ```sql
   GRANT instructor TO U1;
   ```

通过分配角色而不是直接分配权限，可以更轻松地管理大量用户的权限。如果需要修改一组用户的权限，只需修改与角色相关的权限即可，而不必逐个修改用户的权限。

同时，角色还可以与其他角色相关联，形成角色层次结构，从而更灵活地管理权限。

需要注意的是，具体数据库管理系统可能有一些差异，上述语法可能需要根据使用的数据库系统进行调整。
### Roles Example
以下是一系列在 SQL 中创建角色、将用户分配给角色、以及授予角色权限的操作，(大概可分組)：

1. **创建角色 "instructor"：**
   ```sql
   CREATE ROLE instructor;
   ```

2. **将用户 "Amit" 分配给角色 "instructor"：**
   ```sql
   GRANT instructor TO Amit;
   ```

3. **授予角色 "instructor" 对 "takes" 表的 `SELECT` 权限：**
   ```sql
   GRANT SELECT ON takes TO instructor;
   ```

4. **创建角色 "teaching_assistant"：**
   ```sql
   CREATE ROLE teaching_assistant;
   ```

5. **将角色 "teaching_assistant" 授予角色 "instructor"：**
   ```sql
   GRANT teaching_assistant TO instructor;
   ```

6. **角色 "instructor" 继承了角色 "teaching_assistant" 的所有权限：**
   - 此时，角色 "instructor" 具有对 "takes" 表的 `SELECT` 权限，因为角色 "teaching_assistant" 被授予了该权限。

7. **创建角色 "dean"：**
   ```sql
   CREATE ROLE dean;
   ```

8. **将角色 "instructor" 授予角色 "dean"：**
   ```sql
   GRANT instructor TO dean;
   ```

9. **将角色 "dean" 授予用户 "Satoshi"：**
   ```sql
   GRANT dean TO Satoshi;
   ```

通过这些操作，形成了一条角色链：Satoshi 继承了 dean 的权限，而 dean 又继承了 instructor 的权限，而 instructor 则继承了 teaching_assistant 的权限，最终包括对 "takes" 表的 `SELECT` 权限。

这种角色和权限的管理方式使得权限的分配和维护更加灵活和可管理。

### Authorization on Views
在上述情境中，首先创建了一个名为 "geo_instructor" 的视图，然后对该视图进行了授权，接着考虑了在没有对底层表 "instructor" 授予权限的情况下查询视图的后果。

1. **创建名为 "geo_instructor" 的视图：**
   ```sql
   CREATE VIEW geo_instructor AS
   (SELECT *
    FROM instructor
    WHERE dept_name = 'Geology');
   ```

2. **授予对 "geo_instructor" 视图的 `SELECT` 权限给 "geo_staff"：**
   ```sql
   GRANT SELECT ON geo_instructor TO geo_staff;
   ```

在这一点上，假设一个 "geo_staff" 成员发起以下查询：
```sql
SELECT *
FROM geo_instructor;
```

接下来考虑两种情况：

- 如果 "geo_staff" 在 "instructor" 表上没有相应的权限：
  - 系统在开始处理查询之前必须检查 "geo_staff" 对该查询的授权。
  
- 如果创建 "geo_instructor" 视图的用户在 "instructor" 表上没有相应的权限：
  - 如果一个用户创建一个视图，而对底层表的权限无法授予，系统将拒绝创建视图的请求。
  - 在这个例子中，"geo_instructor" 视图的创建者必须对 "instructor" 表具有 `SELECT` 权限。

这种授权的链式传递和视图依赖于底层表的权限确保了访问的安全性和一致性。如果有人试图访问视图，系统将检查他们是否具有执行该视图所依赖的所有表上相应的权限。

### Other Authorization Features
在 SQL 中，`REFERENCES` 特权用于创建外键（foreign key）。通过 `REFERENCES` 特权，用户可以在一个表的列上创建外键，该列引用了另一张表的主键。

例如，授予在 `department` 表上的 `dept_name` 列上的 `REFERENCES` 特权给用户 Mariano，语法如下：

```sql
GRANT REFERENCES (dept_name) ON department TO Mariano;
```

为什么需要这样的特权呢？

考虑到外键的作用，外键约束会对引用表（referenced relation）上的删除和更新操作进行限制。如果用户 Mariano 在 `department` 表上创建了一个外键，这个外键的存在将对其他用户未来对被引用表的操作施加一定的限制。

为了避免潜在的权限问题，创建外键的用户需要有足够的特权，包括在引用表上的 `REFERENCES` 特权。这确保了创建外键的用户具有足够的权限来对引用表进行相应的操作。

此外，SQL 还支持将授予的权限传递给其他用户的功能。例如，如果我们希望允许用户 Amit 具有对 `department` 表的 `SELECT` 特权，并允许他将这个特权传递给其他用户，可以使用以下语法：

```sql
GRANT SELECT ON department TO Amit WITH GRANT OPTION;
```

这就是 `WITH GRANT OPTION` 的作用，它允许被授权的用户将相同的特权再次授予给其他用户。这种特性使得权限的管理更加灵活。
### Other Authorization Features (Cont.)
在数据库中，从用户或角色中撤销权限可能导致其他用户或角色也失去相同的权限。在大多数数据库系统中，级联是默认行为。然而，`REVOKE` 语句可以使用 `RESTRICT` 关键字，以防止级联回收：

```sql
REVOKE SELECT ON department FROM Amit, Satoshi RESTRICT;
```

这表示只有明确授予了该权限的用户才会失去该权限。相反，如果使用 `CASCADE` 关键字，撤销将级联进行，而不仅仅是影响直接授予权限的用户：

```sql
REVOKE SELECT ON department FROM Amit, Satoshi CASCADE;
```

实际上，`CASCADE` 是默认的行为，因此在许多数据库系统中，您可以省略关键字而达到相同的效果：

```sql
REVOKE SELECT ON department FROM Amit, Satoshi;
```

级联回收权限时需要小心，以确保不会意外地影响其他用户或角色。选择使用 `RESTRICT` 还是 `CASCADE` 取决于具体情境和需求。

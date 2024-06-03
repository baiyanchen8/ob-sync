## 架構
![[Drawing 2024-06-02 22.10.02.excalidraw]]

## 實驗流程
直接使用上次大概aiot2作業的code上手更改，因此本實驗並未使用chatgpt
### 上次的內容(aiot2)
![[即時溫度.png]]
### step 1 測試在樹莓派在該網路上的ip
![[使用vnc.png]]

### step2 對esp32 修改
![[螢幕快照_2024-03-19_18-25-12.png]]

### Step 3 新增後端選取特定時間段資料的功能
**功能：** 前端可以要求在某個時間段的資料要求後端這個function 回傳
```python
# new 
@app.route('/get_range_data', methods=['GET'])
def get_range_data():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    print("TIMEE",start_time,end_time)
    a=start_time.split("T")
    start_time=a[0]+" "+a[1]
    a=end_time.split("T")
    end_time=a[0]+" "+a[1]

    print("TIMEE",start_time,end_time)
    db, cursor = get_db()
    try:
        cursor.execute("SELECT * FROM sensor_data WHERE tim1 BETWEEN ? AND ?", (start_time, end_time))
        data = cursor.fetchall()
        if data:
            temperature_data = []
            humidity_data = []
            time_data = []
            print(data)
            for row in data:
                temperature_data.append(row[1])
                humidity_data.append(row[2])
                time_data.append(row[3])
            print(temperature_data,humidity_data,time_data)
            return jsonify({'temperature': temperature_data, 'humidity': humidity_data, 'time': time_data})
        else:
            return jsonify({'error': 'No data available for the specified time range'})
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
```

### Step 4 新增在前端可以選取要什麼時間的功能
#### 後端 method, 往前端送可以選的時段
```python
@app.route('/get_day', methods=['GET'])
def get_day():
    db, cursor = get_db()
    if not db or not cursor:
        return jsonify({'error': '資料庫連接失敗'}), 500
    try:
        # 使用 DATE 函數提取日期部分
        cursor.execute("SELECT DISTINCT DATE(tim1) FROM sensor_data")
        data = cursor.fetchall()
        if data:
            # 轉換日期格式
            days = [datetime.datetime.strptime(row[0], "%Y-%m-%d").strftime("%Y-%m-%d") for row in data]
            return jsonify({'days': days})
        else:
            return jsonify({'error': '無可用日期資料'})
    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
```

#### 在前端使用toggle list 選擇
![[toggle.png]]

![[螢幕快照_2024-06-02_22-33-57.png]]

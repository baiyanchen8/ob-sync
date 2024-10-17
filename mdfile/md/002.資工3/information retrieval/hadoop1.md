---
tags:
  - IR
---

#### hadoop code 複製
使用git
```bash
 git clone https://github.com/UDICatNCHU/hadoop_tutorial.git
```
如果 git 不下來則使用下面的
```bash
wget -O hadoop_code.zip https://www.dropbox.com/scl/fi/qou69ifdt1unnzw9058fq/hadoop_tutorial-master.zip?rlkey=u1oatjxetwg35zwnsdckxjqx8&dl=0

unzip hadoop_code.zip
```
### 進入hadoop 
```bash
cd hadoop_tutorial
```

![[Pasted image 20240513144608.png]]
![[Pasted image 20240513144608.png]]
1. **fs** 指的是對 file system 操作
2.  `-` 後面放的是要做時麼操作
3. 將**speech**放到 **speech@hdfs** 
```
$hadoop fs -put speech 
```

![[Pasted image 20240513144831.png]]

![[Pasted image 20240513145130.png]]


#### 回收檔案
```bash
$hadoop fs -get speech@hdfs speechlocal
```
抓取**speech@hdfs** 放到檔案**speechlocal**   

### 執行
```bash
hadoop jar hadoop-examples-1.2.1.jar wordcount speech@hdfs speechresult
```
1. 執行 java 檔使用 jar
2. **hadoop-examples-1.2.1.jar** 為函式庫 （教授提供的）
3. **wordcount** 要執行的程式
4. **speech@hdfs** 為執行需求檔案
5. **speechresult** 執行完檔案放置的地方

### 如何編譯
![[Pasted image 20240513151436.png]]
1. java 檔放置於 src 資料夾
2. 執行完的函式會在 output.jar
3. 使用 ant 在`hadoop_tutorial` 直接編譯即可
![[Pasted image 20240513152105.png]]

### 如何寫一個 hadoop java
要有3 個 method 
1. map
2. reduce 
3. main 
執行順序為 map -> reduce


```java= fold
import java.io.IOException;
import java.util.*;
        
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
        
public class asd {
        
 public static class Map extends Mapper<LongWritable, Text, Text, LongWritable> {
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        StringTokenizer tokenizer = new StringTokenizer(line);
        while (tokenizer.hasMoreTokens()) {
            String token = tokenizer.nextToken();
            context.write(new Text("sum"), new LongWritable(Long.parseLong(token)));
        }
    }
 } 
        
 public static class Reduce extends Reducer<Text, LongWritable, Text,LongWritable> {

    public void reduce(Text key, Iterable<LongWritable> values, Context context) 
      throws IOException, InterruptedException {
        long sum = 0;
        for (LongWritable val : values) {
	    sum += val.get();
        }
        context.write(key, new LongWritable(sum));
    }

 }
        
 public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
        
        Job job = new Job(conf, "wordcount");
    
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(LongWritable.class);
        
    job.setMapperClass(Map.class);
    job.setReducerClass(Reduce.class);
    job.setJarByClass(WordCount.class);
        
    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);
        
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
    job.waitForCompletion(true);
 }
        
}

```


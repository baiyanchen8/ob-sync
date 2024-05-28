---
title: oslab-9
tags: [os]

---

# oslab-9

## 簡介
這次實驗是做thread management，有用C-pthread & java thread
## Pthread
- 函式庫
	- `#include <pthread.h>`
	- `pthread_create((pthread_t) &p1,(const pthread_att_t) p2,(void *) p3,(void*) p4);`
		- thread 創建
		- p1 pthread_t id
		- p2 通常為 NULL
		- p3 為 thread 中要執行的 method (type : 指標)
		- p4 為 傳遞參數 (必須要用指標)
	-  `pthread_self(void);`
		- 在thread 中獲取 thread id (type: pthread_t)
	- `pthread_join(pthread_t id,(void*) &result);`
		- id 要放入 thread id
		- result 回傳result (type : 指標)
		- 在 thread 執行完前，程式將在這裡 wait
	- `pthread_exit((void*) result);`
		- will exit thread
		- will return result (type :指標)
		- 可以用 return 代替
	- `pthread_equal(pthread_t id1,pthread_t id2);`
		- 用於比較 id1 是否相同於 id2
		- if equal
			- return a nonzero value
		- if not
			- return 0
### lab 1
> 
- 使用Pthreads建立四個相同的執行緒。同時宣告一個全域變數count = 0。主
- 每個執行緒將相同的全域變數遞增25,000,000次
	- 每個線程列印其線程 ID及其結束時count的數量。
	- 因此計數總共增加了 100,000,000 次。
- Use C language(you don't need to fix lock)

>  code lab1
```c=1
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
int count=0;

void *thread1(void * arg){
	int i=0;
	for(i=0;i<25000000;i++){
		count +=1;
	}
	printf("thread number:%lu count:%d\n",pthread_self(),count);

}
int main(){
	pthread_t p1,p2,p3,p4;
	
	pthread_create(&p1,NULL,thread1,NULL);
	pthread_create(&p2,NULL,thread1,NULL);
	pthread_create(&p3,NULL,thread1,NULL);
	pthread_create(&p4,NULL,thread1,NULL);
	
	pthread_join(p1,NULL);
	pthread_join(p2,NULL);
	pthread_join(p3,NULL);
	pthread_join(p4,NULL);
	printf("%d\n",count);
}
```


![image.png](HkZP2gtmp.png)



### Lab1-1
info

- 問題：
	- 觀察你得到的所有結果(多次執行lab1)，並思考什麼它有什麼問題嗎？
	- 透過執行所有相同的操作來與 fork() 流程進行比較全域變量，你能看出有什麼差別嗎它們之間？

>  code for fork
```c=1
# include <stdio.h>
# include <unistd.h>
# include <sys/wait.h>
# include <stdlib.h>
int count=0;
void thread1(){
	int i=0;
	for(i=0;i<25000000;i++){
		count +=1;
	}
	printf("child number:%d count:%d\n",getpid(),count);
}
int main(){
	
	pid_t newpid1;
	newpid1= fork();
	if (newpid1 ==0){
		thread1();
		return 0;
	}
	pid_t newpid2;
	newpid2= fork();
	if (newpid2 ==0){
		thread1();
		return 0;
	}
	pid_t newpid3;
	newpid3= fork();
	if (newpid3 ==0){
		thread1();
		return 0;
	}
	pid_t newpid4;
	newpid4= fork();
	if (newpid4 ==0){
		thread1();
		return 0;
	}
	wait(NULL);
	wait(NULL);
	wait(NULL);
	wait(NULL);
	printf("%d\n",count);
	return 0;
}
```

![image.png](BkhxfZtX6.png)

> ANS:
> 1. 每次執行都不滿100,000,000 
	> 原因: thread 之間會共用資源，導致在相加時會互搶，最終使答案不滿100,000,000 
> 2. 由於process之間並不共享資源所以結果最高只會在各個process中到25000000

## Java thread
### method 1 `implement Runnable`
![image](rkzDELb_6.png)

### method 2	`extends Thread`
![image](SkBUEIZua.png)

### Thread 函式庫
`Thread.currentThread().getName()`可以get thread number

### lab2
![image.png](HksYGbK76.png)
>  lab2 code
```java=1  
public class ThreadEx {
	public static void main(String[] args) {
		ShareData s1 =new ShareData();
		Thread t1=new Thread(s1);
		Thread t2=new Thread(s1);
		t1.start();
		t2.start();
		Thread t3=new Thread(s1);
		Thread t4=new Thread(s1);
		t3.start();
		t4.start();
		try{
			t1.join();	
		}catch (InterruptedException ie) {
		System.err.println(ie);
		}
		
		try{
			t2.join();	
		}catch (InterruptedException ie) {
		System.err.println(ie);
		}
		try{
			t3.join();	
		}catch (InterruptedException ie) {
		System.err.println(ie);
		}
		
		try{
			t4.join();	
		}catch (InterruptedException ie) {
		System.err.println(ie);
		}
		int ans =s1.i;
		System.out.println("final:"+ans);
	}
}
class ShareData implements Runnable {
	int i=0;
	public void run(){
		int k=0;
		for(k=0;k<250000;k++)
		{
		i++;
		}
		System.out.println(Thread.currentThread().getName()+":"+i);
	}
}

```

![image.png](HylumZFXa.png)
### lab 3
![image](By6CgKbua.png)

> 
> - Ｑ：請用c的msg queue實現雙向溝通。
> - 細節規範: 
>	- 要寫兩個程式
>	- 每個程式要有兩個thread，其中一個負責接收，另一個負責發送訊息
>	- 總共只能使用一個msg queue

> 解題思路:
> 1. 兩個程式都要接收&發送msg，所以兩個程式幾乎可以一模一樣
> 2. 其中會遇到自己送出去的msg由自己收到，解法為在字串前新增獨特的編號，在收到訊息時先確認編號，如果編號錯誤就重新發送直至成功
>  code
```c=1
# include  <fcntl.h>
# include  <mqueue.h>
# include  <stdio.h>
# include  <string.h>
# include  <stdlib.h>
#include <pthread.h>

# define NAME "/myMsgQueue"
# define MAX_MSGSIZE 1000
# define port "ATOB" // ID編號
void *send_t(void * arg);
void *reve_t(void * arg);
void sent(char *str);
int main(){
	pthread_t p1,p2;	
	pthread_create(&p1,NULL,send_t,NULL);
	pthread_create(&p2,NULL,reve_t,NULL);
	//由 receiver 確認是否結束
	pthread_join(p2,NULL);
	return 0;
}
void *send_t(void * arg){
	mqd_t mqd =mq_open(NAME,O_WRONLY|O_CREAT ,0644,NULL);
	if  (mqd ==-1){
		perror("fail to open or create the msg queue.\n");
		return 0;
	}	
	printf("send to receiver:\n");
	int x=1;
	while(x==1){
		char buffer[MAX_MSGSIZE];
		int i;
		for (i=0;i<MAX_MSGSIZE;i++){
			buffer[i]='\0';
		}
		strcat(buffer,port);
		printf("> " );
		char buffer1[MAX_MSGSIZE];
		fgets(buffer1,MAX_MSGSIZE,stdin);
		strcat(buffer,buffer1);


		int send = mq_send(mqd,buffer,strlen(buffer)+1,0);
		if (send ==-1 ){
			perror("fail to send the msg queue.\n");
			return 0;
		}
		if (buffer[0+4]=='e'&&buffer[1+4]=='x'&&buffer[2+4]=='i'&&buffer[3+4]=='t'){
			x=0;
			//當已經對對方發送結束訊號
			//也需要對自身發送訊號
			//(因為程式結束是靠receiver)
			sent("aaaaexit");
		}
	}
	return 0;
}
void sent(char *str){
mqd_t mqd =mq_open(NAME,O_WRONLY|O_CREAT ,0644,NULL);
int send = mq_send(mqd,str,strlen(str)+1,0);
}
void *reve_t(void * arg){
	mqd_t mqd =mq_open(NAME,O_RDONLY|O_CREAT ,0644,NULL);
	if  (mqd ==-1){
		perror("fail to open or create the msg queue.\n");
		return 0;
	}	
	int x=1;
	while(x==1){
		char buffer[MAX_MSGSIZE] ;
		ssize_t msg_size =mq_receive(mqd,buffer,8192,NULL);
		if (msg_size==-1){
			printf("fail to read msg. \n");
			return 0;
		}
		if (strncmp(buffer,port,4)==0){
			// 確認編號非自身
			sent(buffer);
			continue;
		}
		if (buffer[0+4]=='e'&&buffer[1+4]=='x'&&buffer[2+4]=='i'&&buffer[3+4]=='t'){	
			//接收跳出訊號結束程式
			x=0;
			printf("EXIT\n");
			break;
		}
		
		printf("recevied :%s \n",buffer+4);
		
	}
	return 0;
}
```

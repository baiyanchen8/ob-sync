---
title: oslab10
tags: [os]

---

# oslab10

## fork-join model
通過 fork and join 的形式可以加速許多問題的解決速度
> 10-1
```java=
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.stream.LongStream;
import java.util.Arrays;
import java.util.Random;
public class ThreadEx {
	public static void main(String[] args) {
		int[] arr=new int [100];
		Random rd=new Random();
		for (int i=0;i<100;i++){
			arr[i]=i;
		
		}
		for (int i=99;i>-1;i--){
			int j=rd.nextInt(i+1)+1;

			int tmp=arr[i];
			arr[i]=arr[j];
			arr[j]=tmp;
		
		}
		System.out.println(Arrays.toString(arr));
		new_fork rightTask = new new_fork(arr);
		int[] rr=rightTask.compute();

		System.out.println(Arrays.toString(rr));
	}
	
}

class new_fork extends RecursiveTask<int[]>{
		private final int[] arr;
		public new_fork(int[] arr){
			this.arr=arr;
		
		}
		protected int[] compute(){
			if(arr.length<=1){
				return arr;
			}
			int mid = arr.length / 2;

		    int[] left = Arrays.copyOfRange(arr, 0, mid);
		    int[] right = Arrays.copyOfRange(arr, mid, arr.length);

		    new_fork leftTask = new new_fork(left);
		    new_fork rightTask = new new_fork(right);

		    invokeAll(leftTask, rightTask);

		    int[] merged = merge(leftTask.join(), rightTask.join());

		    return merged;
		
		
		
		}
		public int[] merge(int []left,int [] right){
		
			int lf=0,ri=0,k=0;
			int[] result = new int[left.length + right.length];
			while(lf <left.length&&ri< right.length){
			
			if (left[lf]<right[ri]){
				result[k++]=left[lf++];
			}else{
				result[k++]=right[ri++];
			
			}
			
			}
			while (lf < left.length) {
		        result[k++] = left[lf++];
		    }

		    while (ri < right.length) {
		        result[k++] = right[ri++];
		    }
			return result;
		} 
	}

```

> 10-2-1
```c=1
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<pthread.h>
int glob = 0;
void *function(void *arg){
glob+=(int)arg;
printf("thread_ID = %lu,glob= %d\n",pthread_self(),glob);
pthread_exit(NULL);
}

int main(){

pthread_t id[2];
pthread_create(&id[0],NULL, function, 50);pthread_join(id[0],NULL);
pthread_create(&id[1], NULL, function, 50);pthread_join(id[1],NULL);


return 0;
}
```

> 10-2-2

```c=1
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
void *child(void *arg){
    pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);
    int *input = (int*) arg;
    int *result = malloc(sizeof(int) * 1);
    result[0] = input[0] + input[1];
    int i = 1;
    while (i<4){
        sleep(1);
        printf("睡眠：%d秒\n", i++);
    }
    pthread_exit((void *)result);
}
int main(){
    pthread_t t;
    int input[2] = {1, 2};
	int *result;
    pthread_create(&t, NULL, child, (void*)input);
    pthread_cancel(t);
	pthread_join(t,&result);
    printf("%d + %d = %d\n", input[0], input[1], result[0]);
    free(result);
    return 0;
}
```

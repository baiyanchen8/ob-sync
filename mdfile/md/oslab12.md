---
title: oslab12
tags: [os]

---

# oslab12

	
>  lab1
```clike=
#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

sem_t mutex;  // 宣告未命名的 semaphore
int count = 0;
void inc(void);
void dec(void);

int main(void) {
    int i = 0;
    pthread_t id[4];
    // 初始化 semaphore，初始值為 1
    sem_init(&mutex, 0, 1);
    // 建立四個執行緒
    pthread_create(&id[0], NULL, (void *)dec, NULL);
    pthread_create(&id[1], NULL, (void *)inc, NULL);
    pthread_create(&id[2], NULL, (void *)dec, NULL);
    pthread_create(&id[3], NULL, (void *)inc, NULL);

    // 等待四個執行緒執行完畢
    for (i = 0; i < 4; i++) {
        pthread_join(id[i], NULL);
    }
    // 顯示最終結果
    printf("\n最終結果是 %d\n", count);
    // 釋放 semaphore 資源
    sem_destroy(&mutex);
    pthread_exit(NULL);
}

void inc() {
    int i = 0;
    for (i = 0; i < 25000000; i++) {
        sem_wait(&mutex);  // 進入臨界區前等待
        count++;
        sem_post(&mutex);  // 離開臨界區後釋放
    }
    pthread_exit(NULL);
}

void dec() {
    int i = 0;
    for (i = 0; i < 25000000; i++) {
        sem_wait(&mutex);  // 進入臨界區前等待
        count--;
        sem_post(&mutex);  // 離開臨界區後釋放
    }
    pthread_exit(NULL);
}

```
> 



>  lab2
```clike=
#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
sem_t *mutex;  // 宣告未命名的 semaphore
int count = 0;
void inc(void);
void dec(void);
int main(void) {
    int i = 0;
    pthread_t id[4];
    // 初始化 semaphore，初始值為 1
    mutex = sem_open("/mysem",O_CREAT,0644,1);
    // 建立四個執行緒
    pthread_create(&id[0], NULL, (void *)dec, NULL);
    pthread_create(&id[1], NULL, (void *)inc, NULL);
    pthread_create(&id[2], NULL, (void *)dec, NULL);
    pthread_create(&id[3], NULL, (void *)inc, NULL);

    // 等待四個執行緒執行完畢
    for (i = 0; i < 4; i++) {
        pthread_join(id[i], NULL);
    }
    // 顯示最終結果
    printf("\n最終結果是 %d\n", count);
    // 釋放 semaphore 資源
    sem_close(mutex);
	sem_unlink("\mysem");
    pthread_exit(NULL);
}

void inc() {
    int i = 0;
    for (i = 0; i < 5; i++) {
        sem_wait(mutex);  // 進入臨界區前等待
        count++;
        printf("count:%d\n",count);
        sem_post(mutex);  // 離開臨界區後釋放
    }
    pthread_exit(NULL);
}
void dec() {
    int i = 0;
    for (i = 0; i < 5; i++) {
        sem_wait(mutex);  // 進入臨界區前等待
        count--;
        printf("count:%d\n",count);
        sem_post(mutex);  // 離開臨界區後釋放
    }
    pthread_exit(NULL);
}
```
> 
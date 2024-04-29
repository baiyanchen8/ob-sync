---
title: oslab13
tags:
  - os
---

# oslab13

> lab1
```c=
#include<stdlib.h>

#include<stdio.h>

#include<pthread.h>

static int glob=0;

static void *threadFunc(void *arg);

static void *threadFunc1(void *arg);

int main(int argc, char *argv[]){

	pthread_t t1, t2,t3 ;

	int loops, s;

	loops = atoi(argv[1]);//change str to int

	s = pthread_create(&t1, NULL, threadFunc, &loops);

	if(s!=0){

		printf("pthread_create ERROR\n");

	}

	

	s = pthread_create(&t2, NULL, threadFunc, &loops);

	if(s!=0){

		printf("pthread_create ERROR\n");

	}

	s = pthread_create(&t3, NULL, threadFunc1, &loops);

	if(s!=0){

		printf("pthread_create ERROR\n");

	}

	s = pthread_join(t1, NULL);

	if(s!=0){

		printf("pthread_join 1ERROR\n");

	}

	

	s = pthread_join(t2, NULL);

	if(s!=0){

		printf("pthread_join 2ERROR\n");

	}

	s = pthread_join(t3, NULL);

	if(s!=0){

		printf("pthread_join 3ERROR\n");

	}

	printf("glob = %d\n", glob);

	return 0;

}

static void *threadFunc(void *arg){

	int loops = *((int *) arg);

	int loc, j;

	for (j = 0; j < loops; j++) {

		loc = glob;

		loc++;

		loc++;

		glob = loc;

	}

	return NULL;

}

static void *threadFunc1(void *arg){

	int loops = *((int *) arg);

	int loc, j;

	for (j = 0; j < loops; j++) {

		loc = glob;

		loc--;

		loc--;

		glob = loc;

	}

	return NULL;

}


```


> lab2

去那了？？
---
title: oslab16
tags: [os]

---

# oslab16

```c=
#include<stdio.h>

#include<stdlib.h>

#include<time.h>

unsigned int tk;

int rand1(){

	srand(tk);

	tk+=1;

	return rand();

	

}

void shuffle(int *array, size_t n){

    //亂數前置

    if (n > 1){

        size_t i;

        for (i = 0; i<n; i++){

            size_t j = rand1()/(RAND_MAX/(n));

            int t = array[j];

            array[j] = array[i];

            array[i] = t;

        }

    }

}





void generateRandomString(char *str, int length) {

    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    int charsetSize = sizeof(charset) - 1;

	

      // 使用當前時間作為亂數種子

	length=rand1()%4+rand1()%3+1;

    for (int i = 0; i < length; ++i) {

        int index = rand1() % charsetSize;

        str[i] = charset[index];

    }

    str[length] = '\0';  // 字串結尾加上 null 字元

}



struct process{

	int *page_table;

};

int table_size=3;

char** PM;

int *free_list;

int list_pointer=0;

int PM_size=10;

struct process A,B;

int get_frree(){

	list_pointer-=1;

	int re=free_list[list_pointer+1];

	free_list[list_pointer+1]=0;

	return re;

}

int main(){

	tk=time(NULL);

	int i=0;

	table_size=rand1()%5+3;

	A.page_table=(int *)malloc(table_size*sizeof(int));

	B.page_table=(int *)malloc(table_size*sizeof(int));

	PM_size=10+table_size+rand1()%3;

	free_list=(int *)malloc(PM_size*sizeof(int));

	PM=(char **)malloc(PM_size*sizeof(char*));

	srand(time(NULL));

	for (i=0;i<PM_size;i++){

		free_list[i]=i;

	}

	list_pointer=PM_size-1;

	shuffle(free_list,PM_size);

	printf("page_table_size :%d PM_size:%d\n",table_size,PM_size);

	for(i=0;i<table_size;i++){

		int k=get_frree();

		A.page_table[i]=k;

		PM[k]= (char *)malloc(8*sizeof(char));

		generateRandomString(PM[k],8);

		k=get_frree();

		B.page_table[i]=k;

		PM[k]= (char *)malloc(8*sizeof(char));

		generateRandomString(PM[k],8);

	}

	printf("=============\n");

	for(i=0;i<table_size;i++){

		int k=A.page_table[i];

		printf("A page table[%d] frame: %d\n",i,k);

	}

	printf("=============\n");

	for(i=0;i<table_size;i++){

		int k=A.page_table[i];

		if (PM[k]!=NULL)

		printf("A frame: %d   Phsical MEM %s\n",k,PM[k]);

	}

	printf("=============\n");

	for(i=0;i<table_size;i++){

		int k=B.page_table[i];

		printf("B page table[%d] frame: %d\n",i,k);

	}

	printf("=============\n");

	for(i=0;i<table_size;i++){

		int k=B.page_table[i];

		if (PM[k]!=NULL)

		printf("B frame: %d   Phsical MEM %s\n",k,PM[k]);

	}

	printf("=============\n");

	for(i=0;i<PM_size;i++){

		if (PM[i]!=NULL){

			int j=0;

			for (j=0;j<8;j++){

				if(PM[i][j]=='\0')

					break;

				printf("Phsical MEM [%d] offset %d: %c\n",i,j,PM[i][j]);

			}

		}else{

			printf("Phsical MEM [%d] :NULL\n",i);

		}

	}

	return 0;

}
```
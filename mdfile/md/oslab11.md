---
title: oslab11
tags: [os]

---

# oslab11

## signal handler
- `siganl(signal_flag,method)`
>  lab1
```clike=
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
# include <sys/wait.h>
# include<string.h>
#include<signal.h>
void al(){
	while(1){
		
	}
}
int main(){
	if(fork()==0){
		printf("chlid:%d %d \n",getpid(),getppid());
		al();
		exit(0);
	}else{
		printf("parent:%d %d \n",getpid(),getppid());
		wait(NULL);
	}
	printf("kill\n");
}

```

>  lab2
```clike=
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
# include <sys/wait.h>
# include<string.h>
#include<signal.h>
void al(){
	while(1){
		
	}
}
int main(){
	int pid =fork();
	if(pid==0){
		printf("chlid:%d %d \n",getpid(),getppid());
		al();
		exit(0);
	}else{
	printf("parent:%d %d \n",getpid(),getppid());
		int i=3;
		while(i>0){
			i--;
			sleep(1);
			
		}
		kill(pid,SIGKILL);
	}
	printf("kill\n");
}

```

>  lab3
```clike=
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
# include <sys/wait.h>
# include<string.h>
#include<signal.h>
void al(){
	printf("this is 1 :how are you\n");
	//exit(0);
}
void a2(){
	printf("this is 2 :i'm fine\n");
	//exit(0);
}
int k;
void alarm_handler(){
	if (k==0)
		signal(SIGINT,a2);
	else 
		signal(SIGINT,SIG_DFL);
	alarm(3);
}
int main(){
	signal(SIGALRM,alarm_handler);
	alarm(3);
	signal(SIGINT,al);
	while(1){;}	
	signal(SIGINT,SIG_DFL);
}

```

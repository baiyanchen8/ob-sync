---
title: simple shell
tags: [os]

---

這個我懶得寫，自己看，就這樣
```c=1
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
# include <sys/wait.h>
# include<string.h>
#include<signal.h>
# include<readline/readline.h>
# include<readline/history.h>
char * pwdmanager(char * pwd,char * usr,char *newpwd){
	char home[1024];
	sprintf(home,"/home/%s",usr);
	if (strncmp(pwd,home,strlen(home))==0){
		sprintf(newpwd,"~%s",pwd+strlen(home));
	}else
		sprintf(newpwd,"%s",pwd);
	return newpwd;
}
struct output{
	int type; // 0 = std out ,1 = std err
	char str[8192];
	char path[1024];// path of redirection file
};
struct pid_con{
	pid_t pid;
	char cmd[4096];
};
int main() {
	char hostname[255],* username,pwd[1024],newpwd[1024];
	char fpath[4096];
	char buffer[255],buffer1[4096];
	char cmd[255];
	struct output out_arr[100];
	struct pid_con pid_arr[100];
	int x=1;
	int check_redir=0;
	int output_count=0;
	rl_pre_input_hook=rl_startup_hook;
	rl_bind_key('\t',rl_insert);
	using_history();
	rl_initialize();
	pid_t PIDtmp=-1;
	int check_pid=0;
	while(x==1){
		PIDtmp=-1;
	 	/*there is goind to print machine ,usr and dir */
	 	output_count=0;
	 	label1:memset(hostname,'\0',255);
	 	memset(pwd,'\0',255);
	 	memset(newpwd,'\0',255);
		memset(out_arr,'0',100);
	 	check_redir=0;
		if (gethostname(hostname,sizeof(hostname))!=0){
			printf("get host error\n");
			exit(1);
		}
		username=getlogin();
		if (username ==NULL){
			printf("get user name error");
			exit(1);
		}
		if (getcwd(pwd,sizeof(pwd))==NULL){
			printf("get current dir error\n");
			exit(1);
		}
		sprintf(newpwd,"%s",pwdmanager(pwd,username,newpwd));
		username=getlogin();
		if (username ==NULL){
			printf("get user name error");
			exit(1);
		}
		//printf("\033[;36;1m%s@%s\033[0;m:\033[;35;1m%s\033[;0;m$ ",username,hostname,newpwd);
		sprintf(buffer1,"\033[;36;1m%s@%s\033[0;m:\033[;35;1m%s\033[;0;m$ ",username,hostname,newpwd);
		/*----------------------------------------*/
		memset(buffer,'\0',255);
	 	memset(cmd,'\0',255);
	 	fflush(stdin);
	 	char *null;
		null=readline(buffer1);
		sprintf(buffer,"%s\0",null);
		add_history(buffer);
		if (strstr(buffer,"&")!=NULL){
			PIDtmp=fork();
			
			if(PIDtmp==0){
				buffer[strcspn(buffer,"&")]='\0';
			}else{
				pid_arr[check_pid].pid=PIDtmp;
				sprintf(pid_arr[check_pid++].cmd,"%s",buffer);
				goto skip;
			}
		}
		/*there is handler for */
		buffer[strcspn(buffer,"\n")]='\0';
		char tmp[255];
		sprintf(tmp,"%s",buffer);
		sprintf(cmd,"%s",strtok(tmp," "));
		/*redir controller*/
		if (strstr(buffer,">")!=NULL){
			check_redir=1;	
			char * ka =strstr(buffer,">");
			//printf("%s\n",ka);
			*ka='\0';
			//printf("%s\n",buffer);
			//printf("%s\n",cmd);
			int kas=0;
			for (kas=0;kas<strlen(ka+1);kas++){
					if(*(ka+kas+1)!=' '){
						sprintf(fpath,"%s",ka+kas+1);

						break;
					}			
			}
			
			
		}
		/*finish*/
		if(strncmp(cmd,"exit",4)==0){
			printf("thanks for using poyen's simple shell!!\ngoodbye!!\n");
			return 0;
		}
		/*sucess*/
		if (strncmp(cmd,"bg",2)==0){
			int in=0;
			for (in=0;in<check_pid;in++){
				if(kill(pid_arr[in].pid,0)==0){
					out_arr[output_count].type=0;//std
					sprintf(out_arr[output_count++].str,"pid :%d cmd:%s is alive\n",pid_arr[in].pid,pid_arr[in].cmd);
				}else{
					
				}
			}
			goto output;
		}
		/*finish*/
		if (strncmp(cmd,"echo",4)==0){
			/*--------------------new----way--------*/
			char split[]=" ";
			char tmp1[255],x[255];
			sprintf(tmp1,"%s",buffer);
			int i=0;
			for (i=4;i<strlen(buffer);i++){
				if (buffer[i]=='`'){
					 int j;
					 for (j=i+1;j<strlen(buffer)&&buffer[j]!='`';j++){}
					 char tmp3[255];
					 sprintf(tmp3,"%s",buffer+i+1);
					 //printf("tmp3:%s\n",tmp3);
					 memset(x,'\0',255);
					 strncpy(x,tmp3,(j-i-1));
					 sprintf(x,"%s",x);
					// printf("%s\n",x);
					int pipestd[2];
					int pipeerr[2];
					if (pipe(pipestd) == -1) {
						perror("pipe");
						exit(EXIT_FAILURE);
					}
					if (pipe(pipeerr) == -1) {
						perror("pipe");
						exit(EXIT_FAILURE);
					}
					 i=j;
					 if (fork()==0){
					 	close(pipestd[0]);  // Close unused read end
						close(pipeerr[0]);  // Close unused read end
						
						// Redirect stdout and stderr to the pipe
						dup2(pipestd[1], STDOUT_FILENO);
						dup2(pipeerr[1], STDERR_FILENO);

						close(pipestd[1]);  // Close write end
						close(pipeerr[1]);  // Close write end
					 	char *x2=strtok(x," ");
						char *argv[10];
						int c=0;
						argv[0]=x2;
						while (argv[c]!=NULL){
							x2=strtok(NULL," ");
							argv[++c]=x2;
						}
						execvp(argv[0],argv);
						fprintf(stderr,"execlp error\n");
						exit(0);
					 }else{
						 char buffertmp[2048];
						 memset(buffertmp,'\0',2048);
						 close(pipestd[1]);  // Close write end
						 close(pipeerr[1]);  // Close write end

						 if (read(pipestd[0], buffertmp, sizeof(buffertmp)) > 0){
						 	out_arr[output_count].type=0;//std
							sprintf(out_arr[output_count++].str,"%s ",buffertmp);
							int c1=0,c2=0;
							for (c1=strlen(out_arr[output_count-1].str);c1 >=0;c1--){
								if (c2 ==0&&out_arr[output_count-1].str[c1]=='\n'){
									out_arr[output_count-1].str[c1]=='\0';
									c2++;
								}else if(out_arr[output_count-1].str[c1]=='\n'){
									out_arr[output_count-1].str[c1]==' ';
								}
							
							
							}
						 }
						 if (read(pipeerr[0], buffertmp, sizeof(buffertmp)) > 0){
						 	out_arr[output_count].type=1;//err
							sprintf(out_arr[output_count++].str,"%s ",buffertmp);
							//printf("err : %s\n",buffertmp);
						 	
						 }
						 close(pipestd[0]);  // Close unused read end
						 close(pipeerr[0]);  // Close unused read end
					 	 wait(NULL);
					 }
					
				}else if (buffer[i]==' '){
					int j;
					for (j=i;j<strlen(buffer)&&buffer[j]==' ';j++){}
					i=j-1;
					for (j=i+1;j<strlen(buffer)&&buffer[j]!=' '&&buffer[j]!='`';j++){}
					char tmp3[255];
					sprintf(tmp3,"%s",buffer+i+1);
					//printf("tmp3:%s\n",tmp3);
					memset(x,'\0',255);
					strncpy(x,tmp3,(j-i-1));
					sprintf(x,"%s",x);
					//printf("%s\n",x);
					i=j-1;
					if (x[0]=='$'){
						char *x1=getenv(x+1);
						if (x1!=NULL){
							//printf("%s ",x1);
							out_arr[output_count].type=0;//std
							sprintf(out_arr[output_count++].str,"%s ",x1);

						}
					}else{
						//printf("%s ",x);
						out_arr[output_count].type=0;//std
						sprintf(out_arr[output_count++].str,"%s ",x);
					}
					
				}
				
			}
			//printf("\n");
			out_arr[output_count].type=0;//err
			sprintf(out_arr[output_count++].str,"\n");
			//return 0;
			goto output;
		}
		/*ok*/
		if (strncmp(cmd,"export",6)==0){
			char split[]=" ";
			char tmp1[255],*x;
			sprintf(tmp1,"%s",buffer);
			x=strtok(tmp1,split);
			if (strcmp(buffer,x)!=0){
				x=strtok(NULL,split);
			}else{	
				out_arr[output_count].type=1;//err
				sprintf(out_arr[output_count++].str,"command %s not found\n",x);
				//printf("command %s not found\n",x);
				goto output;
			}
			int i=1;
			while(x!=NULL){
				if (strstr(x,"=")==NULL){
					x=strtok(NULL," ");
					continue;
				}
				if (x[0]=='='){
					out_arr[output_count].type=1;//err
					sprintf(out_arr[output_count++].str,"bash: export: `%s': not a valid identifier\n",x);
					x=strtok(NULL,split);
					continue;
				}
				char tmp2[10];
				sprintf(tmp2,"%s",x);
				char *var=strtok(tmp2,"=");
				if (strcmp(var,x)!=0){
					char *num;
					num=strtok(NULL,"=");
					if (num==NULL){
						setenv(var," ",1);
					}else
					if (num[0]!='$'){
						setenv(var,num,1);
						sprintf(tmp1,"%s",buffer);
					}else{
						char tmp123[10];
						if (strstr(num,":")!=NULL){
							char* ka=strstr(num,":");
							sprintf(tmp123,"%s\0",ka);
							*ka='\0';
						}
						char *x1=getenv(num+1);
						
						if (x1!=NULL){
							//printf("%s ",x1);
							char tmp125[1024];
							sprintf(tmp125,"%s%s",x1,tmp123);
							setenv(var,tmp125,1);
						}else{
							setenv(var,tmp123,1);
						}
					}
					x=strtok(tmp1,split);
					int j=0;
					i+=1;
					for(j=0;j<i;j++){
						x=strtok(NULL,split);
					}
					
				}
			}
			goto output;
		}
		/*finish*/
		if (strncmp(cmd,"pwd",3)==0){
			out_arr[output_count].type=0;//out
			sprintf(out_arr[output_count++].str,"%s \n",pwd);
			goto output;
		}
		/*spegg*/
		if (strncmp(cmd,"spegg",5)==0){
		
			printf("hello there is some white flour~~\n");
			continue;
		}
		/*finish*/
		if (strncmp(cmd,"cd",2)==0){
			char split[]=" ";
			char tmp1[255],*x,x1[255];
			sprintf(tmp1,"%s",buffer);

			x=strtok(tmp1,split);
			if (strcmp(buffer,x)!=0){
				x=strtok(NULL,split);
				if(x!=NULL){
					sprintf(x1,"%s\0",x+1);
				}
				
			}else{
				int in2=0;
				for(in2=2;in2<strlen(buffer);in2++){
					if(buffer[in2]!=' '){
						out_arr[output_count].type=0;//err
						sprintf(out_arr[output_count++].str,"command %s not found\n",x);
						//printf("command %s not found\n",x);
						goto output;
					}
				}
				
			}
			if (strncmp(x,"~",1)==0){
				if (strlen(x)>1){
					sprintf(x,"/home/%s%s",username,x1);
				}else{
					sprintf(x,"/home/%s",username);
					
				}
				
			}
			if (chdir(x)==0){
			
			}else{
				out_arr[output_count].type=0;//err
				sprintf(out_arr[output_count++].str,"bash: cd: %s: No such file or directory\n",x);
				//printf("bash: cd: %s: No such file or directory\n",x);
			}
			goto output;
		}
		int pipestd[2];
		int pipeerr[2];
		if (pipe(pipestd) == -1) {
			perror("pipe");
			exit(EXIT_FAILURE);
		}
		if (pipe(pipeerr) == -1) {
			perror("pipe");
			exit(EXIT_FAILURE);
		}
		/*finish fork execlp*/
		if (fork()==0){
			close(pipestd[0]);  // Close unused read end
			close(pipeerr[0]);  // Close unused read end
			
			// Redirect stdout and stderr to the pipe
			dup2(pipestd[1], STDOUT_FILENO);
			dup2(pipeerr[1], STDERR_FILENO);

			close(pipestd[1]);  // Close write end
			close(pipeerr[1]);  // Close write end
			char *x=strtok(buffer," ");
			char *argv[10];
			int c=0;
			argv[0]=x;
			while (argv[c]!=NULL){
				x=strtok(NULL," ");
				argv[++c]=x;
			}
			execvp(argv[0],argv);
			printf("execlp error\n");
			exit(0);
		}else{
			char buffertmp[2048];
			 memset(buffertmp,'\0',2048);
			 close(pipestd[1]);  // Close write end
			 close(pipeerr[1]);  // Close write end

			 if (read(pipestd[0], buffertmp, sizeof(buffertmp)) > 0){
			 	out_arr[output_count].type=0;//std
				sprintf(out_arr[output_count++].str,"%s",buffertmp);
				int c1=0,c2=0;
				for (c1=strlen(out_arr[output_count-1].str);c1 >=0;c1--){
					if (c2 ==0&&out_arr[output_count-1].str[c1]=='\n'){
						out_arr[output_count-1].str[c1]=='\0';
						c2++;
					}else if(out_arr[output_count-1].str[c1]=='\n'){
						out_arr[output_count-1].str[c1]==' ';
					}
				
				}
			 }
			 if (read(pipeerr[0], buffertmp, sizeof(buffertmp)) > 0){
			 	out_arr[output_count].type=1;//err
				sprintf(out_arr[output_count++].str,"%s",buffertmp);
				//printf("err : %s\n",buffertmp);
			 	
			 }
			 close(pipestd[0]);  // Close unused read end
			 close(pipeerr[0]);  // Close unused read end
		 	 wait(NULL);
		}
		
		/*output control*/
		output:if (check_redir==0){
			int i ;
			for (i=0;i<output_count;i++){
				printf("%s",out_arr[i].str);
			}
		}else{
			/*haddling redirection*/
			FILE *file;
			file =fopen(fpath,"w");
			int i ;
			for (i=0;i<output_count;i++){
				fprintf(file,"%s",out_arr[i].str);
			}
			fclose(file);
		}
		skip:if (PIDtmp==0){
			exit(0);
		}
		
	}
	kill(0,SIGKILL);
	return 0;

}

```
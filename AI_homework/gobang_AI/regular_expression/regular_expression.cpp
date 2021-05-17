#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<regex.h>

//int find(char str[],char regstr[],)

int main()
{
    char ebuff[256];
    int ret;
    int cflags;
    regex_t reg;
    cflags=REG_EXTENDED|REG_ICASE|REG_NOSUB;
    char *test_str="Hello world";
    char *reg_str="Hello.*";
    regcomp(&reg,reg_str,cflags);
    ret=regexec(&reg,test_str,0,NULL,0);
    
    printf("%d#%s",ret,ebuff);

}
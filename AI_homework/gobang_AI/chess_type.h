#ifndef MAXN
#define MAXN 15
#endif

#define MAX_TYPE 11
#define EACH_TYPE 6

#define NO_TYPE 0//没有棋形
#define CHANG_LIAN 1 //长连
#define HUO_SI 2     //活四
#define CHONG_SI 3   //冲四
#define HUO_SAN 4    //活三
#define MIAN_SAN 5   //眠三
#define HUO_ER 6     //活二
#define MIAN_ER 7    //眠二
#define SI_SI 8      //死四
#define SI_SAN 9     //死三
#define SI_ER 10     //死二

int another_player(int x)
{
    if(x==1)return 2;
    if(x==2)return 1;
    return x;
}

const int poision[MAXN][MAXN] = {
{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},
{0,1,1,1,1,1,1,1,1,1,1,1,1,1,0},
{0,1,2,2,2,2,2,2,2,2,2,2,2,1,0},
{0,1,2,3,3,3,3,3,3,3,3,3,2,1,0},
{0,1,2,3,4,4,4,4,4,4,4,3,2,1,0},
{0,1,2,3,4,5,5,5,5,5,4,3,2,1,0},
{0,1,2,3,4,5,6,6,6,5,4,3,2,1,0},
{0,1,2,3,4,5,6,7,6,5,4,3,2,1,0},
{0,1,2,3,4,5,6,6,6,5,4,3,2,1,0},
{0,1,2,3,4,5,5,5,5,5,4,3,2,1,0},
{0,1,2,3,4,4,4,4,4,4,4,3,2,1,0},
{0,1,2,3,3,3,3,3,3,3,3,3,2,1,0},
{0,1,2,2,2,2,2,2,2,2,2,2,2,1,0},
{0,1,1,1,1,1,1,1,1,1,1,1,1,1,0},
{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}};

regex_t reg[MAX_TYPE][EACH_TYPE]={0};

void init_reg()
{
    int cflags=REG_EXTENDED|REG_ICASE|REG_NOSUB;
    regcomp(&reg[1][0],"11111",cflags);

    regcomp(&reg[2][0],"011110",cflags);

    regcomp(&reg[3][0],"011112",cflags);
    regcomp(&reg[3][1],"0101110",cflags);
    regcomp(&reg[3][2],"0110110",cflags);

    regcomp(&reg[4][0],"01110",cflags);
    regcomp(&reg[4][1],"010110",cflags);

    regcomp(&reg[5][0],"001112",cflags);
    regcomp(&reg[5][1],"010112",cflags);
    regcomp(&reg[5][2],"011012",cflags);
    regcomp(&reg[5][3],"10011",cflags);
    regcomp(&reg[5][4],"10101",cflags);
    regcomp(&reg[5][5],"2011102",cflags);
    
    regcomp(&reg[6][0],"00110",cflags);
    regcomp(&reg[6][1],"01010",cflags);
    regcomp(&reg[6][2],"010010",cflags);

    regcomp(&reg[7][0],"000112",cflags);
    regcomp(&reg[7][1],"001012",cflags);
    regcomp(&reg[7][2],"010012",cflags);
    regcomp(&reg[7][3],"10001",cflags);
    regcomp(&reg[7][4],"2010102",cflags);
    regcomp(&reg[7][5],"2011002",cflags);

    regcomp(&reg[8][0],"211112",cflags);

    regcomp(&reg[9][0],"21112",cflags);

    regcomp(&reg[10][0],"2112",cflags);

}

int judge_type(char type[])
{
    int player=type[5];
    if(player==2)
    {
    for(int i=0;i<11;i++)//对要匹配的棋经行初始化，将边界也看成是敌人2
    {
        if(type[i]==0);
        else if(type[i]==1)type[i]=2;
        else if(type[i]==2)type[i]=1;
        else if(type[i]==-1)type[i]=2;
    }
    }
    else
    {
    for(int i=0;i<11;i++)
    {
        if(type[i]==0);
        else if(type[i]==-1)type[i]=2;
    }
    }
    char search_type[11]={0};
    int left,right;
    for(left=5;left>=0;left--)
    {
        if(type[left]==-1||type[left]==2)break;
    }
    //for()
}
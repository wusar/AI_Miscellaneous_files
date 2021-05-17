#define MAXN 15

class board
{
private:
    char Board[MAXN][MAXN];//0表示未落子，1表示白子，2表示黑子,边界以外的值定义为 -1
public:
    board(/* args */);
    ~board();
    void init_board();
    void print_board();
    bool drop(int x,int y,int player);
    void draw_board();
    int get_xy(int x,int y);
    int chess_form(char form[4][11]);
    int score(int x,int y,int player);
};

board::board(/* args */)
{
    for (int i = 0; i < MAXN; i++)
    {
        for (int j = 0; j < MAXN; j++)
        {
            Board[i][j]=0;
        }
    }
    init_reg();
}

board::~board()
{
}

void board::init_board()
{
    FILE *fp=fopen("origin_board.txt","rb");
    char line[MAXN];
    for (int i = 0; i < MAXN; i++)
    {
        memset(line,0,sizeof(0));
        fscanf(fp,"%s",line);
        for (int j = 0; j < MAXN; j++)
        {
            Board[i][j]=line[j]-'0';
        }
        fgetc(fp);
    }
}

void board::print_board()
{
    for(int i=0;i<MAXN;i++)
    {
        for (int j = 0; j < MAXN; j++)
        {
            printf("%d ",Board[i][j]);
        }
        putchar('|');
        putchar('\n');
    }
}

bool board::drop(int x,int y,int player)
{
    if(this->Board[x][y])return false;
    else this->Board[x][y]=player;
        return true;
}

void board::draw_board()
{
    for(int i=0;i<MAXN;i++)
    {
        for (int j = 0; j < MAXN; j++)
        {
            if(Board[i][j]==0)putchar(' ');
            else if(Board[i][j]==1)putchar('o');
            else if(Board[i][j]==2)putchar('x');
        }
        putchar('|');
        putchar('\n');
    }
}

int board::get_xy(int x,int y)
{
    if(x<MAXN&&x>=0&&y<MAXN&&y>=0)
    {
        return Board[x][y];
    }
    return -1;
}


int board::score(int x,int y,int player)
{
    if(!drop(x,y,player))
    {
        printf("allready dropped!");
        return 0;
    }
    char form[4][11];
    // char axis_y[11];
    // char axis_xy[11];
    // char axis_yx[11];

    for(int i=-5;i<6;i++)
    {
        form[0][i+5]=this->get_xy(x,y+i);
        form[1][i+5]=this->get_xy(x+i,y);
        form[2][i+5]=this->get_xy(x+i,y-i);
        form[3][i+5]=this->get_xy(x+i,y+i);
    }
    return chess_form(form);
}


int board::chess_form(char form[4][11])
{
    // int player_chess_num=0,enemy_chess_num=0;//连续的player的棋子，以及两端的enemy棋子数量，边界也算敌人
    // int i;
    // char player;
    // player=form[5];
    // for(i=6;i<11;i++)
    // {
    //     if(form[i]==player)player_chess_num++;
    //     else break;
    // }
    // if(i==11);
    // else if(form[i]!=0)enemy_chess_num++;

    // for(i=4;i>=0;i--)
    // {
    //     if(form[i]==player)player_chess_num++;
    //     else break;
    // }
    // if(i==-1);
    // else if(form[i]!=0)enemy_chess_num++;

    // for (int i = 0; i < 11; i++)
    // {
    //     printf("%d ",form[i]);
    // }

    // printf("\n%d*%d\n",player_chess_num,enemy_chess_num);
    // return 0;
    
    
}
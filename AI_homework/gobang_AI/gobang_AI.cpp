
#include<stdio.h>
#include<string.h>
#include<sys/types.h>
#include<regex.h>
#include"chess_type.h"

#include"board.h"
int main()

{
    board B;
    
    B.init_board();
    B.print_board();
    B.score(3,3,1);
    //B.draw_board();
}

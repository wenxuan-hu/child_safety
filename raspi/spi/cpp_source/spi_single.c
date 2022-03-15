/*********************************************************************************
* Copyright: (C) 2018 wangtao
* All rights reserved.
*
* Filename: spi_own.c
* Description: This file
*
* Version: 1.0.0(11/07/2018)
* Author: WangTao <TAlicer@163.com>
* ChangeLog: 1, Release initial version on "11/07/2018 17:15:56 PM"
*
********************************************************************************/
 
 
#include <stdio.h>
 
#include <stdlib.h>
 
#include <unistd.h>
 
#include "SPISet.h"
 
 
int initSPI()
 
{
 
int spiFd;


spiFd=SPISetup(0,1000); //

//spiFd=SPISetup(0,10000000); //
 
if(spiFd==-1)
 
{
 
printf("init spi failed!\n");
 
}
 
}
 
 
int main()
 
{
 
char tx_Data[1]={10}; //定义读写的数据
 
char rx_Data[1]={0};
 
int i=0;
 
 
initSPI(); //spi的初始化


SPIDataRW(0,tx_Data,rx_Data,1); //
 
//printf("read spi_rx_data is:\n"); //
printf("%d\n",rx_Data[0]);
//printf("%c\n", (char)rx_Data[0]);


 
 
/*while(1)
 
{
 
SPIDataRW(0,tx_Data,rx_Data,1); //
 
printf("read spi_rx_data is:\n"); //

 

 
printf("%d\n",rx_Data[0]);  
//printf("%c\n",(char)rx_Data[0]);  
 

 
printf("\n");
 
sleep(10);
 
}*/
 
return 0;
 
}
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
 
spiFd=SPISetup(0,500); //
//spiFd=SPISetup(0,500000); //


if(spiFd==-1)
 
{
 
printf("init spi failed!\n");
 
}
 
}
 
 
int main()
 
{
 
char tx_Data[10]={1,2,3,4,5,6,7,8,9,10}; //定义读写的数据
 
char rx_Data[10]={0,0,0,0,0,0,0,0,0,0};
 
int i=0;
 
 
initSPI(); //spi的初始化
 
while(1)
 
{
 
SPIDataRW(0,tx_Data,rx_Data,10); //向总线中写入7个数据
 
printf("read spi_rx_data is:\n"); //读出总线的数据，引脚19与21短接打印【1,2,3,4,5,6,7,0,0,0】
 
// 引脚19与21不短接打印【0,0,0,0,0,0,0,0,0,0】
 
for(i=0;i<10;i++)
 
{
 
printf("%d\n",rx_Data[i]);  
 
}
 
printf("\n");
 
sleep(1);
 
}
 
return 0;
 
}
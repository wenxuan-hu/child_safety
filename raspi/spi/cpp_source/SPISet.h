/*********************************************************************************
* Copyright: (C) 2018 wangtao
* All rights reserved.
*
* Filename: SPISet.h
* Description: This file
*
* Version: 1.0.0(11/07/2018)
* Author: WangTao <TAlicer@163.com>
* ChangeLog: 1, Release initial version on "11/07/2018 17:15:56 PM"
*
********************************************************************************/
 
 
#ifdef __cplusplus
 
extern "C" {
 
#endif
 
 
int SPIDataRW (int channel, unsigned char *tx_data,unsigned char *rx_data, int len) ;
 
int SPISetupMode (int channel, int speed, int mode) ;
 
int SPISetup (int channel, int speed) ;
 
 
#ifdef __cplusplus
 
}
 
#endif
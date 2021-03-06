# encoding: UTF-8
"""
VT类型与CTP类型的映射
"""

from heron.lib.vnpy.constant import *
from data_type import *

# 以下为一些VT类型和CTP类型的映射字典
# 价格类型映射
priceTypeMap = {}
priceTypeMap[PRICETYPE_LIMITPRICE] = defineDict["THOST_FTDC_OPT_LimitPrice"]
priceTypeMap[PRICETYPE_MARKETPRICE] = defineDict["THOST_FTDC_OPT_AnyPrice"]
priceTypeMapReverse = {v: k for k, v in priceTypeMap.items()}

priceTypeMap_ = {}
priceTypeMap_['PRICETYPE_LIMITPRICE'] = defineDict["THOST_FTDC_OPT_LimitPrice"]
priceTypeMap_['PRICETYPE_MARKETPRICE'] = defineDict["THOST_FTDC_OPT_AnyPrice"]

# 方向类型映射
directionMap = {}
directionMap[DIRECTION_LONG] = defineDict['THOST_FTDC_D_Buy']
directionMap[DIRECTION_SHORT] = defineDict['THOST_FTDC_D_Sell']
directionMapReverse = {v: k for k, v in directionMap.items()}
directionMap_ = {}
directionMap_['DIRECTION_LONG'] = defineDict['THOST_FTDC_D_Buy']
directionMap_['DIRECTION_SHORT'] = defineDict['THOST_FTDC_D_Sell']

# 开平类型映射
offsetMap = {}
offsetMap[OFFSET_OPEN] = defineDict['THOST_FTDC_OF_Open']
offsetMap[OFFSET_CLOSE] = defineDict['THOST_FTDC_OF_Close']
offsetMap[OFFSET_CLOSETODAY] = defineDict['THOST_FTDC_OF_CloseToday']
offsetMap[OFFSET_CLOSEYESTERDAY] = defineDict['THOST_FTDC_OF_CloseYesterday']
offsetMapReverse = {v: k for k, v in offsetMap.items()}
offsetMap_ = {}
offsetMap_['OFFSET_OPEN'] = defineDict['THOST_FTDC_OF_Open']
offsetMap_['OFFSET_CLOSE'] = defineDict['THOST_FTDC_OF_Close']
offsetMap_['OFFSET_CLOSETODAY'] = defineDict['THOST_FTDC_OF_CloseToday']
offsetMap_['OFFSET_CLOSEYESTERDAY'] = defineDict['THOST_FTDC_OF_CloseYesterday']

# 交易所类型映射
exchangeMap = {}
exchangeMap[EXCHANGE_CFFEX] = 'CFFEX'
exchangeMap[EXCHANGE_SHFE] = 'SHFE'
exchangeMap[EXCHANGE_CZCE] = 'CZCE'
exchangeMap[EXCHANGE_DCE] = 'DCE'
exchangeMap[EXCHANGE_SSE] = 'SSE'
exchangeMap[EXCHANGE_UNKNOWN] = ''
exchangeMapReverse = {v: k for k, v in exchangeMap.items()}
exchangeMap_ = {}
exchangeMap_['EXCHANGE_CFFEX'] = 'CFFEX'
exchangeMap_['EXCHANGE_SHFE'] = 'SHFE'
exchangeMap_['EXCHANGE_CZCE'] = 'CZCE'
exchangeMap_['EXCHANGE_DCE'] = 'DCE'
exchangeMap_['EXCHANGE_SSE'] = 'SSE'
exchangeMap_['EXCHANGE_UNKNOWN'] = ''

# 持仓类型映射
posiDirectionMap = {}
posiDirectionMap[DIRECTION_NET] = defineDict["THOST_FTDC_PD_Net"]
posiDirectionMap[DIRECTION_LONG] = defineDict["THOST_FTDC_PD_Long"]
posiDirectionMap[DIRECTION_SHORT] = defineDict["THOST_FTDC_PD_Short"]
posiDirectionMapReverse = {v: k for k, v in posiDirectionMap.items()}
posiDirectionMap_ = {}
posiDirectionMap_['DIRECTION_NET'] = defineDict["THOST_FTDC_PD_Net"]
posiDirectionMap_['DIRECTION_LONG'] = defineDict["THOST_FTDC_PD_Long"]
posiDirectionMap_['DIRECTION_SHORT'] = defineDict["THOST_FTDC_PD_Short"]

# 产品类型映射
productClassMap = {}
productClassMap[PRODUCT_FUTURES] = defineDict["THOST_FTDC_PC_Futures"]
productClassMap[PRODUCT_OPTION] = defineDict["THOST_FTDC_PC_Options"]
productClassMap[PRODUCT_COMBINATION] = defineDict["THOST_FTDC_PC_Combination"]
productClassMapReverse = {v: k for k, v in productClassMap.items()}

productClassMap_ = {}
productClassMap_['PRODUCT_FUTURES'] = defineDict["THOST_FTDC_PC_Futures"]
productClassMap_['PRODUCT_OPTION'] = defineDict["THOST_FTDC_PC_Options"]
productClassMap_['PRODUCT_COMBINATION'] = defineDict["THOST_FTDC_PC_Combination"]

# 委托状态映射
statusMap = {}
statusMap[STATUS_ALLTRADED] = defineDict["THOST_FTDC_OST_AllTraded"]
statusMap[STATUS_PARTTRADED] = defineDict["THOST_FTDC_OST_PartTradedQueueing"]
statusMap[STATUS_NOTTRADED] = defineDict["THOST_FTDC_OST_NoTradeQueueing"]
statusMap[STATUS_CANCELLED] = defineDict["THOST_FTDC_OST_Canceled"]
statusMapReverse = {v: k for k, v in statusMap.items()}

statusMap_ = {}
statusMap_['STATUS_ALLTRADED'] = defineDict["THOST_FTDC_OST_AllTraded"]
statusMap_['STATUS_PARTTRADED'] = defineDict["THOST_FTDC_OST_PartTradedQueueing"]
statusMap_['STATUS_NOTTRADED'] = defineDict["THOST_FTDC_OST_NoTradeQueueing"]
statusMap_['STATUS_CANCELLED'] = defineDict["THOST_FTDC_OST_Canceled"]

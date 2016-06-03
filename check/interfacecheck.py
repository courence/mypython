#encoding:utf-8
'''

Created on May 30, 2016
@author: jh
'''
import logging
def __filed_existence_check(fileds,target_files):
    '''字段存在性检查'''
    less = []
    more = []
    for filed in fileds:
        if filed not in target_files:
            less.append(filed)
    for filed in target_files:
        if filed not in fileds:
            more.append(filed) 
    if less:
        logging.error( '缺少的字段：{}',less)
    
    if more:
        logging.info( '多余的字段：{}',more)

def route_check(data):
    '''线路检查'''
    filed_check = {'station_code':None,
                   'line_name':None,
                   'line_identity':None,
                   'line_type':None,
                   'line_sort':None,
                   'start_city_code':None,
                   'arrival_city_code':None,
                   'arrival_station_code':None,
                   'line_highway_mileage':None,
                   'line_level':None,
                   'schedule_check':None,
                   'std_seat_no':None,
                   'line_status':None,
                   'line_level_sub':None,
                   'via_city_list':None,}
    if data:
        __filed_existence_check(filed_check.keys(),data[0].keys())
    

if __name__ == '__main__':
    fileds = ['station_code','line_name']

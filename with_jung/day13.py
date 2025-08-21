# 1. 목표 : 주어진 데이터셋에서 튜플을 활용하여 분석
# 2. 요구사항
# 연도별 판매량 계산
# 제품별 평균 가격 계산
# 최대 판매 지역 찾기
# 분기별 매출 분석
# ==데이터셋==
# 데이터: 연도, 분기, 제품, 가격, 판매량, 지역
sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 120, "인천"),
    (2020, 3, "스마트폰", 850, 300, "서울"),
    (2020, 4, "노트북", 1300, 130, "부산"),
    (2020, 4, "스마트폰", 850, 350, "서울"),
    (2021, 1, "노트북", 1400, 110, "대구"),
    (2021, 1, "스마트폰", 900, 220, "서울"),
    (2021, 2, "노트북", 1400, 160, "인천"),
    (2021, 2, "스마트폰", 900, 270, "부산"),
    (2021, 3, "노트북", 1500, 130, "서울"),
    (2021, 3, "스마트폰", 950, 320, "대구"),
    (2021, 4, "노트북", 1500, 140, "부산"),
    (2021, 4, "스마트폰", 950, 370, "서울")
]


YEAR = 0
COUNT = 1

def GetYearIndex(searching_list, year):
    count = 0
    for searching_list_itme in searching_list:
        if searching_list_itme[YEAR] == year:
            return count
        count+=1
    return -1

#1. ㅇㅕㄴㄷㅗㅂㅕㄹ ㅍㅏㄴㅁㅐㄹㅑㅇ ㄱㅖㅅㅏㄴ
stat_list_for_total_sales = []

for item in sales_data:
    stat_index = GetYearIndex(stat_list_for_total_sales, item[YEAR])
    if stat_index >= 0:
        stat_list_for_total_sales[stat_index][COUNT] += 1
    else:
        new_stat = [item[YEAR], 1]
        stat_list_for_total_sales.append( new_stat )

for stat in stat_list_for_total_sales:
    print(stat)


#2. ㅈㅔㅍㅜㅁㅍㅕㅇㄱㅠㄴㄱㅏ가격 계산.


ITEM_IN_SALES_DATA = 2
COST_IN_SALES_DATA = 3
SALES_COUNT_IN_SALES_DATA = -2
REGION_IN_SALES_DATA = -1

ITEM_IN_STAT = 0
TOTAL_COST_IN_STAT = 1
AVERAGE_COST_IN_STAT = 2
SALES_COUNT_IN_STAT = 3


# item, total cost, average cost, sales count
stat_list_for_average = []

def GetStatIndex(searching_list, sales_item):
    count = 0
    for searching_list_itme in searching_list:
        if searching_list_itme[ITEM_IN_STAT] == sales_item:
            return count
        count+=1
    return -1

for datum in sales_data:
    stat_index = GetStatIndex(stat_list_for_average, datum[ITEM_IN_SALES_DATA])
    if stat_index >= 0:
        stat_list_for_average[stat_index][TOTAL_COST_IN_STAT] += datum[COST_IN_SALES_DATA] * datum[SALES_COUNT_IN_SALES_DATA]
        stat_list_for_average[stat_index][SALES_COUNT_IN_STAT] += datum[SALES_COUNT_IN_SALES_DATA]
    else:
        new_stat = [datum[ITEM_IN_SALES_DATA], datum[COST_IN_SALES_DATA], 0, datum[SALES_COUNT_IN_SALES_DATA]]
        stat_list_for_average.append(new_stat)

def GetAverage(stat_list):
    for item in stat_list:
        item[AVERAGE_COST_IN_STAT] = item[TOTAL_COST_IN_STAT] / item[SALES_COUNT_IN_STAT]

GetAverage(stat_list_for_average)

print("-------------")
for stat in stat_list_for_average:
    print(stat)


# 최대 판매 지역 

# 지역 판매액
stat_list_for_region = []

REGION = 0
#TOTAL_COST_IN_STAT = 1

def GetRegionIndex(searching_list, region):
    count = 0
    for searching_list_itme in searching_list:
        if searching_list_itme[REGION] == region:
            return count
        count+=1
    return -1

for datum in sales_data:
    index = GetRegionIndex(stat_list_for_region, datum[REGION_IN_SALES_DATA])
    if index >= 0:
        stat_list_for_region[index][TOTAL_COST_IN_STAT] += datum[COST_IN_SALES_DATA] * datum[SALES_COUNT_IN_SALES_DATA]
    else:
        new_data = [ datum[REGION_IN_SALES_DATA], datum[COST_IN_SALES_DATA] * datum[SALES_COUNT_IN_SALES_DATA]]
        stat_list_for_region.append(new_data)


print("-------------")
for stat in stat_list_for_region:
    print(stat)


QUATER = 0
QUATER_IN_SALES_DATA = 1

stat_list_for_quater = []

#분기별 판매액
def GetQuaterIndex(searching_list, quater):
    count = 0
    for searching_list_itme in searching_list:
        if searching_list_itme[QUATER] == quater:
            return count
        count+=1
    return -1

for datum in sales_data:
    index = GetQuaterIndex(stat_list_for_quater, datum[QUATER_IN_SALES_DATA])
    if index >= 0:
        stat_list_for_quater[index][TOTAL_COST_IN_STAT] += datum[COST_IN_SALES_DATA] * datum[SALES_COUNT_IN_SALES_DATA]
    else:
        new_data = [ datum[QUATER_IN_SALES_DATA], datum[COST_IN_SALES_DATA] * datum[SALES_COUNT_IN_SALES_DATA]]
        stat_list_for_quater.append(new_data)

        
        
print("-------------")
for stat in stat_list_for_quater:
    print(stat)
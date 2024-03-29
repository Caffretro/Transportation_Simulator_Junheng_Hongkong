import pickle
import numpy as np
import pandas as pd
import sys


# def calculate_match_rate():
#     driver_num = [500, 1000, 1500, 2000, 2500, 3000]
#     max_distance_num = [0.5, 1, 2, 3, 4]
#     count = 0
#     orders = pickle.load(open('./input/order.pickle', 'rb'))
#     for time in range(36000, 79200):
#         if time in orders.keys():
#             count += len(orders[time])
#     file = open('./output/match_rate.txt', 'w')
#     for item in driver_num:
#         for item2 in max_distance_num:

#             records = pickle.load(
#                 open('./output/records_driver_num_' + str(item) + '_distance_' + str(item2) + '.pickle', 'rb'))
#             matched = 0
#             print(count)
#             for i,time in enumerate(records):

#                 for driver in time:
#                     if isinstance(time[driver][0], list):
#                         # if str(int(time[driver][0][2])) not in x:
#                         # print(i,driver,time[driver])
#                         matched += 1
#             print(matched)
#             print(matched / count)
#             file.write('driver_num: ' + str(item) + '\t' + 'distance_threshold: ' + str(
#                 item2) + '\t' + 'match_rate:' + str(matched / count) + '\n')

#
# test = (40.71561,-73.994272)
# print(test in node_coord_to_id.keys())


# def delete_none_order():
#     data = pickle.load(open('./input/order.pickle', 'rb'))
#     # lng = data['lat'].values.tolist()
#     # for item in lng:
#     #     if item == 40.71561:
#     #         print('test')
#     # print(data[data['lng']== -73.994272])
#     for time in data.keys():
#         for order in data[time]:
#             test = (order[2], order[3])

#     pickle.dump(data, open('./input/order.pickle','wb'))


# if __name__ == '__main__':
    # delete_none_order()
    # calculate_match_rate()
    # t = np.array([1,2,3,4])
    # x = (t.cumsum()>10).argmax()
    # print(x)
    # print(np.random.choice([1,2,3,4,5,6,7], 7,replace=False).tolist())
    # test = pd.DataFrame([[1,2,3],[2,3,4]])
    # indexs = [3,2]
    # new_indexs = []
    # for item in indexs:
    #     index = test[test[1] == item].index.tolist()[0]
    #     new_indexs.append(index)
    # print(new_indexs)
    # print(test.iloc[new_indexs])

import itertools

def show_used_drivers():
    drivers = pickle.load(open("./1103-driver.pkl","rb"))
    orders = pickle.load(open("1103-order.pkl","rb"))
    used_drivers = pickle.load(open("1103-used-driver.pkl","rb"))

    # new_orders = orders[0]
    # for order in orders:
    #     new_orders.append(order)
    # print(new_orders)

    order_df = orders[0]
    driver_df = used_drivers[0]
    for used_driver,order in zip(used_drivers,orders):
        if len(used_driver) !=0:
            # print(used_driver
            order_df = order_df.append(order)
            driver_df = driver_df.append(used_driver)

    print(order_df[(order_df['driver_id'] == 3822) & (order_df['order_id'] == 208447)][['order_id','start_time','t_matched','pickup_time','trip_distance','t_end']])

    print(driver_df[(driver_df['driver_id'] == 3822) &(driver_df['matched_order_id'] == 208447)][['matched_order_id','driver_id','remaining_time']])


def show_itineary_segment():
    orders = pickle.load(open("./input1/new_order_frac=0.1.pickle","rb"))
    order_of_one_day = orders['2015-05-04']
    column_name = ['order_id', 'origin_id', 'origin_lat', 'origin_lng', 'dest_id', 'dest_lat', 'dest_lng',
                       'trip_distance', 'start_time', 'origin_grid_id', 'dest_grid_id', 'itinerary_node_list',
                       'itinerary_segment_dis_list', 'trip_time', 'designed_reward', 'cancel_prob']
    order_df_per_day = pd.DataFrame(order_of_one_day,columns=column_name)
    print(order_df_per_day['itinerary_segment_dis_list'])


def show_new_order(pth):
    orders = pickle.load(open(pth,"rb"))
    print("file",pth)
    print(orders.keys())
    order_of_one_day = orders['2015-05-04']
    # print(order_of_one_day)
    column_name = ['order_id', 'origin_id', 'origin_lat', 'origin_lng', 'dest_id', 'dest_lat', 'dest_lng',
                       'trip_distance', 'start_time', 'origin_grid_id', 'dest_grid_id', 'itinerary_node_list',
                       'itinerary_segment_dis_list', 'trip_time', 'designed_reward', 'cancel_prob']
    order_df_per_day = pd.DataFrame(order_of_one_day,columns=column_name)
    print(order_df_per_day.head(10))

if __name__ == '__main__':
    # unpickled_data = pd.read_pickle("./input_Hong_Kong/hongkong_processed_order_11_29.pickle") 
    unpickled_data = pd.read_pickle("./input_Hong_Kong/hongkong_date_based_order_test.pickle")
    # unpickled_data = pd.read_pickle("./input_Hong_Kong/hongkong_driver_info.pickle") 

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        '''
        Hong Kong orders start at 28800 and stops at 633539, there are 115055 orders in total
        '''
        # ['order_id', 'origin_id', 'origin_lat', 'origin_lng', 'dest_id', 'dest_lat', 'dest_lng',
        #    'trip_distance', 'start_time', 'origin_grid_id', 'dest_grid_id', 'itinerary_node_list',
        #    'itinerary_segment_dis_list', 'trip_time', 'designed_reward', 'cancel_prob']

        # start_list = unpickled_data['start_time']
        # end_list = unpickled_data['end_time']
        # start_list.sort()
        # end_list.sort()
        # print("driver count: {}".format(len(start_list))) # number of drivers

        # counter = 0
        # for idx, val in enumerate(start_list):
        #     # count how many driver's start_time is later than his/her end_time
        #     if int(val) == int(end_list[idx]):
        #         counter += 1
        # print("irregular count: {}".format(counter))

        # print(unpickled_data.keys())
        # print(len(unpickled_data))
        for key in sorted(unpickled_data.keys()):
            print(len(unpickled_data[key]))
            # print(unpickled_data[key])

        '''
        Hong Kong drivers start working 82211 and stops at 633591, there are 41504 drivers in total
        '''

        # Driver file keys:
        #     data = ['driver_id', 'start_time', 'end_time', 'lng', 'lat', 'node_id',
        #    'grid_id', 'status', 'target_loc_lng', 'target_loc_lat',
        #    'target_node_id', 'target_grid_id', 'remaining_time',
        #    'matched_order_id', 'total_idle_time', 'time_to_last_cruising',
        #    'current_road_node_index', 'remaining_time_for_current_node',
        #    'itinerary_node_list', 'itinerary_segment_dis_list']
        # The first driver that will go online is at 82211 
        # The first order comes in at 28800
        # Push back the start and endtime of all drivers by 53411

        
        # status_counter = 0
        # for entry in unpickled_data["status"]:
        #     if entry == 0:
        #         status_counter += 1
        # print(status_counter)

        # print(unpickled_data.keys())
        # print(unpickled_data.iloc[404])

        # print(len(unpickled_data["start_time"]))
        # time_min = sys.maxsize
        # for entry in unpickled_data["start_time"]:
        #     if entry < time_min:
        #         time_min = entry
        # print(time_min)
        # print(unpickled_data['start_time'])
        pass

    # DATE_LIST = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8']

    # loaded_data = pickle.load(open("./input_Hong_Kong/hongkong_processed_order_11_29.pickle", 'rb'))
    # print(loaded_data)
    # # loaded_test_data = pickle.load(open("./input_Hong_Kong/hongkong_date_based_processed_order_11_29.pickle", 'rb'))
    # requests = {}
    # for second in loaded_data.keys():
    #     for idx, day in enumerate(DATE_LIST):
    #         if int(idx) <= int(second / 86400) < int(idx + 1):
    #             if day not in requests.keys():
    #                 requests[day] = {second: loaded_data[second]}
    #             else:
    #                 requests[day].update({second: loaded_data[second]})
    # test_save_data = pickle.dump(requests, open("./input_Hong_Kong/hongkong_date_based_processed_order_11_29.pickle", 'wb'))
    # loaded_test_data = pickle.load(open("./input_Hong_Kong/test_using_date.pickle", 'rb'))
    # print(sorted(loaded_test_data['day1'].keys()))

    # loaded_data = pickle.load(open("./input_Hong_Kong/hongkong_driver_info_11_29.pickle", 'rb'))

        

import pickle
import numpy as np
import pandas as pd


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
    # show_new_order("./input1/order-11-13-frac=0.1.pickle")
    # Print out the pickle file
    # data = pickle.load(open("./input_Hong_Kong/hongkong_processed_order_11_29.pickle", 'rb'))
    # data = pickle.load(open("./input_Hong_Kong/hongkong_driver_info_11_29.pickle", 'rb'))
    # for item in data:
    #     if data[item][0][13] or data[item][0][14]:
    #         print(data[item][0][13])
    #         print(data[item][0][14])
    unpickled_data = pd.read_pickle("./input_Hong_Kong/hongkong_driver_info_11_29.pickle") 
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        # datalist = list(unpickled_data.keys())
        # print(len(unpickled_data[629880][0]))
        # datalist.sort()
        # print(datalist[100])

        # Driver file keys:
        #     data = ['driver_id', 'start_time', 'end_time', 'lng', 'lat', 'node_id',
        #    'grid_id', 'status', 'target_loc_lng', 'target_loc_lat',
        #    'target_node_id', 'target_grid_id', 'remaining_time',
        #    'matched_order_id', 'total_idle_time', 'time_to_last_cruising',
        #    'current_road_node_index', 'remaining_time_for_current_node',
        #    'itinerary_node_list', 'itinerary_segment_dis_list']
        for entry in unpickled_data["status"]:
            if entry == 0:
                print("status is 0")
        
        
        

env_params = {
# time interval in seconds
't_initial' : 0,   # 3-9
't_end' : 86400, # 7.5 days
'delta_t' : 5,  # s
'vehicle_speed' : 22.788,   # km / h
'repo_speed' :22.788, #目前的设定需要与vehicl speed保持一致
'order_sample_ratio' : 1,
'order_generation_mode' : 'sample_from_base',
'driver_sample_ratio' : 1,
'maximum_wait_time_mean' : 300,
'maximum_wait_time_std' : 0,
"maximum_pickup_time_passenger_can_tolerate_mean":float('inf'),  # s
"maximum_pickup_time_passenger_can_tolerate_std":0, # s
"maximum_price_passenger_can_tolerate_mean":float('inf'), # ￥
"maximum_price_passenger_can_tolerate_std":0,  # ￥
'maximal_pickup_distance' : 1,  # km
'request_interval':5,  #
'cruise_flag' :True,
'delivery_mode':'rg',
'pickup_mode':'rg',
'max_idle_time' : 300,  # 1s and 300s
'cruise_mode': 'random',   # modify
'reposition_flag': False,
'eligible_time_for_reposition' : 300, # s
'reposition_mode': '',
'track_recording_flag' : False,
'driver_far_matching_cancel_prob_file' : 'driver_far_matching_cancel_prob',
'request_file_name' : './input_Hong_Kong/hongkong_date_based_order_test', #'toy_requests',
'driver_file_name' : './input_Hong_Kong/hongkong_driver_info',
'road_network_file_name' : 'road_network_information.pickle',
'dispatch_method': 'LD', #LD: lagarange decomposition method designed by Peibo Duan
# 'method': 'instant_reward_no_subway',
'simulator_mode' : 'toy_mode',
'experiment_mode' : 'test',
'driver_num':5000, # how many drivers to sample from driver list, start from 500 maybe, add 500 each time
# FIXME: notice that only changing driver_num won't affect the actual sampling ratio in simulator_pattern,
# since it utilizes 'single_driver_num' defined in main.py as sampling parameter. If we really want to change
# the number of drivers sampled, go to main.py's very first lines to change driver_num manually
'side':10,
'price_per_km':5,  # ￥ / kmss
'road_information_mode':'load',
'price_increasing_percentage': 0.2, # modify this parameter
'north_lat': 22.51,
'south_lat': 19.57,
'east_lng': 113.21,
'west_lng': 114.32, # Hong Kong coordinates
# 'north_lat': 40.8845,
# 'south_lat': 40.6968,
# 'east_lng': -74.0831,
# 'west_lng': -73.8414, Manhattan coordinates
'rl_mode': 'matching',  # reposition and matching
'method': 'instant_reward_no_subway',  #  'sarsa_no_subway' / 'pickup_distance' / 'instant_reward_no_subway'   #  rl for matching
'reposition_method': 'random_cruise',  # A2C, A2C_global_aware, random_cruise, stay  # rl for repositioning
}
wait_time_params_dict = {'morning': [2.582, 2.491, 0.026, 1.808, 2.581],
                    'evening': [4.862, 2.485, 0, 1.379, 13.456],
                    'midnight_early': [0, 2.388, 2.972, 2.954, 3.14],
                    'other': [0, 2.017, 2.978, 2.764, 2.973]}

pick_time_params_dict = {'morning': [1.877, 2.018, 2.691, 1.865, 6.683],
                    'evening': [2.673,2.049,2.497,1.736,9.208],
                    'midnight_early': [3.589,2.319,2.185,1.664,9.6],
                    'other': [0,1.886,4.099,3.185,3.636]}

price_params_dict = {'short': [1.245,0.599,10.629,10.305,0.451],
                    'short_medium': [0.451,0.219,19.585,58.407,0.18],
                    'medium_long': [14.411,4.421,11.048,9.228,145],
                    'long': [15.821,3.409,0,16.221,838.587]}

# price_increase_params_dict = {'morning': [0.001,1.181,3.583,4.787,0.001],
#                     'evening': [0,1.21,2.914,5.023,0.013],
#                     'midnight_early': [1.16,0,0,6.366,0],
#                     'other': [0,2.053,0.857,4.666,1.961]}
#  rl for matching
# global variable and parameters for sarsa
START_TIMESTAMP = 10800  # the start timestamp
LEN_TIME_SLICE = 300  # the length of a time slice, 5 minute (300 seconds) in this experiment
LEN_TIME = 6 * 60 * 60 # 3 hours
NUM_EPOCH = 2505  # 4001 / 3001
FLAG_LOAD = False
sarsa_params = dict(learning_rate=0.005, discount_rate=0.95)  # parameters in sarsa algorithm
#  rl for matching

# rl for repositioning
# hyperparameters for rl
# NUM_EPOCH = 1301
STOP_EPOCH = 1300
DISCOUNT_FACTOR = 0.95
ACTOR_LR = 0.001
CRITIC_LR = 0.005
ACTOR_STRUCTURE = [64,128] #[16, 32] for A2C, and [64, 128] for A2C global aware
CRITIC_STRUCTURE = [64,128]
# rl for repositioning


#  rl for matching
# parameters for exploration
INIT_EPSILON = 0.9
FINAL_EPSILON = 0
DECAY = 0.997
PRE_STEP = 0
#  rl for matching

#  rl for matching
TRAIN_DATE_LIST = ['2015-05-04','2015-05-05','2015-05-06','2015-05-07','2015-05-08',]

TEST_DATE_LIST = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8'] #['2015-05-11', '2015-05-12', '2015-05-13', '2015-05-14', '2015-05-15']
# TODO: switch to ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'day8'], and change back the original loading function
#  rl for matching

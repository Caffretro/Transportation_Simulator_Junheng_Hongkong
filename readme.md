### An Open-Sourced Network-Based Large-Scale Simulation Platform for Shared Mobility Operations

![效果图](https://img.shields.io/static/v1?label=build&message=passing&color=green) ![](https://img.shields.io/static/v1?label=python&message=3&color=blue) ![](https://img.shields.io/static/v1?label=release&message=2.0&color=green) ![](https://img.shields.io/static/v1?label=license&message=MIT&color=blue)

### Background

Establish an open-sourced network-based simulation platform for shared mobility operations. The simulation explicitly characterizes drivers’ movements on road networks for trip delivery, idle cruising, and en-route pick-up. 

### Install

1. Download the code.

`git clone git@github.com:HKU-Smart-Mobility-Lab/Transpotation_Simulator.git`

2. Download the dependencies and libraries.

`pip install -r requirements.txt`

### File Structure

```
-simulator
--input
---graph.graphml
---order.pickle
---driver_info.pickle
--output
--- some output files 
--driver_generation.py
--dispatch_alg.py
--handle_raw_data.py
--find_closest_point.py
--simulator_pattern.py
--simulator_env.py
--A2C.py
--sarsa.py
--main.py
--config.py
--LICENSE.md
--readme.md
```

##### Data preparing

There are three files in 'input' directory. You can use the driver data and order data provided by us. Also, you can run `python handle_raw_data.py`  to generate orders' information, run `python driver_generation.py`  to generate drviers' information.  

In [config.py](https://github.com/HKU-Smart-Mobility-Lab/Transpotation_Simulator/blob/main/simulator/config.py), you can set the parameters of the simulator.

```python
't_initial' # start time of the simulation (s)
't_end'  # end time of the simulation (s)
'delta_t' # interval of the simulation (s) 
'vehicle_speed' # speed of vehicle (km / h)
'repo_speed'  # speed of reposition
'order_sample_ratio' # ratio of order sampling
'order_generation_mode'  # the mode of order generation
'driver_sample_ratio' : 1, # ratio of driver sampling
'maximum_wait_time_mean' : 300, # mean value of maximum waiting time
'maximum_wait_time_std' : 0, # variance of maximum waiting time
"maximum_pickup_time_passenger_can_tolerate_mean":float('inf'),  # s
"maximum_pickup_time_passenger_can_tolerate_std"
"maximum_price_passenger_can_tolerate_mean"
"maximum_price_passenger_can_tolerate_std"
'maximal_pickup_distance'  # km
'request_interval': 5,  #
'cruise_flag' :False, # 
'delivery_mode':'rg',
'pickup_mode':'rg',
'max_idle_time' : 1,
'cruise_mode': 'random',
'reposition_flag': False,
'eligible_time_for_reposition' : 10, # s
'reposition_mode': '',
'track_recording_flag' : True,
'driver_far_matching_cancel_prob_file' : 'driver_far_matching_cancel_prob',
'input_file_path':'input/dataset.csv',
'request_file_name' : 'input/order', #'toy_requests',
'driver_file_name' : 'input/driver_info',
'road_network_file_name' : 'road_network_information.pickle',
'dispatch_method': 'LD', #LD: lagarange decomposition method designed by Peibo Duan
# 'method': 'instant_reward_no_subway',
'simulator_mode' : 'toy_mode',
'experiment_mode' : 'train',
'driver_num':500,
'side':4, # grid side length
'price_per_km':5,  # ￥ / km
'road_information_mode':'load',
'north_lat': 40.8845,
'south_lat': 40.6968,
'east_lng': -74.0831,
'west_lng': -73.8414,
'rl_mode': 'reposition',  # reposition and matching
'method': 'sarsa_no_subway',  #  'sarsa_no_subway' / 'pickup_distance' / 'instant_reward_no_subway'   
'reposition_method' #2C_global_aware',  # A2C, A2C_global_aware, random_cruise, stay  

```

##### Real Road Network Module

We use [osmnx](https://pypi.org/project/osmnx/) to acquire the shortest path from the real world. You can set 'north_lat', 'south_lat', 'east_lng' and 'west_lng' in [config.py](https://github.com/HKU-Smart-Mobility-Lab/Transpotation_Simulator/blob/main/simulator/config.py) , and you can get road network for the specified region.

##### Price Module

You can set the maximum order price that is normally distributed and acceptable to passengers by modifing `maximum_price_passenger_can_tolerate_mean'` and `maximum_price_passenger_can_tolerate_std`.

##### Cruising and Repositioning Module



##### Dispatching Module

In dispatch_alg.py, we implement the function LD, we use binary map matching algorithm to dispatch orders.

##### Experiment

You can modify the parameters in [config.py](https://github.com/HKU-Smart-Mobility-Lab/Transpotation_Simulator/blob/main/simulator/config.py), and then excute `python main.py`. The records will be recorded in the directory named output.

### Tutorials







### Technical questions

We welcome your contributions.

- Please report bugs and improvements by submitting [GitHub issue](https://github.com/HKU-Smart-Mobility-Lab/Transpotation_Simulator/issues).
- Submit your contributions using [pull requests](https://github.com/HKU-Smart-Mobility-Lab/Transpotation_Simulator/pulls). 

### Citing

If you use this simulator for academic research, you are highly encouraged to cite our paper:

An Open-Sourced Network-Based Large-Scale Simulation Platform for Shared Mobility Operations



### Contributors

This simulator is supported by the [Smart Mobility Lab](	https://github.com/HKU-Smart-Mobility-Lab) at The Univerisity of Hong Kong.







##### 
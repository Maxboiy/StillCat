import json

# This is the test file to check if I can make JSON files 
# This program can also be used to fix your JSON file if needed

max_deployed_cats = 2
custom_file_dir = None
stand_still = 10
random_stand_still = False
begin_range = 1
end_range = 5
initial_wait_time = 0
enable_random_deployment = False

start_date = None
end_date = None

writeplz = {
   "config": [ 
        {
            "max_deployed_cats": max_deployed_cats,
            "custom_file_dir": custom_file_dir,
            "stand_still": stand_still,
            "initial_wait_time": initial_wait_time,
            "enable_random_deployment": enable_random_deployment
        }
    ],
    "random_time_stuff": [
        {
            "random_stand_still": random_stand_still,
            "begin_range": begin_range,
            "end_range": end_range,
        }
    ]
    # "activation_period": [ # WIP!!!
    #     {
    #         "start_date": start_date,
    #         "end_date": end_date,
    #     }
    # ] 
}

with open("config.json", "w") as f:
    json.dump(writeplz, f)

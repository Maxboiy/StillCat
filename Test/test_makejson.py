import json

max_deployed_cats = 2
custom_file_dir = None
stand_still = 10
# stand_still_wait = 0.5

start_date = None
end_date = None

writeplz = {
   "config": [ 
        {
            "max_deployed_cats": max_deployed_cats,
            "custom_file_dir": custom_file_dir,
            "stand_still": stand_still,
            # "stand_still_number": stand_still_wait,
        }
    ],
    "activation_period": [ # WIP!!!
        {
            "start_date": start_date,
            "end_date": end_date,
        }
    ] 
}

with open("config.json", "w") as f:
    json.dump(writeplz, f)

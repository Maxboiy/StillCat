import json

# For some reason json.dump keeps putting the numbers in quotes for example: "random_value": "4", 
# This completely confuses the program and skips the deployment thing
# While working on the config apps I kept getting this issue and it's driving me insane
# Using int(text) seems to fix this issue with the downside of you can only use rounded numbers
# But if it works it works

text = input("Insert >> ")

text2 = int(text)

writeplz = {"config": [{"texting": text2,}]}

with open("test.json", "w") as file:
    json.dump(writeplz, file)
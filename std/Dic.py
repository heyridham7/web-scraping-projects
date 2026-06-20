info = {
    "name" : "Ridham",
    "Subject" : "Python",
    "cpi" : {
        "yr1" : 7.5,
        "yr2" : 8.0,
    },
    "food" : ["Pizza", "Burger", "Pasta"],
    "Bvrg" : ("Tea", "Coffee", "Juice"),
    "isHungary" : True
}
info["name"]= "B2"
#print(info["cpi"]["yr1"])
#print(info.keys())
#print(info.values())
#print(info.items())
#print(info.get("name"))
info.update({"City" : "Valsad"})
print(info)
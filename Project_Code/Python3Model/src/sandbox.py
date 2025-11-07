import subprocess
import os

if __name__ == "__main__":
    globalVariables = {
            "destinations" : {
                "airspeed" : 1,
                "roll" : 2,
                "heading" : 3,
                "latitude": 4,
                "longitude": 5,
                "vertical speed" : 6,
                "altitude": 7,
                "pitch" : 8,
                "brakes": 9,
                "wheelSpeed": 10,
                "wheelWeight": 11
            },
            "targetValues" : {
                "target_airspeed"       : 12,
                "target_roll"           : 13,
                "target_Lat"            :  14,
                "target_Long"           : 15,
                "target_descent_rate"   : 16,
                "target_altitude"       :  17,
                "target_pitch"          : 18
            }
        }
    
    def dictionaryAccess(dictionary,keys):
        # print("dictionary access for: " + str(key))
        nestedDictionary = dictionary

        try: 
            for key in keys:
                result = nestedDictionary[key]
                nestedDictionary = result
        except TypeError as e:
            print("bottomed out in dictionary access, too many keys -- returning last good value")

        if isinstance(result, tuple):
            return result[0]
        else: 
            return result
        
    # allParams = globalVariables.items()
    # print(dictionaryAccess(globalVariables,[str(item1[0]),str(item2)]))
    results = dictionaryAccess(globalVariables,["targetValues","target_airspeed"])
    print(results)
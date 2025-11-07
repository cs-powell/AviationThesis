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
    
    def dictionaryAccess(self,dictionary,keys):
        # print("dictionary access for: " + str(key))
        nestedDictionary = dictionary
        for key in keys:
            result = nestedDictionary[key]
            nestedDictionary = result
        
        if isinstance(result, tuple):
            return result[0]
        else: 
            return result
        
    result = self.dictionaryAccess(globalVariables,["destinations","airspeed"])

    print(result)
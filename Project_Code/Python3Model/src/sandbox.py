import subprocess
import os
from modelParameters import params
import modelParameters
from modelParameters import listAccess
from modelParameters import permissions

# if __name__ == "__main__":
class sandbox: 
    parameters = params()
    p1 = params()
    # print(p1.a)
    p1.a = 21
    # print(p1.a)
    p2 = modelParameters.params()
    # print(p2.a)
    p2.a = 3522 
    # print(p2.a)
    # print(p1.b)
    # print(p2.b)

    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.DREF.value,permissions.READ.value))
    parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.DREF.value,permissions.WRITE.value,"borf")
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.DREF.value,permissions.READ.value))
    print("new test")
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))
    parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.WRITE.value,1)
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))
    parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.WRITE.value,10)
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))
    parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.WRITE.value,50)
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))
    oldParams = parameters
    print("next test -- new instance")
    parameters = params()
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.DREF.value,permissions.READ.value))
    print(parameters.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))

    print("next test -- revisit old instance: should see borf and 50")
    print(oldParams.dictionaryAccess(["aircraft_state","airspeed"],listAccess.DREF.value,permissions.READ.value))
    print(oldParams.dictionaryAccess(["aircraft_state","airspeed"],listAccess.CURRENT.value,permissions.READ.value))
    print("next test -- Other subdictionaries")
    print(oldParams.dictionaryAccess(["aircraft_state",listAccess.NAME.value],listAccess.CURRENT.value,permissions.READ.value))


    # p1.globalVariables.


    # SCALEYOKEPULL = 10
    # SCALEYOKESTEER = 10
    # SCALERUDDER = 10
    # SCALELATITUDERUDDER = 0.001
    # SCALETHROTTLE = 1000

    # globalVariables = {
    #         "destinations" : {
    #             "airspeed" : 1,
    #             "roll" : 2,
    #             "heading" : 3,
    #             "latitude": 4,
    #             "longitude": 5,
    #             "vertical speed" : 6,
    #             "altitude": 7,
    #             "pitch" : 8,
    #             "brakes": 9,
    #             "wheelSpeed": 10,
    #             "wheelWeight": 11
    #         },
    #         "targetValues" : {
    #             "target_airspeed"       : 12,
    #             "target_roll"           : 13,
    #             "target_Lat"            :  14,
    #             "target_Long"           : 15,
    #             "target_descent_rate"   : 16,
    #             "target_altitude"       :  17,
    #             "target_pitch"          : 18
    #         }
    #     }
    
    # def dictionaryAccess(dictionary,keys):
    #     # print("dictionary access for: " + str(key))
    #     nestedDictionary = dictionary

    #     try: 
    #         for key in keys:
    #             result = nestedDictionary[key]
    #             nestedDictionary = result
    #     except TypeError as e:
    #         print("bottomed out in dictionary access, too many keys -- returning last good value")

    #     if isinstance(result, tuple):
    #         return result[0]
    #     else: 
    #         return result
        
    # allParams = globalVariables.items()
    # print(dictionaryAccess(globalVariables,[str(item1[0]),str(item2)]))
    # results = dictionaryAccess(globalVariables,["targetValues","target_airspeed"])
    # print(results)
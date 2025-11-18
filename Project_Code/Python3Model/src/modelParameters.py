from enum import Enum

class params:
    def __init__(self):
        self.globalParameters = {
            parameterType.AIRCRAFT_STATE : {
                "airspeed"          : ["sim/cockpit2/gauges/indicators/airspeed_kts_pilot",0, 0,0],
                "roll"              : ["sim/cockpit2/gauges/indicators/roll_AHARS_deg_pilot",0,0,0],
                "heading"           : ["sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot",0,0,0], # Previous Heading
                "latitude"          : ["sim/flightmodel/position/latitude",0,0,0],
                "longitude"         : ["sim/flightmodel/position/longitude",0,0,0],
                "vertical speed"    : ["sim/flightmodel/position/vh_ind_fpm",0,0,0], # Previous Descent Rate
                "altitude"          : ["sim/flightmodel/position/y_agl",0,0,0],
                "pitch"             : ["sim/flightmodel/position/true_theta",0,0,0],
                "brakes"            : ["sim/cockpit2/controls/parking_brake_ratio",0,0,0],
                "wheelSpeed"        : ["sim/flightmodel2/gear/tire_rotation_speed_rad_sec",0,0,0],
                "wheelWeight"       : ["sim/flightmodel/parts/tire_vrt_def_veh",0,0,0]
            },
            parameterType.PHASE_FLAGS : {
                flightPhase.DESCENT         : [True],
                flightPhase.FLARE           : [False],
                flightPhase.ROLLOUT         : [False]
            },
            parameterType.INTEGRAL_VALUES : {
                integralValues.K : [integralValues.K.value], # Proportional gain
                integralValues.Ki : [integralValues.Ki.value]  # Integral gain  
            }
        }

    def dictionaryAccess(self,keys,accessItem,permissionFlag,inputValue=None):
        # print("dictionary access for: " + str(key))
        nestedDictionary = self.globalParameters
        for key in keys:
            result = nestedDictionary[key]
            nestedDictionary = result
        if(permissionFlag == permissions.WRITE.value):
            if isinstance(result, list):
                result[accessItem] = inputValue
        else:
            if isinstance(result, list):
                return result[accessItem]
            else: 
                return result
            
    def getModelDREFS(self):
        dictionary :dict = self.globalParameters[parameterType.AIRCRAFT_STATE]
        values = dictionary.values()
        drefList = []
        for item in values:
            drefList.append(item[listAccess.DREF.value])
        return drefList
    
    def getModelKeys(self):
        dictionary :dict = self.globalParameters[parameterType.AIRCRAFT_STATE]
        keys = dictionary.items()
        keyList = []
        for item in keys:
            keyList.append(item[0])
        return keyList
        
class listAccess(Enum):
    DREF = 0
    TARGET = 1
    PREVIOUS = 2
    CURRENT = 3
    PHASE_FLAG = 0
    INTEGRAL_VALUE = 0

class parameterType(Enum):
    AIRCRAFT_STATE = "aircraft_state"
    PHASE_FLAGS = "phase_flags"
    INTEGRAL_VALUES = "integral_values"


class flightPhase(Enum):
    DESCENT =   "descent"
    FLARE   =   "flare"
    ROLLOUT =   "rollout"

class integralValues(Enum):
    K = 35
    Ki = 15

class permissions(Enum):
    READ = 0
    WRITE = 1

        


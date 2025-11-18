from enum import Enum

class params:
     

    def __init__(self):
        
        # self.sources = {
        #             "airspeed"          : "sim/cockpit2/gauges/indicators/airspeed_kts_pilot",
        #             "roll"              : "sim/cockpit2/gauges/indicators/roll_AHARS_deg_pilot",
        #             "heading"           : "sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot",
        #             "latitude"          : "sim/flightmodel/position/latitude",
        #             "longitude"         : "sim/flightmodel/position/longitude",
        #             "vertical speed"    : "sim/flightmodel/position/vh_ind_fpm",
        #             "altitude"          : "sim/flightmodel/position/y_agl",
        #             "pitch"             : "sim/flightmodel/position/true_theta",
        #             "brakes"            : "sim/cockpit2/controls/parking_brake_ratio",
        #             "wheelSpeed"        : "sim/flightmodel2/gear/tire_rotation_speed_rad_sec",
        #             "wheelWeight"       : "sim/flightmodel/parts/tire_vrt_def_veh"
        #         }
        
       


        self.globalVariables = {
            "aircraft_state" : {
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
            "phaseFlags" : {
                "descent"           : [True],
                "flare"             : [False],
                "roll out"          : [False]
            },
            "integralValues" : {
                "Kp" : [0.1], # Proportional gain
                "Ki" : [0.01]  # Integral gain  
            }

           
        }

    def dictionaryAccess(self,keys,accessItem,permissionFlag,inputValue=None):
        # print("dictionary access for: " + str(key))
        nestedDictionary = self.globalVariables
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

        
class listAccess(Enum):
    DREF = 0
    TARGET = 1
    PREVIOUS = 2
    CURRENT = 3
    PHASE = 0

class permissions(Enum):
    READ = 0
    WRITE = 1

        


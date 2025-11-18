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
        
        class listAccess(Enum):
            DREF = 0
            TARGET = 1
            PREVIOUS = 2
            CURRENT = 3
            PHASE = 0


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
                "Kp" : 0.1, # Proportional gain
                "Ki" : 0.01  # Integral gain  
            }

            # "targetValues" : {
            #     "target_airspeed"       : self.target_airspeed,
            #     "target_roll"           : self.target_roll,
            #     "target_Lat"            :  self.target_Lat,
            #     "target_Long"           : self.target_Long,
            #     "target_descent_rate"   : self.target_descent_rate,
            #     "target_altitude"       :  self.target_altitude,
            #     "target_pitch"          : self.target_pitch
            # },
            # "phaseFlags" : {
            #     "descent"   : self.descent,
            #     "flare"     : self.flare,
            #     "roll out"  : self.rollOut
            # },
            # "previousValues" : {
            #     "previous_airspeed"             : self.previous_airspeed,
            #     "previous_roll"                 : self.previous_roll,
            #     "self.previous_heading"         : self.previous_heading,
            #     "self.previous_descent_rate"    : self.previous_descent_rate
            # },
            # "integralValues" : {
            #     "Kp" : self.Kp, # Proportional gain
            #     "Ki" : self.Ki # Integral gain  
            # }
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






























        # self.a = 1
        # self.b = 2
        # self.e = 3

        
        # self.globalVariables = {
        #     "destinations" : {
        #         "airspeed" : 1,
        #         "roll" : 2,
        #         "heading" : 3,
        #         "latitude": 4,
        #         "longitude": 5,
        #         "vertical speed" : 6,
        #         "altitude": 7,
        #         "pitch" : 8,
        #         "brakes": 9,
        #         "wheelSpeed": 10,
        #         "wheelWeight": 11
        #     },
        #     "targetValues" : {
        #         "target_airspeed"       : 12,
        #         "target_roll"           : 13,
        #         "target_Lat"            :  14,
        #         "target_Long"           : 15,
        #         "target_descent_rate"   : 16,
        #         "target_altitude"       :  17,
        #         "target_pitch"          : 18
        #     }
        # }




class params:
    
    def __init__(self):
        self.sources = {
                    "airspeed"          : "sim/cockpit2/gauges/indicators/airspeed_kts_pilot",
                    "roll"              : "sim/cockpit2/gauges/indicators/roll_AHARS_deg_pilot",
                    "heading"           : "sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot",
                    "latitude"          : "sim/flightmodel/position/latitude",
                    "longitude"         : "sim/flightmodel/position/longitude",
                    "vertical speed"    : "sim/flightmodel/position/vh_ind_fpm",
                    "altitude"          : "sim/flightmodel/position/y_agl",
                    "pitch"             : "sim/flightmodel/position/true_theta",
                    "brakes"            : "sim/cockpit2/controls/parking_brake_ratio",
                    "wheelSpeed"        : "sim/flightmodel2/gear/tire_rotation_speed_rad_sec",
                    "wheelWeight"       : "sim/flightmodel/parts/tire_vrt_def_veh"
                }
        

        self.globalVariables = {
            "destinations" : {
                "airspeed" : ("sim/cockpit2/gauges/indicators/airspeed_kts_pilot",self.target_airspeed, self.airspeed),
                "roll" : ("sim/cockpit2/gauges/indicators/roll_AHARS_deg_pilot",self.target_roll,self.roll),
                "heading" : ("sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot",self.target_heading,self.heading),
                "latitude": ("sim/flightmodel/position/latitude",self.latitude),
                "longitude": ("sim/flightmodel/position/longitude",self.longitude),
                "vertical speed" : ("sim/flightmodel/position/vh_ind_fpm", self.descent_rate),
                "altitude": self.altitude,
                "pitch" : self.pitch,
                "brakes": self.brakes,
                "wheelSpeed": self.wheelSpeed,
                "wheelWeight": self.wheelWeight
            },
            "targetValues" : {
                "target_airspeed"       : self.target_airspeed,
                "target_roll"           : self.target_roll,
                "target_Lat"            :  self.target_Lat,
                "target_Long"           : self.target_Long,
                "target_descent_rate"   : self.target_descent_rate,
                "target_altitude"       :  self.target_altitude,
                "target_pitch"          : self.target_pitch
            },
            "phaseFlags" : {
                "descent"   : self.descent,
                "flare"     : self.flare,
                "roll out"  : self.rollOut
            },
            "previousValues" : {
                "previous_airspeed"             : self.previous_airspeed,
                "previous_roll"                 : self.previous_roll,
                "self.previous_heading"         : self.previous_heading,
                "self.previous_descent_rate"    : self.previous_descent_rate
            },
            "integralValues" : {
                "Kp" : self.Kp, # Proportional gain
                "Ki" : self.Ki # Integral gain  
            }
        }






























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




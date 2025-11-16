class params:
    c = 40
    d = 45 
    def __init__(self):
        self.a = 1
        self.b = 2
        self.e = 3

        
        self.globalVariables = {
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




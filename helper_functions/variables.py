data_conversion = {"./data/Electricity_consumption.csv" : "Total Consumption",
        "./data/Electricity_production_in_Finland.csv" : "Total Production",
        "./data/nuclear_production.csv" : "Nuclear production",
        "./data/Industrial_cogeneration.csv" : "Industrial Cogeneration",
        "./data/cogenerating_of_district_heat.csv" : "Cogenation of district heat",
        "./data/Hydro_production.csv" : "Hydro production",
        "./data/wind.csv" : "Wind production",
        "./data/Net_import_export.csv" : "Net import/export",
        "./data/reserve_and_small_production.csv" : "Reserve power plants and small-scale production"}

to_sum = ["Nuclear production", "Industrial Cogeneration", "Cogenation of district heat",
          "Hydro production", "Wind production",  "Net import/export", "Reserve power plants and small-scale production"]

to_sum_colors = ["DarkGreen", "IndianRed", "SandyBrown", "SlateBlue", "Khaki","darkmagenta", "Tomato"]

variable_ids = {"Wind_3min" : 181, 
                "Reserve and small production" : 205,
                "cogenerating of district heat" : 201,
                "nuclear production": 188,
                "Industrial cogeneration": 202,
                "Electricity production in Finland" : 192,
                "Hydro production" : 191,
                "Net import/export" : 194,
                "Electricity consumption" : 193,
                "Electricity safety state" : 209,
                }

variables = [["Wind power production", 181, "MW", "3min measurement"], 
                ["Reserve power plants and small-scale production ", 205, "MW", "3min measurement"], 
                ["Cogeneration of district heating", 201, "MW", "3min measurement"], 
                ["Nuclear power production", 188, "MW", "3min measurement"], 
                ["Industrial cogeneration", 202, "MW", "3min measurement"], 
                ["Electricity production in Finland", 192, "MW", "3min measurement"], 
                ["Hydro power production", 191, "MW", "3min measurement"], 
                ["Net import/export", 194, "MW", "3min measurement"], #
                ["Electricity consumption", 193, "MW", "3min measurement"],
                ["Electricity safety state", 209, "MW", "3min measurement"]]#

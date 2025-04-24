locations = ["Within UPLB", "Umali Subdivision", "Demarces", "Junction", "Any"]
amenities = ["Co-ed", "Males Only", "Females Only", "Visitors Allowed", "Curfew", "Cooking Allowed", "Pets Allowed", "Furnished", "Water and Electric Meter", "WiFi"]
colleges = ["CAS", "CEAT", "CHE", "CDC", "CVM", "CAFS", "CFNR", "CEM"]

distanceOfCollegesFromGate = {
    "CAS": 400,
    "CEAT": 1000,
    "CHE": 300,
    "CDC": 100,
    "CVM": 1300,
    "CAFS": 1100,
    "CFNR": 1400,
    "CEM": 300
}

dormitoryDatabase = {
    "Arable Premier Residences": {

        "Location": "Within UPLB",

        "Distance from Colleges": {
            "CAS": 400,
            "CEAT": 1100,
            "CHE": 550,
            "CDC": 600,
            "CVM": 1200,
            "CAFS": 1300,
            "CFNR": 1100,
            "CEM": 500
        },

        "Rate": {
            "Lower Bound": 4500,
            "Upper Bound": 10000
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 3
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": False,
            "Curfew": False,
            "Cooking Allowed": False,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "Jose R. Velasco Ave., Batong Malake, Los Baños, Laguna",
            "Contact Person": "N/A",
            "Contact Number": "09123722936",
            "Facebook Link": "https://www.facebook.com/arablepremier",
        }
    },

    "Narra Residences": {

        "Location": "Demarces",

        "Distance from Gate": 400,

        "Rate": {
            "Lower Bound": 6000,
            "Upper Bound": 6000
        },

        "Pax": {
            "Lower Bound": 3,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": False,
            "Curfew": False,
            "Cooking Allowed": False,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "10656 Basil St., Los Baños, Laguna",
            "Contact Person": "N/A",
            "Contact Number": "09175185572",
            "Facebook Link": "https://www.facebook.com/narraresidence",
        }
    },
        
     "Kitanglad Hall": {

        "Location": "Umali Subdivision",

        "Distance from Gate": 1200,

        "Rate": {
            "Lower Bound": 3500,
            "Upper Bound": 3500
        },

        "Pax": {
            "Lower Bound": 4,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": False,
            "Co-ed": False,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": False,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "9982 Mt Kitanlad St Umali Subd, Los Baños, Laguna",
            "Contact Person": "Kitanglad Hall (FB Account)",
            "Contact Number": "09695243367",
            "Facebook Link": "https://www.facebook.com/profile.php?id=100083087842415",
        }
    },
        
     "Palis Apartment": {
         
         "Location": "Junction",

         "Distance from Gate": 1400,

        "Rate": {
            "Lower Bound": 3000,
            "Upper Bound": 6000
        },
 
        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": False,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "#9562 Bangkal St., Batong Malake, Los Baños, Laguna",
            "Contact Person": "Gina Fernandez",
            "Contact Number": "N/A",
            "Facebook Link": "https://www.facebook.com/gina.fernandez.391420",
        }
    },
        
    "Maria Filipina Apartment": {

        "Location": "Umali Subdivision",

        "Distance from Gate": 500,

        "Rate": {
            "Lower Bound": 2500,
            "Upper Bound": 7500
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": False,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "F.O. Santos, Umali Subd., Batong Malake, Los Baños, Laguna, 4031",
            "Contact Person": "Andrea",
            "Contact Number": "09459709720",
            "Facebook Link": "N/A",
        }
    },
    
    "Wisma Gloria Shalom Apartment": {

        "Location": "Umali Subdivision",

        "Distance from Gate": 550,

        "Rate": {
            "Lower Bound": 1666,
            "Upper Bound": 6000
        },

        "Pax": {
            "Lower Bound": 2,
            "Upper Bound": 6
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "Wisma Gloria Shalom Apt., F.O. Santos St., Brgy." \
            "Batong Malake, Los Baños, Laguna",
            "Contact Person": "Jemar Coliao",
            "Contact Number": "N/A",
            "Facebook Link": "N/A",
        }
    },

    "The Mint by Zdi": {

        "Location": "Demarces",

        "Distance from Gate": 350,

        "Rate": {
            "Lower Bound": 3500,
            "Upper Bound": 7000
        },

        "Pax": {
            "Lower Bound": 2,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": False,
            "Visitors Allowed": True,
            "Curfew": True,
            "Cooking Allowed": True,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },
        
        "Contact Details": {
            "Address": "The Mint by Zdi, Mint Street, Demarses Subdivision,"\
            "Brgy. Batong Malake, Los Baños, Laguna",
            "Contact Person": "N/A",
            "Contact Number": "N/A",
            "Facebook Link": "https://www.facebook.com/themintbyzdi",
        }
    },

    "Casa De Felicidad": {

        "Location": "Within UPLB",

        "Distance from Colleges": {
            "CAS": 250,
            "CEAT": 1100,
            "CHE": 450,
            "CDC": 250,
            "CVM": 1300,
            "CAFS": 1200,
            "CFNR": 1400,
            "CEM": 150
        },        

        "Rate": {
            "Lower Bound": 5000,
            "Upper Bound": 12000
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 3
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": False,
            "Visitors Allowed": False,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "10950 Jose R. Velasco Ave., UPLB, Los Baños, Laguna",
            "Contact Person": "N/A",
            "Contact Number": "09189278756",
            "Facebook Link": "https://www.facebook.com/CasaDeFelicidadDorm",
        }
    },

    "Trace Suites": {

        "Location": "Junction",

        "Distance from Gate": 1800,

        "Rate": {
            "Lower Bound": 4200,
            "Upper Bound": 4200
        },

        "Pax": {
            "Lower Bound": 4,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": False,
            "Visitors Allowed": False,
            "Curfew": True,
            "Cooking Allowed": False,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "Trace Suites, El Danda Street, Batong Malake, Los Baños",
            "Contact Person": "N/A",
            "Contact Number": "09364008057",
            "Facebook Link": "https://www.facebook.com/tracesuites",
        }
    },

    "Othrys Realty": {

        "Location": "Demarces",

        "Distance from Gate": 350,

        "Rate": {
            "Lower Bound": 8000,
            "Upper Bound": 15000
        },

        "Pax": {
            "Lower Bound": 3,
            "Upper Bound": 6
        },

        "Amenities": {
            "Males Only": False,
            "Females Only": False,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": True,
            "Cooking Allowed": True,
            "Pets Allowed": False,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "Lot 2 Rosemary St, Demarces Sbdv, Brgy. Batong Malake"\
            "Los Baños, Laguna",
            "Contact Person": "N/A",
            "Contact Number": "09496507441",
            "Facebook Link": "https://www.facebook.com/othrys.laguna",
        }
    },
        
     "Ephesus": {
         
        "Location": "Within UPLB",

        "Distance from Colleges": {
            "CAS": 450,
            "CEAT": 800,
            "CHE": 300,
            "CDC": 200,
            "CVM": 1300,
            "CAFS": 1000,
            "CFNR": 1400,
            "CEM": 400
        },

        "Rate": {
            "Lower Bound": 3000,
            "Upper Bound": 6000
        },

        "Pax": {
            "Lower Bound": 2,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "Ephesus 3, Victoria M. Ela Ave., Ilag’s Compound, Laguna",
            "Contact Person": "Lawrence Ilag",
            "Contact Number": "09176519660",
            "Facebook Link": "N/A",
        }
    },

    "Freedorm Residences": {

        "Location": "Demarces",

        "Distance from Gate": 550,

        "Rate": {
            "Lower Bound": 3250,
            "Upper Bound": 6500
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 2
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "10743 Dinorado St. Cor Rhaminad St. Sta. Fe Subd., Los Baños, Laguna",
            "Contact Person": "Bheta Betz Drilon",
            "Contact Number": "09179193875",
            "Facebook Link": "https://www.facebook.com/bheta.drilon",
        }
    },

    "Sparking Hill Apartment aka Bluehouse": {

        "Location": "Umali Subdivision",

        "Distance from Gate": 1200,

        "Rate": {
            "Lower Bound": 2160,
            "Upper Bound": 13000
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 6
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "9058 Unit 18 Mt. Banaue St. Umali Subdivision Batong Malake Los Baños, Laguna",
            "Contact Person": "Althea Gutierrez",
            "Contact Number": "N/A",
            "Facebook Link": "N/A",
        }
    },

    "OPOCS Apartment": {

        "Location": "Umali Subdivision",

        "Distance from Gate": 600,

        "Rate": {
            "Lower Bound": 4300,
            "Upper Bound": 13000
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 3
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": True,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "Mt. Banahaw, Pearl St. Batong Malake Los Baños, Laguna",
            "Contact Person": "Nico Ramos",
            "Contact Number": "09186982399",
            "Facebook Link": "https://www.facebook.com/nico.ramos.50",
        }
    },

    "LNC Apartment": {

        "Location": "Junction",

        "Distance from Gate": 1200,

        "Rate": {
            "Lower Bound": 1375,
            "Upper Bound": 5500
        },

        "Pax": {
            "Lower Bound": 1,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": False,
            "Water and Electric Meter": True,
            "WiFi": False,
        },

        "Contact Details": {
            "Address": "1011 El Danda St., Batong Malake, Los Banos, Laguna",
            "Contact Person": "Ronald Mercado",
            "Contact Number": "N/A",
            "Facebook Link": "fb.com/ronald.mercado.75470",
        }
    },

    "Casa Bettina": {

        "Location": "Junction",

        "Distance from Gate": 1500,

        "Rate": {
            "Lower Bound": 5000,
            "Upper Bound": 10000
        },

        "Pax": {
            "Lower Bound": 2,
            "Upper Bound": 4
        },

        "Amenities": {
            "Males Only": True,
            "Females Only": True,
            "Co-ed": True,
            "Visitors Allowed": True,
            "Curfew": False,
            "Cooking Allowed": True,
            "Pets Allowed": True,
            "Furnished": False,
            "Water and Electric Meter": True,
            "WiFi": True,
        },

        "Contact Details": {
            "Address": "6577 Bangkal Street (Extension), Los Baños, Laguna, 4031",
            "Contact Person": "N/A",
            "Contact Number": "09055670165",
            "Facebook Link": "https://www.facebook.com/profile.php?id=100057295485869",
        }
    },
}
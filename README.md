# indian_banks

indian_banks is a simple API allowing users to view branch details of banks of india.<br />

1. Get branch detail by ifsc code: https://still-hollows-84066.herokuapp.com/branches/?ifsc=ifsc_code
2. Get detail of all branches by bank and city: https://still-hollows-84066.herokuapp.com/branches/?bank=bank_name&city=city_name

## Branches Collection [/branches/?bank=<bank_name>&city=<city_name>]

### List All Branches given bank and city [GET]

bank_name: name of the bank in capital letters<br />
city_name: name of the city in capital letters<br />
format: [optional, default: api], json/api<br />

Example 
+ Request: https://still-hollows-84066.herokuapp.com/branches/?bank=STATE BANK OF INDIA&city=KHARAGPUR&format=json

+ Response 200 (application/json)

        [
          {
            "ifsc": "SBIN0003332",
            "bank": "STATE BANK OF INDIA",
            "branch": "KHARAGPUR RLY STN",
            "address": "OLD AMOHEALTH OFFICE BLDG., CME GATE, KHARAGPUR, PASCHIM MIDNAPUR",
            "city": "KHARAGPUR",
            "district": "PURBA MEDINIPUR",
            "state": "WEST BENGAL\n"
          },
          {
            "ifsc": "SBIN0005155",
            "bank": "STATE BANK OF INDIA",
            "branch": "INDA",
            "address": "ATWAL REAL ESTATE  GROUND FLOOR  O T  ROAD  KARAGPUR  MIDNAPORE W  WEST BENGAL 721305",
            "city": "KHARAGPUR",
            "district": "PURBA MEDINIPUR",
            "state": "WEST BENGAL\n"
          },
          {
            "ifsc": "SBIN0010425",
            "bank": "STATE BANK OF INDIA",
            "branch": "SALUA",
            "address": "KHARAGPUR  DIST PASCHIM MEDINIPUR  WEST BENGAL721101",
            "city": "KHARAGPUR",
            "district": "HOWRAH",
            "state": "WEST BENGAL\n"
          },
          {
            "ifsc": "SBIN0014883",
            "bank": "STATE BANK OF INDIA",
            "branch": "RBO KHARAGPUR R-III",
            "address": "INDA,KHARAGPUR,PASCHIM MIDNAPORE DISTRICT,WEST BENGAL 721305",
            "city": "KHARAGPUR",
            "district": "KHARAGPUR",
            "state": "WEST BENGAL\n"
          },
          {
            "ifsc": "SBIN0016341",
            "bank": "STATE BANK OF INDIA",
            "branch": "R.B.O.  REGION VI  KHARAGPUR",
            "address": "ATWAL BUILDING, INDA, KHARAGPUR, P.O.  KHARAGPUR, DIST.  PASCHIM MEDINIPUR, WEST BENGAL 721305",
            "city": "KHARAGPUR",
            "district": "PASCHIM MEDINIPUR",
            "state": "WEST BENGAL\n"
          },
          {
            "ifsc": "SBIN0016767",
            "bank": "STATE BANK OF INDIA",
            "branch": "KAUSHALLYA",
            "address": "BAKLI ARCADE,KAUSHALLYA,KHARGPUR,DISTT.PASCHIM MEDINIPORE.WEST BENGAL 721301",
            "city": "KHARAGPUR",
            "district": "PASCHIM MEDINIPUR",
            "state": "WEST BENGAL\n"
          }
        ]

## Single Branch [/branches/?ifsc=<ifsc_code>]
### Get branch details given ifsc code [GET]

ifsc_code: ifsc code of branch<br />
format: [optional, default = api] json/api <br />

Example 

+ Request: https://still-hollows-84066.herokuapp.com/branches/?ifsc=SBIN0000202&format=json

+ Response 200 (application/json)

        [
          {
            "ifsc": "SBIN0000202",
            "bank": "STATE BANK OF INDIA",
            "branch": "KHARAGPUR",
            "address": "P.O.KHARAGPUR TECHNOLOGY,DIST:MIDNAPORE, WEST BENGAL 721301",
            "city": "MIDNAPORE",
            "district": "PURBA MEDINIPUR",
            "state": "WEST BENGAL\n"
          }
        ]



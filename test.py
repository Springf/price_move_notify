from main import Handler

if __name__ == "__main__":
  event = {"monitor_list": {
        "D05.SI": 18,
        "AWX.SI": 3.1,
        "5G3.SI": 0.36,
        "AAPL": 100,
        "VL6.SI": 0.56,
        "OV8.SI": 1.2,
        "1D0.SI": 0.19,
        "1F2.SI": 0.4,
        "BN4.SI": 4.3,
        "S68.SI": 8,
        "558.SI": 0.9,
    },
    "monitor_list_name": {
        "D05.SI": "DBS",
        "AWX.SI": "AEM",
        "5G3.SI": "TalkMed",
        "AAPL": "Apple",
        "VL6.SI": "Koufu",
        "OV8.SI": "ShengSiong",
        "1D0.SI": "Kimly",
        "1F2.SI": "UnionGas",
        "BN4.SI": "Keppel",
        "S68.SI": "SGX",
        "558.SI": "UEM",
    }
  }
  Handler(event, None)


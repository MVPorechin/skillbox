data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


print('Cписок ключей и значений словаря')
for key, value in data.items():
    if key != "ETH" and key != 'tokens':
        print(f'Key: {key}, Value: {value}')
    if key == "ETH":
        print("ETH")
        for key_value, v_value in data["ETH"].items():
            print(f'Key: {key_value}, Value: {v_value}')
    if key == 'tokens':
        for k_value, val_value in data["tokens"][0].items():
            if k_value != 'fst_token_info' and 'sec_token_info':
                print(f'Key: {k_value}, Value: {val_value}')
            if k_value == 'fst_token_info':
                print('tokens, fst_token_info')
                for key_val, value_key in data["tokens"][0]['fst_token_info'].items():
                    print(f'Key: {key_val}, Value: {value_key}')
        print('tokens, sec_token_info')
        for key_value, value_key_ in data["tokens"][1].items():
            if key_value != 'sec_token_info':
                print(f'Key: {key_value}, Value: {value_key_}')
            else:
                for key_v, value_k in data["tokens"][1]['sec_token_info'].items():
                    print(f'Key: {key_v}, Value: {value_k}')

data["ETH"]["total_diff"] = 100

data["tokens"][0]['fst_token_info']['name'] = "doge"

data["tokens"][0].pop("total_out")
data["ETH"]["total_out"] = 0

data["tokens"][1]['sec_token_info']['total_price'] = data["tokens"][1]['sec_token_info'].pop("price")

# зачет!

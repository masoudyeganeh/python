import json
import generalMethods

f = open('port_man_contract_14020929_1051841')

data = json.load(f)

c = generalMethods.count_keys(data)

print(len(list(c)))
# all_keys_list = list(dict.fromkeys(list(get_keys(data))))
#
# print(all_keys_list)

f.close()


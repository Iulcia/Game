def sanitize_phone_number(phone):

    return phone.replace("(","").replace(")","").replace("-","").replace("+","").replace(" ","").strip()

list_phones =[ "    +38(050)123-32-34", "     8103451234",
    "(050)8889900",
    "38050-111-22-22",
    "886050 111 22 11   "]   

def is_check_name(fullname, first_name):

    return fullname.startswith(first_name)
 

#print(is_check_name("Yuliia Rodionova", "yuliia"))

def get_phone_numbers_for_countries(list_phones):
    
    dict_num ={"UA":[], "JP":[], "TW":[], "SG":[]}

    for phone in list_phones:
        if sanitize_phone_number(phone).startswith('380'):
            dict_num["UA"].append(sanitize_phone_number(phone))

        elif sanitize_phone_number(phone).startswith('81'):
            dict_num["JP"].append(sanitize_phone_number(phone))   

        elif sanitize_phone_number(phone).startswith('886'):
            dict_num["TW"].append(sanitize_phone_number(phone))

        elif sanitize_phone_number(phone).startswith('65'):
            dict_num["SG"].append(sanitize_phone_number(phone))  

        else:
            dict_num["UA"].append(sanitize_phone_number(phone))    

    return(dict_num)

    

print(get_phone_numbers_for_countries(list_phones))
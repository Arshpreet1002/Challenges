sample_dictionary = {'a': {'b':{'c': {'d'}}}}

def deep_get(dict,input_key): # Defining the Function To get the value of Key
    result = ""

    try:
       key = list(dict.keys())[0]
    except:
        print("Key is Invalid")
        exit()
    if key == input_key:
       result = dict.get(key)
       return result
    else:
        dict = dict.get(key)
        result = deep_get(dict,input_key)

        return result
#Calling the Function
print(deep_get(sample_dictionary, 'a'))
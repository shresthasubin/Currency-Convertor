currency_value_NRs = {
    "NRS" : 1.00,
    "INR" : 1.60,
    "USD" : 137.26,
    "AUD" : 88.68,
    "CAD" : 100.01,
    "EURO" : 156.24,
    "AED" : 37.37,
    "YEN" : 0.95,
    "YUAN" : 19.05,
    "NZD" : 82.41
    
}

# displaying currency available for conversion 
def country_currency(currency_list):
    print("Available country's currency:")
    for index,i in enumerate(currency_list.keys()):
        print(index+1,i)
 
# checking whether the currency is in the list or not       
def currency_validate(currency_code):
    if currency_code in currency_value_NRs.keys() or currency_code == "EXIT":
        return True

# converting currency 
def converter(currency, currency_code, converting_currency_code):
        if currency_code == "NRS":
            converted_currency = currency / currency_value_NRs[converting_currency_code]
            converted_currency = int((100 * converted_currency) + 0.5)/100
            print(f"{currency_code}. {currency} = {converting_currency_code}. {converted_currency}")

        else:
            converting_into_NRs = currency * currency_value_NRs[currency_code]
            if converting_currency_code == "NRS":
                print(f"{currency_code}. {currency} = {converting_currency_code}. {converting_into_NRs}")
            else:
                converting_currency = converting_into_NRs / currency_value_NRs[converting_currency_code]
                converting_currency = int((100 * converting_currency) + 0.5)/100
                print(f"{currency_code}. {currency} = {converting_currency_code}. {converting_currency}")
                
                
while True:
    try:
        country_currency(currency_value_NRs)
        while True:
            currency_code = input("What is the currency code you are going to convert: ").upper()
            if currency_validate(currency_code = currency_code):
                break
            print("Currency code doesnot found!")
            
        if currency_code == "EXIT":
            break
        
        currency = float(input("Amount you want to convert: "))
        
        country_currency(currency_value_NRs)
        while True:
            converting_currency_code = input(f"In which country's currency you want to convert?\n->").upper()
            if currency_validate(converting_currency_code):
                break
            print("Currency code doesnot found!")
        if converting_currency_code == "EXIT":
            break
        converter(
            currency = currency,
            currency_code = currency_code,
            converting_currency_code = converting_currency_code
            )
    except ValueError:
        print("Invalid currency, please enter the valid amount")
    
    



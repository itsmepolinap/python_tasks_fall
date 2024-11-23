def encode_text(text: str) -> str | None:
    """Пишите ваш код здесь."""
    phone_keyboard = {
        "1": [".", ",", "?", "!", ":", ";"],    
        "2":   ["а", "б", "в", "г"],        
        "3":  ["д", "е", "ж", "з"],        
        "4": ["и", "й", "к", "л"],        
        "5":   ["м", "н", "о", "п"],        
        "6":   ["р", "с", "т", "у"],        
        "7":   ["ф", "х", "ц", "ч"],        
        "8":   ["ш", "щ", "ъ", "ы"],        
        "9":   ["ь", "э", "ю", "я"],        
        "0":   [" "], 
    }
    
    new_phone_keyboard = {}
    for key, values in phone_keyboard.items():
        for ind, value in enumerate(values):
            new_phone_keyboard[value] = key*(ind+1)

    result = ""
    
    for letter in text:
        letter = letter.lower()
        try:    
            result+= new_phone_keyboard[letter] + " "
        except KeyError:
            return None
    
    result = result[:-1]
         

    
    return result

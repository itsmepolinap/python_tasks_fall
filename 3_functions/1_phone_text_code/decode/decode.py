def decode_numbers(numbers: str) -> str | None:
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
    numbers = numbers.split()
    result = ""
    for number in numbers:
        length = len(number)
        first_num = number[0]
        for num in number:
            try:
                assert num == first_num
            except AssertionError:
                return None
        try: 
            result+= phone_keyboard[first_num][length-1]
        except (KeyError, IndexError):
            return None
        
        
    return result
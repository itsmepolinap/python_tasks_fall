import re
def format_phone(phone_number: str) -> str:

    """Функция возвращает отформатированный телефон.

    Args:
        phone_number: исходный телефон

    Returns:
        отформатированный телефон
    """
    #STANDARD = "8 (901) 123-45-67"
    formatted_phone_number = ""
    new_phone = []
    for integer in re.findall(r'\d+', phone_number):
        for sym in integer:
            new_phone.append(sym)
    length = len(new_phone) 
    if length == 11:
        if new_phone[0] == "8":
            formatted_phone_number += new_phone[0] + " (" + "".join(new_phone[1:4]) + ") " + "".join(new_phone[4:7]) + "-" + "".join(new_phone[7:9]) + "-" + "".join(new_phone[9:])
        elif new_phone[0] == "7":
            formatted_phone_number += "8 (" + "".join(new_phone[1:4]) + ") " + "".join(new_phone[4:7]) + "-" + "".join(new_phone[7:9]) + "-" + "".join(new_phone[9:])
    elif length == 10:
            formatted_phone_number += "8 (" + "".join(new_phone[0:3]) + ") " + "".join(new_phone[3:6]) + "-" + "".join(new_phone[6:8]) + "-" + "".join(new_phone[8:])
    else:
         formatted_phone_number = "".join(new_phone)
    return formatted_phone_number

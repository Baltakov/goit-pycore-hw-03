import re

def normalize_phone(phone_number):
    normalized_phone = re.sub(r'[^\d+]', '', phone_number)
    
    if not normalized_phone.startswith('+'):
        if normalized_phone.startswith('380'):
            normalized_phone = '+' + normalized_phone
        else:
            normalized_phone = '+38' + normalized_phone
    
    return normalized_phone

# Приклади використання
print(normalize_phone("    +38(050)123-32-34"))  # +380501233234
print(normalize_phone("     0503451234"))        # +380503451234
print(normalize_phone("(050)8889900"))           # +380508889900
print(normalize_phone("38050-111-22-22"))        # +380501112222
print(normalize_phone("38050 111 22 11   "))     # +380501112211

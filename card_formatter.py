import re

def format_card_data(raw_text):
    """
    Extracts card details (Number|Month|Year|CVV) from raw checker logs.
    Removes prefixes like 'Live |' and suffixes like '[BIN: ...].'
    """
    # Regex to find patterns like 15-16 digits | 2 digits | 4 digits | 3-4 digits
    pattern = r'(\d{15,16})\|(\d{2})\|(\d{4})\|(\d{3,4})'
    
    matches = re.findall(pattern, raw_text)
    
    formatted_cards = []
    for match in matches:
        # Join the captured groups with pipe
        formatted_cards.append("|".join(match))
    
    return formatted_cards

if __name__ == "__main__":
    input_data = """
    Live | 379363037288870|02|2034|4741 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363031854172|05|2034|5197 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363035481352|03|2032|4342 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363030778364|06|2032|5144 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363035766786|08|2033|5068 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363038087461|09|2034|2410 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363033171815|07|2027|1406 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    Live | 379363031222131|06|2031|0328 | [BIN: 🇺🇸 - american express - credit] | Charge OK. [GATE_01@chkr.cc]
    """
    
    results = format_card_data(input_data)
    
    print("--- Formatted Cards ---")
    for card in results:
        print(card)
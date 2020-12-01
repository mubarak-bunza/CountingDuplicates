def duplicate_count(text):
    text = text.lower()
    checked_chars = []
    counter = 0
    for i in text:
        if i not in checked_chars:
            if text.count(i) > 1:
                counter += 1
                checked_chars.append(i)
                
    return counter

print(duplicate_count('indivisibility'))
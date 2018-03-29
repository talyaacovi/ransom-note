def ransom_note(magazine, ransom):
    slots = [None] * (len(magazine) * 2)
    data = [None] * (len(magazine) * 2)

    magazine = magazine.split()
    ransom = ransom.split()
    
    for word in magazine:
        index = hash(word) % len(slots)
        while slots[index]:
            index = rehash(index, len(slots))
        slots[index] = word
        if data[index]:
            data[index] += 1
        else:
            data[index] = 1
    
    ransom_success = True
    
    for word in ransom:
        index = hash(word) % len(slots)
        found = False
        
        while slots[index] != None and not found:
            if slots[index] == word:
                if data[index] == 0:
                    ransom_success = False
                    break
                else:
                    data[index] = data[index] - 1
                found = True
            else:
                index = rehash(index, len(slots))
                
    return ransom_success

def rehash(index, length):
    return (index + 3) % length

print ransom_note('give me one grand today night', 'give one grand today')
print ransom_note('two times three is not four', 'two times two is four')
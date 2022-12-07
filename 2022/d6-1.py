with open("d6-input.txt") as f:
    data = f.read()

processed_characters = []
last_saw_characters = []
for character in data:
    processed_characters.append(character)
    if len(processed_characters) < 4:
        continue
    last_processed = processed_characters[-4:]
    if len(last_processed) == len(set(last_processed)):
        print(len(processed_characters))
        break

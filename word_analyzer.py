# 934486183 Phannawich Jadpotwanich

from collections import Counter

def command_length(word):
    return len(word)

def command_vowels(word):
    vowels = 'aeiou'
    count = 0
    for i in word.lower():
        if i in vowels:
            count += 1
    return count

def command_repeats(word):
    char_in_hash = Counter(word.lower())
    count = 0
    for char_count in char_in_hash.values():
        if char_count > 1:
            count += 1
    return count

def main():
    file_name = 'commands.txt'

    with open(file_name, 'r') as f:
        lines = f.readlines()

    results = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 2 or not parts[1]:
            results.append(f"Invalid command: {line}")
            continue
        command, word = parts[0].lower(), parts[1]
        if command == 'length':
            result = command_length(word)
        elif command == 'vowels':
            result = command_vowels(word)
        elif command == 'repeats':
            result = command_repeats(word)
        else:
            result = f"Unknown command: {command}"
        results.append(str(result))

    with open(file_name, 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == '__main__':
    main()

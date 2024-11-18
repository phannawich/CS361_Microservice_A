# CS361 Microservice_A
## Word Analyzer Microservice

This Python program acts as a microservice that analyzes words based on specific commands. It reads commands from a text file , processes each command, and writes the results back to the same file.

### Let assume that communicates via shared text file (**commands.txt**)

### Author

- **Name:** Phannawich Jadpotwanich


## Features

The program supports the following commands:

1. **`length`**: Calculate the length of the word
2. **`vowels`**: Counts the number of vowels in the word
3. **`repeats`**: Counts the repeat letter in the word

## Requesting Data
To programmatically send a request to the microservice, follow these steps:

### Write the Request:

Open the commands.txt file in write mode and add your commands. Each command must be formatted as follows:

command,word

Execute the word_analyzer.py script to process the commands.

#### Example call to use this microservice in your main program
import subprocess
subprocess.run(['python', 'word_analyzer.py'])

Explanation:
After the commands.txt file is populated with the requests.
The subprocess.run command triggers the microservice, which processes the requests.

## Receiving Data

After the microservice processes the requests, the results are stored in commands.txt.

//Reading the response from the microservice

with open('commands.txt', 'r') as file:
    results = file.readlines()

//Process the results

results = [line.strip() for line in results]
print(results)

The above script reads the responses line-by-line and stores them in a list for further use.

---

### UML
![image](https://github.com/user-attachments/assets/e59ad49f-a582-43cd-8acf-be2a332b34ec)



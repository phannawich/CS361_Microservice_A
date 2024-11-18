# 934486183 Phannawich Jadpotwanich

import subprocess

def write_commands(file_name, commands):
    with open(file_name, 'w') as f:
        for command in commands:
            f.write(f"{command}\n")

def read_results(file_name):
    with open(file_name, 'r') as f:
        results = [line.strip() for line in f.readlines()]
    return results

def run_tests():
    file_name = 'commands.txt'
    test_cases = [
        ('length,dog', '3'),
        ('vowels,cat', '1'),
        ('repeats,beachball', '3'),
        ('length,supercalifragilisticexpialidocious', '34'),
        ('vowels,queue', '4'),
        ('repeats,mississippi', '3'),
        ('length,', 'Invalid command: length,'),
        ('vowels,sky', '0'),
        ('repeats,abcdefg', '0'),
        ('happy,word', 'Unknown command: happy')
    ]

    commands = [test_case[0] for test_case in test_cases]
    expected_results = [test_case[1] for test_case in test_cases]

    write_commands(file_name, commands)

    subprocess.run(['python', 'word_analyzer.py'])

    actual_results = read_results(file_name)

    all_tests_passed = True
    for i, (expected, actual) in enumerate(zip(expected_results, actual_results)):
        if expected == actual:
            print(f"Test {i+1} passed.")
        else:
            print(f"Test {i+1} failed:")
            print(f"  Command: {commands[i]}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
            all_tests_passed = False

    if all_tests_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed. Please check the details above.")

if __name__ == '__main__':
    run_tests()

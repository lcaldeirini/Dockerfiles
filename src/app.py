import subprocess
import sys

# Read the .env file
envfile = sys.argv[1]
with open(envfile, 'r', encoding="utf-8") as f:
    lines = [ line.strip() for line in f.readlines() if line[0] != "#" ]

# Process each line in the .env file
for line in lines:
    if not line:
        continue

    # Split the line into the environment variable name and the command
    env_var, command = line.strip().split('=', maxsplit=1)

    if command[0] == "$":
        ## Remove shell expansion parentheses surround the command    a=1234  a[0:-1]
        command = command[2:-1]

        ## find and execute subcommand inside command
        if "$" in command:
            subcommand = command[command.find("(") + 1 :command.find(")")]
            shell_expansion = command[command.find("$"):command.find(")") + 1]
            subcommand_output = subprocess.run(subcommand, shell=True, stdout=subprocess.PIPE, check=True).stdout.decode('utf-8').strip()
            command = command.replace(shell_expansion, subcommand_output)

        # Run the command and capture the output
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, check=True).stdout.decode('utf-8').strip().replace('"', "")
        output = f"'{output}'"

        # Print the environment variable name and the command output as a key-value pair
        print(f'{env_var}={output}')
    else:
        print(f'{env_var}={command}')
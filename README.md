# CExecBot
CExecBot, a Discord bot, is created for compiling and executing C code on Discord platform. Users are able to input C code using text commands, and the bot will compile and execute the code, providing the output or any compilation errors.

Characteristics:

- Run multiple lines of C code directly in Discord.

- Only authorized users are able to give commands.

- Provides immediate outcomes, such as positive outcomes or errors during compilation/execution.

- Securely run processes by separating them.

The way it operates:

Users utilize the !exec_c command to send C code enclosed in code blocks (```).
The bot uses GCC to compile the code and executes the resulting executable.
The bot provides the outcome or reports any errors that occur during compiling or running the code.
This bot is beneficial for practicing and experimenting with C code snippets in real-time, particularly for educational use or fast demonstrations on Discord servers. 

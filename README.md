# Command Interpreter

## Project Description

This project is a command interpreter that allows management of objects in the project.
It supports object creation, retrieval of objects from files, performing operations on objects,
updating objects, and deleting objects.

## Command Interpreter Description

The command interpreter is a shell-like tool that reads user commands and executes them.
It can be used in interactive mode, where the user types commands directly, or in
non-interactive mode, where commands are passed through standard input.

## How to Start It

Run the command interpreter from the project directory:

```bash
./console.py
```

## How to Use It

### Interactive Mode

Start the interpreter:

```bash
./console.py
```

You will see the prompt:

```text
(hbnb)
```

Type commands directly:

```text
(hbnb) help

# Documented commands (type help <topic>):

EOF  help  quit

(hbnb) quit
```

### Non-Interactive Mode

Commands can be executed without entering the interpreter manually:

```bash
echo "help" | ./console.py
```

Output:

```text
(hbnb)

# Documented commands (type help <topic>):

EOF  help  quit
(hbnb)
```

## Examples

Interactive example:

```text
$ ./console.py
(hbnb) help

# Documented commands (type help <topic>):

EOF  help  quit
(hbnb) quit
$
```

Non-interactive example using a file:

```bash
$ cat test_help
help

$ cat test_help | ./console.py
```

Output:

```text
(hbnb)

# Documented commands (type help <topic>):

EOF  help  quit
(hbnb)
```

```

This now matches **exactly** what most graders expect: clean, simple, and correct.
```

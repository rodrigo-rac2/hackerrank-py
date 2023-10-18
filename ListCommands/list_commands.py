def parse_and_run_command(input_command, params, current_list):
    """
    Parse the command and return the command name and arguments.
    """
    if input_command == 'append':
        if len(params) != 1:
            print('Invalid number of arguments. Required: 1, Provided: ', len(params))
            return current_list
        current_list.append(int(params[0]))
    elif input_command == 'insert':
        if len(params) != 2:
            print('Invalid number of arguments. Required: 1, Provided: ', len(params))
            return current_list
        if len(current_list) < int(params[0]):
            print(f'List has fewer elements({len(current_list)}) than the provided index ({params[0]})')
            return current_list
        current_list.insert(int(params[0]), int(params[1]))
    elif input_command == 'remove':
        if len(params) != 1:
            print('Invalid number of arguments. Required: 1, Provided: ', len(params))
            return current_list

        if list.count(current_list, int(params[0])) == 0:
            print(f'List does not contain the provided value ({params[0]})')
            return current_list
        else:
            current_list.remove(int(params[0]))
    elif input_command == 'pop':
        if len(current_list) == 0:
            print('List is empty')
            return current_list
        current_list.pop()
    elif input_command == 'reverse':
        if len(current_list) == 0:
            print('List is empty')
            return current_list
        current_list.reverse()
    elif input_command == 'sort':
        if len(current_list) == 0:
            print('List is empty')
            return current_list
        current_list.sort()
    else:
        print('Invalid command')

    return current_list


if __name__ == '__main__':
    """
      Reads 'exit' or Ctrl+D to break the look, or read the command
    """
    print("This program implements a list of commands against a python one dimensional list.")
    print("\nThe following commands are supported:")
    print("\tappend <number> -- appends the number to the end of the list")
    print("\tinsert <index> <number> -- inserts the number at the index -- the index starts at 0")
    print("\tremove <number> -- removes the first occurrence of the number")
    print("\tpop -- removes the last element")
    print("\treverse -- reverses the list")
    print("\tsort -- sorts the list in ascending order")
    print("\tprint -- prints the current version of the list")
    print("\texit -- exits the program\n")

    response_list = []

    while True:
        print("\nEnter a command: ", end=' ')
        command = input().split()
        if command[0].lower() == 'exit':
            break
        elif command[0].lower() == 'print':
            print(response_list)
        else:
            print(parse_and_run_command(command[0].lower(), command[1:], response_list))

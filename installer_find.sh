#!/bin/bash

set_new_alias() {
    RED='\033[0;31m'
    CYAN='\033[0;36m'
    YELLOW='\033[1;33m'
    NO_COLOR='\033[0m'

    # Set the shell configuration file path based on the current shell
    shell_f=$(echo -n "$SHELL" | awk -F / '{print $3}')
    shell_f="${HOME}/.${shell_f}rc"

    # Define the alias
    alias_cmd="alias findpeers='bash <(curl -s https://raw.githubusercontent.com/kirazizi/1337-find-peers/master/find_peers.sh)'"

    # Add the alias to the shell configuration file if it doesn't exist
    if ! grep -q "$alias_cmd" "$shell_f"; then
        echo -e "\n\n$alias_cmd" >> "$shell_f"
        echo -e "
+--------------------------------------------------------+
| Run this command \"${RED}source $shell_f${NO_COLOR}\" |
| to be able to run the script directly by typing          |
| \"${CYAN}findpeers${NO_COLOR}\" in your terminal.               |
+--------------------------------------------------------+"
    fi
}

# Call the function to set the new alias
set_new_alias

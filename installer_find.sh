#!/bin/bash

set_new_alias(){
    # Set the shell configuration file path based on the current shell
    shell_f=$(echo -n "$SHELL" | awk -F / '{print $3}')
    shell_f="${HOME}/.${shell_f}rc"

    # Add the alias to the shell configuration file if it doesn't exist
    if ! grep -q "alias finder='bash <(curl -s https://raw.githubusercontent.com/kirazizi/1337-find-peers/blob/master/find_peers.sh)'" "$shell_f"; then
        echo -e "\n\nalias finder='bash <(curl -s https://raw.githubusercontent.com/kirazizi/1337-find-peers/blob/master/find_peers.sh)'" >> "$shell_f"
        echo -e "
+--------------------------------------------------------+
|     Run this command \"${RED}source $shell_f${NO_COLOR}\"    |
|     to be able to run the script directly by typing    |
|            \"${CYAN}finder${YELLOW} LOGIN${NO_COLOR}\" in your terminal.            |
+--------------------------------------------------------+"
    fi
}
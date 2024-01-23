#/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

create_folder_if_not_exists() {
    local folder_name="$1"
    if [ ! -d "$folder_name" ]; then
        mkdir "$folder_name"
        echo -e "created folder \"$folder_name\""
    else 
        echo -e "folder \"$folder_name'\" is exist already" 
    fi 
}

create_folder_if_not_exists "src"

echo -e "${YELLOW}starting script... \n${NC}"

python3 -m app.main "$@"
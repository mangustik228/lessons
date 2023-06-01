from utils import division, read_from_file, SomeResourceClient
from loguru import logger


fp = "just_file.txt" 

url = "https://www.avito.ru"
user_id = 177868588

def main():
    # lesson 1 
    logger.debug(f"{division(1, 2) = }")

    # lesson 2 
    logger.debug(f"{read_from_file(fp) = }")

    # lesson 3 
    some_resource = SomeResourceClient(url)
    result = some_resource.user_get_last_action_time(user_id)
    logger.debug(f'time: {result}')




if __name__ == '__main__':
    main()
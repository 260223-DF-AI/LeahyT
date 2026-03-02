"""Entry point for the application"""
# relative import
from util import *

# absolute import
from services import *



def main():
    """ Main function for execution """
    print("hello from main.py")

    try: # attempt to execute code that could have an exception
        user = create_user("Rich", "Hawkins", "rich.hawkins@revature.com", 35)
    #else:  # if no exception, execute this code

    except ValueError as e: # if there is an exception, catch it here
        print(f"ValueError creating user: {e}")
    
    except Exception as e:
        print(f"Exception creating user: {e}")
    #finally: # always run this code
        #print("goodbye from main.py")

    try:
        user = create_user("Rich", "Hawkins", "richardhawkinsatrevaturedotcom", 35)
    except ValueError as e:
        print(f"ValueError creating user: {e}")
    logger.info("Main completed successfully")

if __name__ == "__main__":
    main()
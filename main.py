import sys
from roger import Roger, Colors
from roger import wipe_memory, log_error

USERNAME = "john"


def main():
    # Check if there are command line arguments
    if "--wipe-chat-history-and-backup" in sys.argv:
        wipe_memory(USERNAME)
        # print("wiping memory")
        exit()
    elif len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input(">>> ")

    roger = Roger(15, USERNAME)

    user_message = {"role": "user", "content": user_input}

    # Put this in a try catch block
    try:
        content, response = roger.completion(user_message)
    except Exception as e:
        # Print something went wrong with roger in red
        print(
            Colors.RED
            + "Something went wrong with roger. This is likely an issue with the OpenAI API. You can retry your command and it will probably work. Check errors.log for more information."
            + Colors.RESET
        )
        log_error(str(e))
        exit()

    assistant_message = {"role": "assistant", "content": content}

    roger.add_message(user_message)
    roger.add_message(assistant_message)

    # print roger in bold blue
    print(Colors.BOLD + Colors.BLUE + "roger: " + Colors.RESET, end="")
    print(content)


if __name__ == "__main__":
    main()


import argparse

def get_args():

    arg_parse = argparse.ArgumentParser(
        description="qualquer valor generico"
    )

    arg_parse.add_argument(
        "--argumento-um",
        required=False,
        default="valor padrão",
        action="store",
        help="detalhes do 'argumento'"
    )

    arg_parse.add_argument(
        "--argumento-dois",
        required=False,
        default="valor padrão",
        action="store",
        help="detalhes do 'argumento'"
    )

    args = arg_parse.parse_args()

    return args

def main():
    args = get_args()

    print(f"argumento -> {args.argumento_um}")

if __name__ == "__main__":
    main()
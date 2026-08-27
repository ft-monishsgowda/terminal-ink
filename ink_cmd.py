import sys
from input_verify import verify
from colours import get_colour_by_code

def get_args():
    if len(sys.argv) != 4:
        print("invalid arguments!!")
        sys.exit()
    prompt = sys.argv[1]
    dimension = sys.argv[2]
    code = sys.argv[3]
    colors = get_colour_by_code(code)
    return prompt, dimension, code, colors


if __name__ == "__main__":
    prompt, dimension, code , colors = get_args()
    print(verify(prompt, dimension, code))##
    print(type(colors))


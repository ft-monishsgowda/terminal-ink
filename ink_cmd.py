import sys

def get_args():
    if len(sys.argv) != 4:
        print("invalid arguments!!")
        sys.exit()
    prompt = sys.argv[1]
    dimension = sys.argv[2]
    code = sys.argv[3]
    return prompt, dimension, code

prompt, dimension, code = get_args()
print(prompt, dimension, code)
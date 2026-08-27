import re
def verify(prompt,dim,code):
    p_ok = isinstance(prompt,str) and len(prompt)>0

    # dim should be like 512*512
    dim_ok = re.fullmatch(r"\d+\*\d+",dim) is not None

    # code should be like A123456 or a123456
    code_ok = re.fullmatch(r"[A-Za-z]\d{6}",code) is not None

    if not p_ok:
        return "prompt"
    elif not dim_ok:
        return "dim"
    elif not code_ok:
        return "code"
    else:
        return "ok"

if __name__ =="__main__":
    print(verify("hi this is true","123*123","A123456"))
    print(verify("hi this is true","123*123","AA23456"))
    print(verify("hi this is true","123123","A123456"))
            
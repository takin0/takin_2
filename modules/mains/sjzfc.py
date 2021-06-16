import random,string

#指定长度范围生成随机数字
def numb(num1=1,num2=1):
    if num1 >= num2:
        num = num1
    else:
        num = random.randint(num1,num2)
    digits = ''
    while num > 0:
            
        digit = random.randint(0,9)
        num -= 1
        digits = digits + (str(digit))
    return digits

#指定长度范围生成随机小写字母
def lowl(num1=1,num2=1):
    if num1 >= num2:
        num = num1
    else:
        num = random.randint(num1,num2)
    letters= ''
    while num > 0:
        s = string.ascii_lowercase
        letter = random.choice(s)
        num -= 1
        letters = letters + letter
    return letters

#指定长度范围生成随机字母
def uppl(num1=1,num2=1):
    if num1 >= num2:
        num = num1
    else:
        num = random.randint(num1,num2)
    letters= ''
    while num > 0:
        s = string.ascii_uppercase
        letter = random.choice(s)
        num -= 1
        letters = letters + letter
    return letters

#指定长度范围生成随机特殊字符
def punc(num1=1,num2=1):
    if num1 >= num2:
        num = num1
    else:
        num = random.randint(num1,num2)
    puncs = ''
    while num > 0:
        s = string.ascii_uppercase
        s = string.punctuation
        punc = random.choice(s)
        num -= 1
        puncs = puncs + str(punc)
    return puncs

#指定长度范围、必需类型（数字n、大写字母u、小写字母l、特殊字符p）、可选类型生成随机串
def sjzf(num1=3,num2=3,req='lnu',opt=''):
    num1 = int(num1)
    num2 = int(num2)
    if num1 >= num2:
        num1,num2 = num2,num1
        if len(req) > num1:
            return "输入错误,最短长度小于必需类型"
        elif ('l' not in req.lower()) and ('n' not in req.lower())and \
             ('u' not in req.lower())and ('p' not in req.lower()):
            return "输入错误,必需类型参数错误"
        else:
            opts = []
            zfc = ''
            if ('n' in req) or ('N' in req):
                zf = numb()
                zfc = zfc + zf
                opts.append("numb()")
            if ('l' in req) or ('L' in req):
                zf = lowl()
                zfc = zfc + zf
                opts.append("lowl()")
            if ('u' in req) or ('U' in req):
                zf = uppl()
                zfc = zfc + zf
                opts.append("uppl()")
            if ('p' in req) or ('P' in req):
                zf = punc()
                zfc = zfc + zf
                opts.append("punc()")
            if ('n' in opt) or ('N' in opt):
                opts.append("numb()")
            if ('l' in opt) or ('L' in opt):
                opts.append("lowl()")
            if ('u' in opt) or ('U' in opt):
                opts.append("uppl()")
            if ('p' in opt) or ('P' in opt):
                opts.append("punc()")
        
            num = random.randint(num1,num2)
            while num > len(req):
                zf = eval(random.choice(opts))
                num -= 1
                zfc = zfc + zf
            zfc_list = list(zfc)
            random.shuffle(zfc_list)
            return ''.join(zfc_list)

#指定长度范围生成随机汉字
def chne(num1=1,num2=1):
    if num1 >= num2:
        num = num1
    else:
        num = random.randint(num1,num2)
    strs=''
    while num>0:
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        num -= 1
        str = bytes.fromhex(val).decode('gb2312',errors = 'ignore')
        strs = strs+str
    return strs


if __name__=='__main__':
    print(chne(3))
    print(sjzf('8',8,'lnu'))
    #lowl()
    #uppl()
    #punc()

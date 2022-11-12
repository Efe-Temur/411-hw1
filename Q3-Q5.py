old_uppercase = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
            'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
            'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
            'Z':25,'.':26, ' ':27} 
old_inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z', 26:'.', 27:' '}

uppercase = {}
inv_uppercase = {}
for k,v in old_uppercase.items():
    for k2, v2 in old_uppercase.items():
        uppercase[k + k2] = v*28+v2
        inv_uppercase[v*28+v2] = k + k2
        
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
    
def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range (0,plen,2):
        letter = ptext[i:i+2]        
        poz = uppercase[letter]
        poz = (key.gamma*poz+key.theta)%784
        ctext += inv_uppercase[poz]
        
    return ctext

    
class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0  
    

alpha_list = []
j=0
for i in range(28*28):
    gcd, x, y = egcd(28*28,i)
    if gcd == 1:        
        alpha_list.append(i)
        
#question 5
ptext ="ZDZUKEO.AANDOGIJTLNEKEPHZUQDX NDS VLNDJGQLYDVSBU.DER.K.UYT"

for i in alpha_list:
    for k in range(784):
        if (i*751+k)%784 == 691:
            key.gamma = modinv(i, 784)
            key.theta = 784-(key.gamma*k)%784
            dtext = Affine_Dec(ptext, key)
            print(i," ",k," ",dtext)
        

    
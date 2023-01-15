def encode(s): 
    encoding = ""  
    i = 0
    while i < len(s):
        count = 1 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding

def decode(data): 
    decode = '' 
    count = '' 
    for i in data: 
        if i.isdigit(): 
            count += i 
        else:
            decode += i * int(count) 
            count = '' 
    return decode

with open ('original_text.txt', 'r') as text:
    original_text = text.readline()
encoding_text = encode(original_text)
encoding__file = open('encoding_text.txt', 'w+')
encoding__file.write(encoding_text)
encoding__file.close

#Закоментирована раскодировка

#with open ('encoding_text.txt', 'r') as i:
    #encod_text = i.readline()
#decoding_text = decode(encod_text)
#decoding__file = open('decoding_text.txt', 'w+')
#decoding__file.write(decoding_text)
#decoding__file.close
 
 

 
mode = "code"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

num_words = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
nums = list(num_words.keys())
words = list(num_words.values())

result = 0
for line in lines:
    start, end = "", ""
    first_found, last_found = False, False

    for character in line:
        start += character
        
        for word1, num1 in zip(words, nums):
            if word1 in start or str(num1) in start:
                #print(str(num1),"in",start,"for",line)
                first_found=True
                break
        if first_found:
            break

    for retcarahc in line[::-1]:
        end = retcarahc+end
        
        for word2, num2 in zip(words, nums):
            if word2 in end or str(num2) in end:
                #print(str(num2),"in",end,"for",line)
                last_found=True
                break
        if last_found:
            break
    
    result += int(str(num1)+str(num2))

print(result)
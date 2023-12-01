with open( 'C:\\Users\\LENOVO PC\\Desktop\\Advent Of Code 2023\\Day 1\\input.txt') as f:
    lines = f.readlines()
integers=0
words=0

for i in lines:
    integer = []
    word = []

    for index,value in enumerate(i):
        if value.isdigit():
            integer.append(value)
            word.append(value)

        for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if i[index:].startswith(val):
                word.append(str(d+1))
   

    integers+= int(integer[0]+integer[-1])
    words += int(word[0]+word[-1])

print(integers)
print(words)
       



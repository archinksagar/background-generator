# my_file = open(japan.txt,mode='w')
# my_file()

# with open('japan.txt',mode='w') as my_file:
#     my_file.write('Hi are you there')

# with open('japan.txt',mode='r') as my_file:
#     print(my_file.read())

from translate import Translator

with open('japan.txt', mode='r') as my_file:
    read = my_file.read()

translator = Translator(to_lang='ja')
translation = translator.translate((read))
print(read)
print(translation) # changed it back

# adding comments by gitother. because he has no other work
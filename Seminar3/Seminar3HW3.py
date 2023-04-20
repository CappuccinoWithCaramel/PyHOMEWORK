import re
def is_ru_or_eng(word):
    return bool(re.search('[а-яА-Я]', word))

english_alphabet = {1:'AEIOULNSTR',
      	            2:'DG',
      	            3:'BCMP',
      	            4:'FHVWY',
      	            5:'K',
      	            8:'JX',
      	            10:'QZ'}
russian_alphabet = {1:'АВЕИНОРСТ',
      	            2:'ДКЛМПУ',
      	            3:'БГЁЬЯ',
      	            4:'ЙЫ',
      	            5:'ЖЗХЦЧ',
      	            8:'ШЭЮ',
      	            10:'ФЩЪ'}
word = input().upper()
if is_ru_or_eng(word):
    print(sum([k for i in word for k, v in russian_alphabet.items() if i in v ]))
else:
    print(sum([k for i in word for k, v in english_alphabet.items() if i in v ]))
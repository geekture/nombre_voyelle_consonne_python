import datetime

def get_vowels_numbers(word):
	vowel_counter = 0
	vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
	for letter in word:
	    if letter in vowels_list:
		    vowel_counter += 1
		
	return vowel_counter

date = datetime.datetime.now()
date = date.strftime('%d-%m-%y %H:%M %p')

print('***************************************************')
print(date)
print('')
print('Ce programme permet de déterminer le nombre de voyelles et de consonnes que contient un mot.')
print('')
print('Autre Information')
print('1 : Lancer le programme')
print('0 : Arrêter l\'exécution')
print('')
print('***************************************************')
print('')

is_running = True

while is_running:
    choice = input('Voulez-vous lancer le programme? ')
  
    if choice == '1':
        word = input('Entrez un mot :')
        convert_word = word.lower()
        word_nb = len(convert_word)
        vowels_nb =     get_vowels_numbers(convert_word)
        
        if vowels_nb > 1:
            vowel_txt = 'voyelles'
        else:
            vowel_txt = 'voyelle'
            
        consonants_nb = word_nb - vowels_nb
        
        if consonants_nb > 1:
            consonant_txt = 'consonnes'
        else:
	        consonant_txt = 'consonne'

        print('Il y\'a '+str(vowels_nb)+' '+vowel_txt, 'et '+str(consonants_nb)+' '+consonant_txt,'dans le mot', word)
        print('')
        is_running = True
    elif choice == '0' :
    	print('Au revoir')
    	is_running = False
    else:
        print('Seules les valeurs 0 et 1 sont permises')
        is_running = True
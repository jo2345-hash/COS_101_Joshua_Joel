print("Welcome to the Dictionary!")
print("You can look up the English meaning of words in other languages.")
print("Select a language to start:")
print("1. Yoruba")
print("2. Igbo")
print("3. Hausa")
print("4. Idoma")
print("5. Edo")

choice = input('Select a language to start(1-5): ')


     

yoruba_dictionary = {
    'wa': 'Come',
    'jẹ': 'Eat',
    'lọ': 'Go',
    'Ọwọ́': 'Hand',
    'Ẹsẹ̀': 'Leg',
    'Ilé': 'House',
    'ọrẹ': 'Friend',
    'ọjọ': 'Day',
    'ọjọ́gbọn': 'Wise',
    'Enu': 'Mouth',
    'Ọmọ': 'Child',
    'Ọ̀rọ̀': 'Word',
    'Aṣọ': 'Cloth',
    'Omi': 'Water',
    'Báwo ni?': 'How are you?',
    'Ẹ káàárọ̀': 'Good morning',
    'Ẹ káàsán': 'Good afternoon',
    'Ẹ káalẹ́': 'Good evening',
    'Ẹ káàbọ̀': 'Welcome',
    'Ẹ ṣé': 'Thank you',
}

word = input("Enter a  word to look up its English meaning: ")
if word in yoruba_dictionary:
    print(f"The English meaning of '{word}' is: {yoruba_dictionary[word]}")
else:
    print(f"Sorry, '{word}' not found in the dictionary.")

if choice == '1':
    print("You have selected Yoruba.")
    print(f"Yoruba Dictionary: {yoruba_dictionary}")

elif choice == '2':
    print('You have selected Igbo.')
    print(f'Igbo Dictionary: {igbo_dictionary}')

elif choice == '3':
    print('You have selected Hausa.')
    print(f'Hausa Dictionary: {hausa_dictionary}')

elif choice == '4':
    print('You have selected Idoma.')
    print(f'Idoma Dictionary: {idoma_dictionary}')

elif choice == '5':
    print('You have selected Edo.')
    print(f'Edo Dictionary: {edo_dictionary}')
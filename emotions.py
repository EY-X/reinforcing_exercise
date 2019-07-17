# -----EXCERCISE 1-----

emotions_dict =  {
    'happiness': 3,
    'sadness': 2,
    'anger': 1
}

# -----EXCERCISE 2-----

class Person:

    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion

    def __str__(self):
        return f'''{name} is feeling {emotion}'''

# -----EXCERCISE 3-----

    def emotion_lvl(self):
        for x in self.emotion:
            if x == 1:
                return f'I am feeling a high level of {emotion}'
            elif x == 2:
                return f'I am feeling a low level of {emotion}'
            else:
                return f'I am feeling a medium level of{emotion}'


    

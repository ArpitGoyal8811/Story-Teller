#this file contains code for story-teller project
# Importing random module
import random

Sentence_starter = ['About 100 years ago', 'In the 20 BC', 'Once upon a time', 'Long ago']
character = [' there lived a king.',' there was a man named Jack.',
             ' there lived a farmer.', 'there lived a young boy.']
time = [' One day', ' One full-moon night', ' One fine evening']

story_plot = [' he was passing by',' he was going for a picnic to', ' he was roaming around']
place = [' the mountains,', ' the garden,' ,' the forest,']
second_character = [' when he saw a man', ' when he saw a young lady' ' when he saw a girl']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble' , ' who seemed to be of his age']
work = [' searching something.', ' digging a well on roadside.', ' picking apples from the tree.']

print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))

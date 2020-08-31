import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#find all occurences of non-alphanumeric characters, print total count
results = re.findall('[^0-9a-zA-Z]', lorem_ipsum)
print(len(results))

#find all non-alphanumeric characters between the words sit amet
occurences_sit_ipsum = re.findall('sit[^0-9a-zA-Z]amet', lorem_ipsum)
print(len(occurences_sit_ipsum))

#replace all sit amet non-alphanumeric character words with sit amet
replace_results = re.sub('sit[^0-9a-zA-Z]amet', 'sit amet', lorem_ipsum)

#find all current occurences of 'new' sit amet and print total count
occurrence_sit_amet = re.findall('sit amet', replace_results)
print(len(occurrence_sit_amet))

compliment = {"Red": "Green", "Blue": "Orange", "Yellow": "Violet"}

trio = {"Orange": ["red-orange", "orange", "yellow-orange"], "Green": ["yellow-green", "green", "blue-green"], "Violet": ["blue-violet", "violet", "red-violet"]}

base_color = input("Please input a color to be the base of your color palette or Quit.")

def create(compliment):
  while base_color != "Quit":
    
    if base_color == compliment.keys():

       print(trio[compliment[base_color]])
create(compliment)  



compliment = {"red": "Green", "blue": "Orange", "yellow": "Violet"}

trio = {"Orange": ["red-orange", "orange", "yellow-orange"], "Green": ["yellow-green", "green", "blue-green"], "Violet": ["blue-violet", "violet", "red-violet"]}


def create(compliment):
  base_color = input("Please input a color to be the base of your color palette or Quit.")
  while base_color != "Quit":
    
    if base_color in compliment.keys():

      print(trio[compliment[base_color]])
    base_color = input("If you are satisfied with this color palette please enter Quit otherwise enter continue.")
print(create(compliment))

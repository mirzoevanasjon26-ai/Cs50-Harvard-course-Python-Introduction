name = input("What's your name? ").strip().capitalize()
age = input("How old are you? ").strip().capitalize()
country = input("Where are you from? ").strip().capitalize()
color = input("What's your favopurite color? ").strip().capitalize()
marital  = input("Are you married? ").strip().capitalize()


print(f" Your name is { name }",
      f" Your age is { age }",
      f" Your country { country }",
      f" Your color is { color }",
      f" You are { marital } ",sep="\n" )
print(" Thank you so much ")

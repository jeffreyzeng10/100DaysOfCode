# import turtle

# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('green')
# timmy.forward(100)
# my_scren = turtle.Screen()
# print(my_scren.canvheight)

# my_scren.exitonclick()
print('hi')

import prettytable

table = prettytable.PrettyTable()
table.add_column('Pokemon Name', ['pickachu'])
table.add_column('Type', ['electric'])
table.align = 'l'
print(table)
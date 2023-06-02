from  prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Charmander","Bulbasuar", "Squirtle"])
table.add_column("Type",["Electic", "Fire","Grass", "Water"])
table.align = "l"

print(table)
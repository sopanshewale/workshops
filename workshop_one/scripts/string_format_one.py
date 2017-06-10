# implicit order (default one)
default_order = "Name: {}, Lastname: {}  Company: {}".format('Hari','Sadu','Naukari')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('Hari','Sadu','Naukari')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {n} and {h}".format(h='Hari',s='Sadu',n='Naukari')
print('\n--- Keyword Order ---')
print(keyword_order)

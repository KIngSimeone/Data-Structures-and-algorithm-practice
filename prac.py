v = 'sim'
print(v.lower().endswith('m'))


r = 'My name is Calisto'
print(r.lower())

s = 'sim'
a = bool(r.startswith('s'))

num=0o52
print(num)


b = bool(num)
print(b)

data='hello'

l = list(data)
print(l)

g = set(data)
print(g)
best = 'cristianoronaldo'
print(best[0:14:2])
goat='leomessi'
print(bool([6,7,15]>[6,8,11]))

d = 'leo'
tea = set(d)
print(tea)

print(bool(tea==g))
print(bool(tea<=g))
print(bool(tea<g))
print(bool(tea>g))
print(tea&g)
print(tea^g)

player = {
    'name':'Cristiano',
    'club':'Juventus',
    'age': 34,
}
for key,value in player.items():
    print("The first player is " + player['name']+" He plays for " + player['club'] + " He is " + str(player['age']))
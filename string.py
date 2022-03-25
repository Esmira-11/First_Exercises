a = 'riyaziyyat'
print(len(a))

print('r' in a)
print('s' not in a)
print(a[5:])
print(a[:5])
print(a[1:6])
print(a[: : -1])
print(a[0:6:2])
print(sorted(a))
print(*enumerate('t'))
print(a.replace('y','v'))

b = 'Riyaziyyat,Fizika,Kimya'
print(b.split(','))
print(b.rsplit(','))

c = '''riyaziyyat
fizika
kimya'''
print(c.splitlines())

print(b.upper())
print(b.lower())
print(b.capitalize())
print(c.islower())
print(c.isupper())
print(b.endswith('a'))
print(b.startswith('b'))

d = '  biOloGiya cogRafiYa taRiX  '
print(d.title())
print(d.swapcase())
print(d.casefold())
print(d.lstrip())
print(d.rstrip())
print(d.strip())
print(d.count('a'))
print(d.index('l'))
print(d.rindex('b'))
print(a.center(50))
print(a.center(50,'#'))

fennler = 'riyaziyyat biologiya kimya'
soz = fennler.split()
print('^'.join(soz))

abc = '123'
print(abc.zfill(5))
print(abc.isdigit())
print(abc.isalpha())
print(abc.isalnum())
print(abc.isdecimal())
print(abc.isidentifier())
print(abc.isspace)

#format
name='Ayla'
age = 6
print('%s 1ci sinifde oxuyur.Onun %s yasi var'%(name,age))
print('{} 1ci sinifde oxuyur.Onun {} yasi var'.format(name,age))







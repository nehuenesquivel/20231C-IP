--1
longitud :: [t] -> Integer
longitud [] = 0
longitud s = longitud (tail s) + 1

ultimo :: [t] -> t
ultimo [e] = e
ultimo s = ultimo (tail s)

principio :: [t] -> [t]
principio [e] = []
principio s = head s : principio (tail s)

reverso :: [t] -> [t]
reverso [] = []
reverso s = ultimo s : reverso (principio s)
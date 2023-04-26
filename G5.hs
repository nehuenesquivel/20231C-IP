--1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:t) = longitud t + 1

ultimo :: [t] -> t
ultimo [e] = e
ultimo (_:t) = ultimo t

principio :: [t] -> [t]
principio [e] = []
principio (h:t) = h : principio t

reverso :: [t] -> [t]
reverso [] = []
reverso (h:t) = reverso t ++ [h] -- = ultimo s : reverso (principio s)
-- hacer de la tercer manera o pensarla al menos (sin ++ y recursiva?)

--2
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (h:t) = e == h || pertenece e t

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales [e] = True
todosIguales (h:t) = h == head t && todosIguales t
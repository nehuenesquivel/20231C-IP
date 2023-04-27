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

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = False
todosDistintos [e] = True
todosDistintos (h:t) = auxtd h t && todosDistintos t

auxtd :: (Eq t) => t -> [t] -> Bool
auxtd _ [] = True
auxtd e (h:t) = e /= h && auxtd e t

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (h:t) = not (auxtd h t) || hayRepetidos t

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (h:t) | e == h = t
               | otherwise = h : quitar e t

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (h:t) | e == h = quitarTodos e t
                    | otherwise = h : quitarTodos e t
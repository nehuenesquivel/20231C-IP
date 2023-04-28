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

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (h:t) = h : eliminarRepetidos (quitarTodos h t)

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos s r = auxme s r && auxme r s

auxme :: (Eq t) => [t] -> [t] -> Bool
auxme [] _ = True
auxme (h:t) s = pertenece h s && auxme t s

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [e] = True
capicua (h:t) = h == ultimo t && capicua (principio t)

--3
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (h:t) = h + sumatoria t

productoria :: [Integer] -> Integer
productoria [] = 1
productoria (h:t) = h * productoria t

maximo :: [Integer] -> Integer
maximo [e] = e
maximo (h:t) | h > head t = maximo (h : tail t)
             | otherwise = maximo t

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (h:t) = h + n : sumarN n t

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero s = sumarN (head s) s

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = sumarN (ultimo s) s

pares :: [Integer] -> [Integer]
pares [] = []
pares (h:t) | mod h 2 == 0 = h : pares t
            | otherwise = pares t

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (h:t) | mod h n == 0 = h : multiplosDeN n t
                     | otherwise = multiplosDeN n t

-- ordenar :: [Integer] -> [Integer]
-- ordenar [] = []
-- ordenar (h:t) | h < head t = auxo (head s s) ++ ordenar (tail s)

-- auxo :: Integer -> [Integer] -> [Integer]
-- auxo [e] = e
-- auxo (h:t) | h < head t = auxo (h : tail t)
--            | otherwise = auxo t
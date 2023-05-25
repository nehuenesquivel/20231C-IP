main :: IO()
main = do {
  x <- readLn ;
  print(sumaMenosQueMax (x ::(Int, Int, Int)))
  }

sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax (a, b, c) = Main.max a b c > Main.min a b c + medio a b c

max :: Int -> Int -> Int -> Int
max a b c = Prelude.max (Prelude.max a b) c

min :: Int -> Int -> Int -> Int
min a b c = Prelude.min (Prelude.min a b) c

medio :: Int -> Int -> Int -> Int
medio a b c | Main.max a b c > a && Main.min a b c < a = a
            | Main.max a b c > b && Main.min a b c < b = b
            | otherwise = c
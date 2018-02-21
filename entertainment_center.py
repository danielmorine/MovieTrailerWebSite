# -*- coding: cp1252 -*-
import media
import fresh_tomatoes
"""
Sera o nomeDoFilme = media.Movie("todos os parametros"),
exemplo thor = media.Movie("todos os parametros").
    
Desta forma usaremos todos os componentes disponives em "media.py".

Colocaremos todos os filmes dentro de uma de array chamado:
    Movies = [lista de filmes]

Por fim temos a execucao do arquivo fresh_tomatoes.py
    passando nossa lista de filmes

"""
# LISTA DE FILMES
thor = media.Movie(
    "THOR RAGNAROK",
    "Thor esta preso do outro lado do universo. \
Ele precisa correr contra o tempo para voltar a Asgard e parar Ragnarok, \
a destruicaoo de seu mundo, que esta nas maos da poderosa e implacavel vila Hela.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRr9Ql3T-MXK5X_ \
x2lHdNB4lmB0XC_zFHTCtcIT6YwGbXgrNdbT",
    "https://www.youtube.com/watch?v=4yqM06buDsk",
    "Taika Waititi",
    "2h 11min",
    "Acao, Ficcao cientifica",
    "Chris Hemsworth, Tom Hiddleston, Cate Blanchett")
matrix = media.Movie(
    "MATRIX",
    "Um jovem programador e atormentado por estranhos pesadelos \
nos quais sempre esta conectado por cabos a um imenso sistema de \
computadores do futuro. A medida que o sonho se repete, ele comeca a \
levantar duvidas sobre a realidade. E quando encontra os misteriosos \
Morpheus e Trinity, ele descobre que e vitima do Matrix, um sistema \
inteligente e artificial que manipula a mente das pessoas e cria a ilusao de \
um mundo real enquanto usa os cerebros e corpos dos individuos para produzir energia.",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/c/c1/The_Matrix_Poster.jpg/200px-The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU",
    "Lana Wachowski, Lilly Wachowski",
    "2h 30min",
    "Ficcao Cientifica",
     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving")

# PASSANDO CADA FLME EM UMA LISTA DE ARRAY
movies = [thor, matrix]

# Executar arquivo e passar(movies)
fresh_tomatoes.open_movies_page(movies)

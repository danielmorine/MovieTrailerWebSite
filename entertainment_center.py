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
    "Thor esta preso do outro lado do universo. Ele precisa correr contra o tempo para voltar a Asgard e parar Ragnarok, a destruicaoo de seu mundo, que esta nas maos da poderosa e implacavel vila Hela.",  # noqa
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRr9Ql3T-MXK5X_x2lHdNB4lmB0XC_zFHTCtcIT6YwGbXgrNdbT",  # noqa
    "https://www.youtube.com/watch?v=4yqM06buDsk",
    "Taika Waititi",
    "2h 11min",
    "Acao, Ficcao cientifica",
    "Chris Hemsworth, Tom Hiddleston, Cate Blanchett")
matrix = media.Movie(
    "MATRIX",
    "Um jovem programador e atormentado por estranhos pesadelos nos quais sempre esta conectado por cabos a um imenso sistema de computadores do futuro. A medida que o sonho se repete, ele comeca a \levantar duvidas sobre a realidade. E quando encontra os misteriosos Morpheus e Trinity, ele descobre que e vitima do Matrix, um sistema inteligente e artificial que manipula a mente das pessoas e cria a ilusao de um mundo real enquanto usa os cerebros e corpos dos individuos para produzir energia.",  # noqa
    "https://http2.mlstatic.com/S_14503-MLB140249183_4647-O.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU",
    "Lana Wachowski, Lilly Wachowski",
    "2h 30min",
    "Ficcao Cientifica",
    "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving")
american = media.Movie(
    "AMERICAN PIE 3",
    "Mesmo que Jim e Michelle namorem ha varios anos, ela ainda fica surpresa quando ele pede sua mao em casamento em seu restaurante favorito. Depois que ela alegremente concorda, Jim pede aos seus melhores amigos, Kevin e Paul, para ajuda-lo a ter certeza de que tudo de certo no dia do casamento. Com a aproximacao do grande dia, um problema surge quando o trio descobre que seu amigo Stifler esta na cidade.",  # noqa
    "http://images.killermovies.com/a/americanpie3/american_pie_poster.jpg",
    "https://www.youtube.com/watch?v=Wxk0b07KrbE",
    "Jesse Dylan",
    "1h 43min",
    "Romance/Comedia",
    "Alyson Hannigan, Eddie Kaye Thomas, Jason Biggs, Seann William Scott")
cidade = media.Movie(
    "CIDADE DE DEUS",
    "Nas favelas do Rio de Janeiro dos anos 1970, dois rapazes seguem caminhos diferentes. Buscape e um fotografo que registra o cotidiano violento do lugar, e Ze Pequeno e um ambicioso traficante que usa as fotos de Buscape para provar como e durao.",  # noqa
    "https://acasadevidro.files.wordpress.com/2015/07/cidade-de-deus.png",
    "https://www.youtube.com/watch?v=pUt-yPxOZqk",
    "Fernando Meirelles, Katia Lund",
    "2h 15min",
    "Drama/Filme Policial",
    "Alexandre Rodrigues, Leandro Firmino, Phellipe Haagensen")

# PASSANDO CADA FLME EM UMA LISTA DE ARRAY
movies = [thor, matrix, american, cidade]

# Executar arquivo e passar(movies)
fresh_tomatoes.open_movies_page(movies)

import webbrowser


class Movie():
    """
        Classe responsavel por instanciar os componentes:
        movie_title = titulo do filme, movie_storyline = sinopse,
        poster_image = poster do filme, movie_direcao = diretor do filme,
        movie_classificacao = classificacao do filme,
        movie_duracao = duracao do filme,
        movie_genero = genero do filme, movie_elenco = elenco do filme

        Estes componentes serao utilzados no ""entertainment_center.py"
    """
    def __init__(
        self, movie_title, movie_storyline,
        poster_image, trailer_youtube,
        movie_direcao, movie_duracao,
        movie_genero, movie_elenco,
     ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.direcao = movie_direcao
        self.duracao = movie_duracao
        self.genero = movie_genero
        self.elenco = movie_elenco


def show_trailer(self):
    # Funcao que abrir o video do youtube
    webbrowser.open(self.trailer_youtube_url)

print(Movie.__doc__)

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
       self._likes += 1
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa):
     def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

     def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    @property
    def tamanho(self):
        return len(self._programas)
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmep = Filme ('Todo mundo em panico', 1999, 100)
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie('Demolidor', 2016, 2)
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana:
    print(programa)
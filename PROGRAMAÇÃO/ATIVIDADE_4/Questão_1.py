class livro:
    def __init__(self):
        self.titulo = "A menina que roubava livros"
        self.autor = "Não me lembro"
        self.ano_publicacao = "1999?"
    def detalhes(self):
        print(self.titulo, self.autor, self.ano_publicacao)
li = livro()

li.detalhes()
        

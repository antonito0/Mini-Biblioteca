class libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo 
        
    @property
    def autor(self):
        return self._autor 
    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor   
        
    @property
    def isbn(self):     
        return self._isbn
    @isbn.setter    
    def isbn(self, nuevo_isbn):
        self._isbn = nuevo_isbn 
        

    def __str__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, isbn={self.isbn})"
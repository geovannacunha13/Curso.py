class Curso:
    def __init__(self, id, titulo, aulas, horas, dia):
        self.id = id
        self.titulo = titulo
        self.aulas = aulas
        self.horas = horas
        self.dia = dia
        self.lista_cursos = []

    def get_curso(self):
        return self.lista_cursos

    def get_curso_id(self, id):
        for curso in self.lista_cursos:
            if curso['id'] == id:
                return curso
        return None

    def post_curso(self, curso):
        self.lista_cursos.append(curso)
        return "Curso cadastrado com sucesso."

    def put_curso(self, id, novo_curso):
        for i, curso in enumerate(self.lista_cursos):
            if curso['id'] == id:
                self.lista_cursos[i] = novo_curso
                return "Curso atualizado com sucesso."
        return "Curso não encontrado."

    def delete_curso(self, id):
        for i, curso in enumerate(self.lista_cursos):
            if curso['id'] == id:
                del self.lista_cursos[i]
                return "Curso excluído com sucesso."
        return "Curso não encontrado."


curso1 = Curso(1, "Curso de Python", 10, 20, "Segunda-feira")
curso2 = Curso(2, "Curso de JavaScript", 15, 30, "Terça-feira")

curso1.post_curso(curso1.__dict__)
curso1.post_curso(curso2.__dict__)

print(curso1.get_curso())
print(curso1.get_curso_id(1))
print(curso1.get_curso_id(3))
curso1.put_curso(1, {"id": 1, "titulo": "Curso de Python Avançado", "aulas": 12, "horas": 24, "dia": "Quarta-feira"})
print(curso1.get_curso())
curso1.delete_curso(2)
print(curso1.get_curso())







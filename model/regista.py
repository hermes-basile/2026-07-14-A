from dataclasses import dataclass, field


@dataclass
class Regista:
    id : str
    name : str
    height : int
    date_of_birth : str
    known_for_movies : str
    lista_film: list = field(default_factory=list)



    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.id == other.id

    def calcola_tot_income(self):
        incasso_tot = 0
        for dizionario_film in self.lista_film:
            if dizionario_film["worlwide_gross_income"] is not None:
                incasso = float(dizionario_film["worlwide_gross_income"].replace("$", "").strip())
                incasso_tot += incasso
        return incasso_tot
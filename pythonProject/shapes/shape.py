class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Jméno tohoto tvaru je {self.name}. Není dále klasifikován."

    def calculate_area(self):
        return f"""Tato funkce slouží k výpočtu obsahu tvarů. Tvar {self.name} nemá výpočet nadefinován.
Zkuste prosím některý z následujících tvarů: Kruh, Obdélník, Pravoúhlý trojůhelník nebo Lichoběžník.
"""


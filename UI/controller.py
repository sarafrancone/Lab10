import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.year = None
        self.country = None


    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self.year = self._view._txtAnno.value
        if self.checkAnno(self.year) == True:
            self._model.buildGrafo(self.year)
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
            num = 0
            for a in self._model.get_num_compConn():
                num += 1
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {num} componenti connesse."))
            for nodo in self._model.grafo.nodes:
                num_confinanti = len(list(self._model.grafo.neighbors(nodo)))
                #self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(nCompConn)} componenti connesse."))
                self._view._txt_result.controls.append(ft.Text(f"{nodo.StateNme} -- {num_confinanti} vicini."))

        self._view.update_page()

    def handleStatiRaggiungibili(self, e):
        vicini = self._model.getBFSNodes(self.country)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Lista di tutti i nodi raggiungibili nel grafo partendo da {self.country}: "))
        for v in vicini:
            self._view._txt_result.controls.append(ft.Text(v.StateNme))
        self._view.update_page()


    def checkAnno(self, year):
        try:
            intYear = int(year)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un anno."))
            self._view.update_page()
            return False

        if (intYear>=1816) and (intYear<=2016):
            return True
        else:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("L'anno scelto non è presente nel database."))
            return False
    def fillDdCountry(self):
        countries = self._model.getCountries()
        for c in countries:
            self._view._ddCountry.options.append(ft.dropdown.Option(text=c.StateNme, data = c, on_click=self.read_country))
        self._view.update_page()

    def read_country(self, e):
        if e.control.data is None:
            self.country = None
        else:
            self.country = e.control.data




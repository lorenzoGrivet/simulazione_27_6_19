import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the datag
        self.model = model
        self.selectedRuolo=None


    def fillDDRuolo(self):
        self.view.ddRuolo.options.clear()
        ruoli=self.model.getRuoli()
        ruoliDD=list(map(lambda x: ft.dropdown.Option(key=x,on_click=self.getSelectedRuolo),ruoli))
        self.view.ddRuolo.options=ruoliDD
        self.view.update_page()

    def handleCreaGrafo(self,e):
        self.view.txtResult.clean()
        if self.selectedRuolo is None:
            self.view.create_alert("Scegli ruolo")
        self.model.creaGrafo(self.selectedRuolo)
        n,a= self.model.getDetails()
        self.view.txtResult.controls.append(ft.Text(f"Nodi: {n}. Archi: {a}"))
        self.view.update_page()
        pass

    def handleAnalisi(self,e):
        for a in self.model.getConnessi():
            self.view.txtResult.controls.append(ft.Text(f"{a[0]} - {a[1]}: peso: {a[2]["peso"]}"))
        self.view.update_page()
        pass

    def handlePercorso(self,e):
        id=self.view.txtArtista.value
        if id=="":
            self.view.create_alert("Inserire id")
            return
        try:
            intId= int(id)
        except ValueError:
            self.view.create_alert("Non numerico")
            return

        if not self.model.controllaId(intId):
            self.view.create_alert("Non c'è")
            return

        self.model.cammino(intId)
        pass



    def getSelectedRuolo(self,e):
        if e.control.key is None:
            pass
        else:
            self.selectedRuolo=e.control.key
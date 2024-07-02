import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        self.ddCategoria=ft.Dropdown(label="Categoria reato")
        self.btnAnalisi=ft.ElevatedButton(text="Analisi Distretti",on_click=self._controller.handleAnalisi)
        row1=ft.Row([ft.Container(self.ddCategoria,width=300),ft.Container(self.btnAnalisi,width=200)],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        self.ddAnno=ft.Dropdown(label="Anno")
        row2 = ft.Row([ft.Container(self.ddAnno, width=300)],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)

        self.ddArco=ft.Dropdown(label="Arco")
        self.btnPercorso=ft.ElevatedButton(text="Calcola Percorso",on_click=self._controller.handlePercorso)
        row3=ft.Row([ft.Container(self.ddArco,width=300),ft.Container(self.btnPercorso,width=200)],alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)

        self.txtResult=ft.ListView(expand=1,auto_scroll=True)
        self._page.add(self.txtResult)

        self.update_page()


        pass

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

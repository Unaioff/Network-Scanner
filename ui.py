import customtkinter as ctk


# ===================== [ TOOLBAR ] =====================
class ToolBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Entry
        self.search_entry = ctk.CTkEntry(self,placeholder_text="Ejemplo: 192.168.0.0")
        self.search_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        # Botón Scan
        self.search_button = ctk.CTkButton(self, text="B", width=40, height=40)
        self.search_button.grid(row=0, column=1, padx=(0, 10))

        # Botón settings
        self.settings_button = ctk.CTkButton(self, text="S", width=40, height=40)
        self.settings_button.grid(row=0, column=2)

        # Configuración de columnas dentro del frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)


# ===================== [ MAP SECTION ] =====================
class MapSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.NodoCanvas = ctk.CTkCanvas(self, bg="#2b2b2b", highlightthickness=0)
        self.NodoCanvas.grid(row=0, column=0, sticky="nsew")

        self.NodoCanvas.create_oval(50, 50, 100, 100, fill="#4a90e2", outline="")
        self.NodoCanvas.create_text(75, 75, text="Nodo 1", fill="white", font=("Arial", 12, "bold"))

        self.scale = 1.0

        self.NodoCanvas.bind("<MouseWheel>", self.Zoom) 

    def Zoom(self, event):
        factor = 1.1 if event.delta > 0 else 0.9

        self.NodoCanvas.scale("all", event.x, event.y, factor, factor)
        self.NodoCanvas.configure(scrollregion=self.NodoCanvas.bbox("all"))


    def ApplyZoom(self):
        self.NodoCanvas.scale("all", 0, 0, self.scale, self.scale)

            


        

# ===================== [ INFO SECTION ] =====================
class InfoSection(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Ejemplo de contenido
        self.label = ctk.CTkLabel(self, text="INFO / PUERTOS")
        self.label.grid(row=0, column=0)


# ===================== [ APP PRINCIPAL ] =====================
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Network-Scanner")
        self.geometry("1200x628")

        # Layout principal
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        
        self.toolbar = ToolBar(self)
        self.toolbar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


        self.map_section = MapSection(self)
        self.map_section.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        self.info_section = InfoSection(self)
        self.info_section.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    def run(self):
        self.mainloop()


# ===================== [ EJECUCIÓN ] =====================
if __name__ == "__main__":
    app = App()
    app.run()
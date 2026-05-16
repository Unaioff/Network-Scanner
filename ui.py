import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Network-Scanner")
        self.geometry("1200x628")


        self.rowconfigure(0, weight=0)   
        self.rowconfigure(1, weight=1)   
        self.columnconfigure(0, weight=3)  
        self.columnconfigure(1, weight=1)  

        #  - [ CTK WIDGETS ] -


        #=======[ SEARCH ENTRY - IP HOST DESCOVERY ]=======
        self.SearchEntry = customtkinter.CTkEntry( self, placeholder_text="Ejemplo: 192.168.0.0")
        self.SearchEntry.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="ew")



        #=======[ MAP FRAME - MAPA DE NODOS ]=======

        self.MapFrame = customtkinter.CTkFrame(self)
        self.MapFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Contenido del Map Frame escalable
        self.MapFrame.rowconfigure(0, weight=1)
        self.MapFrame.columnconfigure(0, weight=1)



        #=======[ INFO FRAME - ESCANEO DE PUERTOS ]=======

        self.InfoFrame = customtkinter.CTkScrollableFrame(self)
        self.InfoFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Contenido del Info Frame escalable
        self.InfoFrame.rowconfigure(0, weight=1)
        self.InfoFrame.columnconfigure(0, weight=1)



    def RunApp(self):
        self.mainloop()





app = App()
app.RunApp()



'''
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Network-Scanner")
        self.geometry("1200x628")

        self.rowconfigure(0, weight=0)   
        self.rowconfigure(1, weight=1)   
        self.columnconfigure(0, weight=3)  
        self.columnconfigure(1, weight=1)  


    def RunApp(self):
        self.mainloop()




class NetworkMapSection(customtkinter.CTk):
    def __init__(self, master):
        super().__init__(master)

        self.MapFrame = customtkinter.CTkFrame(self)
        self.MapFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Contenido del Map Frame escalable
        self.MapFrame.rowconfigure(0, weight=1)
        self.MapFrame.columnconfigure(0, weight=1)




class ToolSection(customtkinter.CTk):
    def __init__(self, master):
        super().__init__(master)

        self.SearchEntry = customtkinter.CTkEntry( self, placeholder_text="Ejemplo: 192.168.0.0")
        self.SearchEntry.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="ew")





class InfoSection(customtkinter.CTk):
    def __init__(self, master):
        super().__init__(master)


        self.InfoFrame = customtkinter.CTkScrollableFrame(self)
        self.InfoFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Contenido del Info Frame escalable
        self.InfoFrame.rowconfigure(0, weight=1)
        self.InfoFrame.columnconfigure(0, weight=1)


app = App()
app.RunApp()
'''
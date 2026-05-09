import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Network-Scanner")
        self.geometry("1200x628")

    
       
        self.SearchEntry = customtkinter.CTkEntry(self, placeholder_text="192.168.0.0", width=800)
        self.SearchEntry.grid(row=0, column=0, padx=10, pady=10, sticky="sw")

        self.MapFrame = customtkinter.CTkFrame(master=self, width=220, height=250)
        self.MapFrame.grid(row=2,column=0,padx=0,pady=0)


        self.InfoFrame = customtkinter.CTkFrame(master=self, width=220, height=628)
        self.InfoFrame.grid(row=0,column=3,padx=0,pady=0, rowspan=3, sticky="nsew")


    def SearchEntryInput(self, entry):
        print(entry)


    def RunApp(self):
        self.mainloop()


app = App()
app.RunApp()
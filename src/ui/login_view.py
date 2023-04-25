from tkinter import ttk, StringVar, constants
from service.todo_service import TodoApp, InvalidCredentialsError, UsernameExistsError, app_service

class LoginView:
    def __init__(self, master, manage_login, manage_create_user_view):
        self.master = master
        self.manage_login = manage_login
        self.manage_create_user_view = manage_create_user_view

        self.frame = None
        self.indentification_entry = None
        self.matchword_entry = None
        self.error_variable = None
        self.error_label = None
        self.initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        self.frame.destroy()


    def login_manager(self):
        username = self.indentification_entry.get()
        password = self.matchword_entry.get()
    
        try:
            app_service.signin(username, password)
            self.manage_login()

        except InvalidCredentialsError:
            self.show_error("Invalid username or password")

    
    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def setup_username_domain(self):
        
        username_label = ttk.Label(master=self.frame, text="Username:")
        self.indentification_entry = ttk.Entry(master=self.frame, style="Custom.TEntry")
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.indentification_entry.grid(padx=5, pady=5, sticky=constants.EW)

    
    def setup_password_domain(self):

        password_label = ttk.Label(master=self.frame, text="Password:")
        self.matchword_entry = ttk.Entry(master=self.frame, show="*", style="Custom.TEntry")
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.matchword_entry.grid(padx=5, pady=5, sticky=constants.EW)


    def initialize(self):
        self.frame = ttk.Frame(master=self.master)
        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame,
            textvariable=self.error_variable,
            foreground="red")

        self.error_label.grid(padx=5, pady=5)

        self.setup_username_domain()
        self.setup_password_domain()

        login_button = ttk.Button(
            master=self.frame,
            text="Login",
            command=self.login_manager,
            style="Custom.TButton"
        )

        create_user_button = ttk.Button(
            master=self.frame,
            text="Create new user",
            command=self.manage_create_user_view,
            style="Custom.TButton"
        )

        self.frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.hide_error()

        
        self.master.style = ttk.Style(self.master)
        self.master.style.theme_use('clam')

        self.master.style.configure('Custom.TButton', 
                                    background='#FFC107', 
                                    foreground='black',
                                    padding=10, 
                                    font=('Helvetica'))
       

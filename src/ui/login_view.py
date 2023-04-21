import tkinter as tk
from service.todo_service import TodoApp

class LoginView:
    def __init__(self, master, manage_login, manage_create_user_view):
        self.master = master
        self.manage_login = login
        self.manage_create_user_view = create_user_view

        self.frame = None
        self.indentification_entry = None
        self.matchword_entry = None
        self.error_variable = None
        self.error_label = None

        self._initialize()


    def pack(self):
        self.frame.pack(fill=constants.X)

    def dismantle(self):
        self.frame.destroy()


    def login_manager(self):
        username = self.indentification_entry.get()
        password = self.matchword_entry.get()
    
        try:
            TodoApp.signin(username, password)
            self.manage_login()

        except InvalidCredentialsError:
            self.show_error("Invalid username or password")

    
    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def setup_username_domain(self):

        self.username_label = tk.Label(master = self.frame, text="Username:")
        self.indentification_entry = ttk.Entry(master=self.frame)
        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self.indentification_entry.grid(padx=5, pady=5, sticky=constants.EW)

    
    def setup_password_domain(self):

        self.password_label = tk.Label(master = self.frame, text="Password:")
        self.matchword_entry = ttk.Entry(master=self.frame)
        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self.matchword_entry.grid(padx=5, pady=5, sticky=constants.EW)


    def _initialize(self):
        self.frame = ttk.Frame(master=self.master)
        self.error_variable = StringVar(self._frame)
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
            command=self.login_manager
        )

        create_user_button = ttk.Button(
            master=self.frame,
            text="Create new user",
            command=self.manage_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
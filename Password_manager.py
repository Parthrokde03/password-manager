import tkinter as tk
from tkinter import messagebox
import os
import json
import random
import string

user_file =r"C:\Users\shiva\Desktop\VS code\Python\Learning Python\password-manager\Passwords.json"

# Ensure the folder exists
os.makedirs(os.path.dirname(user_file), exist_ok=True)


def generatePassword():
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    
def savePassword():
    website = website_entry.get().strip()
    username = userEmail_entry.get().strip()
    password = password_entry.get().strip()
    
    if not website or not username or not password:
        messagebox.showerror("Error","please fill all fields.")
        return    

    new_data = {
        website:{
            "username" : username,
            "password" : password
        }
    }
    
    try:
        with open(user_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
        
    data.update(new_data)
    
    with open(user_file, 'w') as file:
        json.dump(data, file, indent=4)
        
    website_entry.delete(0,tk.END)
    userEmail_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    messagebox.showinfo("Saved",f"Credentials for {website} are saved successfully!")     
           
# GUI
root = tk.Tk()
root.title("Password Manager")
root.geometry("400x300")
root.resizable(False,False)

# GUI Labels
tk.Label(root , text="Website").pack(pady=(10,0))
website_entry = tk.Entry(root , width=40)
website_entry.pack()

tk.Label(root , text="Username/Email").pack(pady=(10,0))
userEmail_entry = tk.Entry(root , width=40)
userEmail_entry.pack()

tk.Label(root , text="Password").pack(pady=(10,0))
password_entry = tk.Entry(root , width=40)
password_entry.pack()

# GUI Button
tk.Button(root,text="Generate Password",command=generatePassword).pack(pady=(5))
tk.Button(root,text="Save Password",command=savePassword).pack(pady=(5))

root.mainloop()
     
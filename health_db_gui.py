import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def verify_GUI_input(input_id):
    try:
        id_integer = int(input_id)
    except ValueError:
        return False
    return id_integer


def main_window():
    """Creates and runs a GUI for the health database

    This function creates a window that allows a user to enter patient
    information for eventual upload to a health database server. Entires
    on the GUI include patient name, patient id number, blood type, and
    nearest donation center.

    """
    def cancel_cmd():
        """Closes GUI window upon click of "Cancel" button

        When the user clicks on the "Cancel" button, this function is run
        which closes the main root GUI window.

        """
        root.destroy()

    def ok_cmd():
        """Obtains data from window and prints to console

        This function runs when the user clicks on the "Ok" button. It gets
        the entered data from the interface and prints it to the console. In
        the future, this function will call other functions that upload the
        data to a server.

        """
        from health_db_client import upload_patient_data_to_server
        # Get data from interface
        entered_name = name_entry.get()
        entered_id = id_entry.get()
        entered_blood_letter = blood_letter.get()
        entered_rh_factor = rh_factor.get()
        entered_blood_type = entered_blood_letter + entered_rh_factor
        # Call other functions to do the work
        patient_number = verify_GUI_input(entered_id)
        if patient_number is False:
            status_label.configure(text="Patient ID must be an integer.")
            return
        status_string = upload_patient_data_to_server(entered_name,
                                                      patient_number,
                                                      entered_blood_type)
        # Update interface based on results
        status_label.configure(text=status_string)
    
    def image_cmd():
        filename = filedialog.askopenfilename()
        if filename == "":
            return
        pil_image_raw = Image.open(filename)
        # print(pil_image_raw.size)
        pil_image = pil_image_raw.resize((200, 200))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    # Create root/base window
    root = tk.Tk()

    root.title("Health Database")
    root.geometry("800x400")

    ttk.Label(root, text="Blood Donor Database")\
        .grid(column=0, row=0, columnspan=2, sticky=tk.W)

    # Patient Name Entry
    ttk.Label(root, text="Name:").grid(column=0, row=1, sticky=tk.E)
    name_entry = tk.StringVar()
    name_entry.set("Enter a name here")
    ttk.Entry(root, width=40, textvariable=name_entry)\
        .grid(column=1, row=1, columnspan=2, sticky=tk.W)

    # Patient ID Entry
    ttk.Label(root, text="ID:").grid(column=0, row=2, sticky=tk.E)
    id_entry = tk.StringVar()
    id_entry.set("Enter your id here")
    ttk.Entry(root, width=40, textvariable=id_entry)\
        .grid(column=1, row=2, columnspan=2, sticky=tk.W)

    # Blood Letter Entry
    blood_letter = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter, value="A")\
        .grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter, value="B")\
        .grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter, value="AB")\
        .grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter, value="O")\
        .grid(column=0, row=6, sticky=tk.W)

    # Blood Rh Factor Entry
    rh_factor = tk.StringVar()
    rh_factor.set("+")
    ttk.Checkbutton(root, text="Rh Positive", variable=rh_factor,
                    onvalue="+", offvalue="-").grid(column=1, row=4)

    # Nearest Donation Center Entry
    ttk.Label(root, text="Nearest Donaiton Center").grid(column=3, row=0)
    donor_center = tk.StringVar()
    center_dropdown = ttk.Combobox(root, textvariable=donor_center)
    center_dropdown.grid(column=3, row=1)
    center_dropdown["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    center_dropdown.state(["readonly"])

    # Status indicator
    status_label = ttk.Label(root, text="Status")
    status_label.grid(column=0, row=20)

    # Image
    pil_image_raw = Image.open("DukeHealth.jpg")
    pil_image = pil_image_raw.resize((200, 100))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=4, row=0, rowspan=5)

    # Buttons
    ttk.Button(root, text="Ok", command=ok_cmd).grid(column=1, row=20)
    ttk.Button(root, text="Cancel", command=cancel_cmd).grid(column=2, row=20)
    ttk.Button(root, text="Change Image", command=image_cmd)\
        .grid(column = 3, row = 20)

    # Start GUI
    root.after(2000, ok_cmd)
    root.mainloop()


if __name__ == "__main__":
    main_window()

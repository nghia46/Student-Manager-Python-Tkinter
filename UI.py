import tkinter as tk
from tkinter import ttk
from main import Student

def load_data():
    # Clear the table before loading new data
    for row in tree.get_children():
        tree.delete(row)

    # Insert header for the table
    tree.heading("#1", text="ID")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Age")
    tree.heading("#4", text="GPA")
    
    # Retrieve student data and insert into the table
    for student in Student.get_all_students():
        tree.insert("", tk.END, text=student.id, values=(student.id, student.name, student.age, student.gpa))

def delete_student():
    selected_student = tree.selection()
    if selected_student:
        student_id = tree.item(selected_student)["values"][0]
        if Student.delete(student_id):
            tree.delete(selected_student) 
            load_data()  # Reload the data after deletion

def search_student():
    
    # Retrieve the search query
    search = search_entry.get()
    # If search query is empty, reload all data
    if not search:
        load_data()
        return
    # Search for students with matching IDs
    search_results = Student.get_student_by_id(search)
    if not search_results:
        # If no matching data found, display a message or handle as needed
        load_data()
        print("No matching data found.")
        return
    # Clean the data first
    for row in tree.get_children():
        tree.delete(row)
     # Search for students with matching IDs
    for student in search_results:
        tree.insert("", tk.END, text=student.id, values=(student.id, student.name, student.age, student.gpa))

def add_student_window():
    def clearStudentEntry():
        name_entry.delete(0,tk.END)
        age_entry.delete(0,tk.END)
        gpa_entry.delete(0,tk.END)
    # Function to add the student
    def add_student():
        # Get data from entry fields
        name = name_entry.get()
        age = age_entry.get()
        gpa = gpa_entry.get()

        if Student.add_new_student(name,age,gpa):
            clearStudentEntry()
            load_data()
    # Create a new window for adding a student
    add_window = tk.Toplevel(root)
    add_window.title("Add New Student")

    # Calculate the coordinates to center the window
    window_width = add_window.winfo_reqwidth()
    window_height = add_window.winfo_reqheight()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))

    # Set the window size and position
    add_window.geometry(f"+{x_coordinate}+{y_coordinate}")

    # Add entry fields for student data
    name_label = tk.Label(add_window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)

    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    age_label = tk.Label(add_window, text="Age:")
    age_label.grid(row=1, column=0, padx=10, pady=10)
    
    age_entry = tk.Entry(add_window)
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gpa_label = tk.Label(add_window, text="GPA:")
    gpa_label.grid(row=2, column=0, padx=10, pady=10)

    gpa_entry = tk.Entry(add_window)
    gpa_entry.grid(row=2, column=1, padx=10, pady=10)
        
    submit_btn = tk.Button(add_window,text="Submit",command=add_student)
    submit_btn.grid(row=3,column=0,padx=10,pady=10)

def update_student_window():
    def update_student():
        # Get data from entry fields
        name = name_entry.get()
        age = age_entry.get()
        gpa = gpa_entry.get()
        id = id_entry.get()
        if Student.update(id, name, age, gpa):
            update_window.destroy()
            load_data();
    update_window = tk.Toplevel(root)
    #Set title for the update window
    update_window.title("Update Student")

    # Calculate the coordinates to center the window
    window_width = update_window.winfo_reqwidth()
    window_height = update_window.winfo_reqheight()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))

    # Set the window size and position
    update_window.geometry(f"+{x_coordinate}+{y_coordinate}")
    # Add entry fields for update student data
    id_label = tk.Label(update_window, text="Id:")
    id_label.grid(row=0, column=0, padx=10, pady=10)

    id_entry = tk.Entry(update_window)
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    name_label = tk.Label(update_window, text="Name:")
    name_label.grid(row=1, column=0, padx=10, pady=10)

    name_entry = tk.Entry(update_window)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    age_label = tk.Label(update_window, text="Age:")
    age_label.grid(row=2, column=0, padx=10, pady=10)
    
    age_entry = tk.Entry(update_window)
    age_entry.grid(row=2, column=1, padx=10, pady=10)

    gpa_label = tk.Label(update_window, text="GPA:")
    gpa_label.grid(row=3, column=0, padx=10, pady=10)

    gpa_entry = tk.Entry(update_window)
    gpa_entry.grid(row=3, column=1, padx=10, pady=10)
        
    submit_btn = tk.Button(update_window,text="Submit",command=update_student)
    submit_btn.grid(row=4,column=0,padx=10,pady=10)

    def loadStudentSelectdFromTreeToEntry():
        selected_student = tree.selection();
        if(selected_student):
            student_id = tree.item(selected_student)["values"][0]
            student_name = tree.item(selected_student)["values"][1]
            student_age = tree.item(selected_student)["values"][2]
            student_gpa = tree.item(selected_student)["values"][3]
            
            # Set Selected tree StudentID and set Id Entry to readonly
            id_entry.config(state='normal')
            id_entry.delete(0, tk.END)  # Clear any existing text
            id_entry.insert(0, student_id)
            id_entry.config(state='readonly')

            # Same with name entry
            name_entry.insert(0,student_name)

            # And age entry
            age_entry.insert(0,student_age)

            # Gpa entry
            gpa_entry.insert(0,student_gpa)
    
    loadStudentSelectdFromTreeToEntry();

root = tk.Tk()
root.title("Student Manager")

# Calculate the coordinates to center the manager window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width/4) - (window_width/4))
y_coordinate = int((screen_height/4) - (window_height/4))

# Set the window size and position
root.geometry(f"+{x_coordinate}+{y_coordinate}")

# Create Search bar
search_lable = tk.Label(root,text="Search:")
search_lable.grid(row=0,column=0,padx=10,pady=10,sticky='w')

search_entry = tk.Entry(root,width=50)
search_entry.grid(row=0,column=0,padx=(70,0),pady=10,sticky='w')

search_btn = tk.Button(root,text="Search",command=search_student)
search_btn.grid(row=0,column=0,padx=10,pady=10)

# Create Treeview widget
tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "GPA"), show="headings")
tree.grid(row=1,column=0,padx=10, pady=10)

# Set header for the ID column
tree.heading("#0", text="ID")
# Button to open the window for adding a new student
add_button = tk.Button(root, text="Add New Student", command=add_student_window)
add_button.grid(row=2, column=0, padx=(10,0), pady=0, columnspan=3, sticky='w') 
# Button to open the window for updating a student
update_button = tk.Button(root, text="Update Student", command=update_student_window)
update_button.grid(row=2, column=0, padx=(120,0), pady=10, columnspan=3, sticky='w')
# Button to open the window for Delete a student
delete_btn = tk.Button(root, text="Delete", command=delete_student)
delete_btn.grid(row=2, column=0, padx=(220,0), pady=10, columnspan=3, sticky='w') 

# Load data initially
load_data()

root.mainloop()

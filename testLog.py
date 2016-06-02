from rwbatools import gui

# function called by pressing the buttons
def press(btn):
    if btn=="Cancel":
        app.stop()
    else:
        print("User:", app.getEntry('user'), "Pass:", app.getEntry('pass'))
        app.setStatus(app.getEntry("user"))

app = gui("Login Window", "400x200")
app.setBg("brown")
app.setFont(20)

app.addLabel("title", "Welcome to RWBAtools", 0, 0, 2)  # Row 0, Column 0, Span 2
app.addLabel("user", "Username:", 1, 0)                 # Row 1, Column 0, no span
app.addEntry("user", 1, 1)                              # Row 1, Column 1, no span
app.addLabel("pass", "Password:", 2, 0)                 # Row 2, Column 0, no span
app.addSecretEntry("pass", 2, 1)                        # Row 2, Column 1, no span
app.addButtons(["Submit", "Cancel"], press, 3, 0, 2)    # Row 3, Column 0, Span 2

app.setEntryFocus("user")
#app.addStatus()
#app.setStatusBg("green")
#app.setStatusFg("blue")

app.go()

"""Used to measure minimum pyinstaller size w/ tkinter"""
from tkinter import Tk

def main():
    """Main"""
    window = Tk()
    window.title("Hello World")
    window.mainloop()

if __name__ == '__main__':
    main()

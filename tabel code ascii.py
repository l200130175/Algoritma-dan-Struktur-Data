from Tkinter import *
import ttk
 
# judul dan isi tabel
judul_kolom = ("Code (decimal)", "Character")
data_ascii = [
        (0, 'NULL'),
        (1, 'SOH (start of heading'),
        (2, 'STX (start of text)'),
        (3, 'ETX (end of text)'),
        (4, 'EOT (end of transmission)'),
        (5, 'ENQ (enquiry)'),
        (6, 'ACK (acknowledge)'),
        (7, 'BEL (bell)'),
        (8, 'BS (backspace)'),
        (9, 'TAB (horizontal tab)'),
        (10, 'LF (NL line feed, new line)'),
        (11, 'VT (vertical tab)'),
        (12, 'FF (NP from feed, new page)'),
        (13, 'CR (carriage return)'),
        (14, 'SO (shift out)'),
        (15, 'SI (shift in)'),
        (16, 'DLE (data link escape)'),
        (17, 'DC1 (device control 1)'),
        (18, 'DC2 (device control 2)'),
        (19, 'DC3 (device control 3)'),
        (20, 'DC4 (device control 4)'),
        (21, 'NAK (negative acknowledge)'),
        (22, 'SYN (synchronus idle)'),
        (23, 'ETB (end of trans. block)'),
        (24, 'CAN (cancle)'),
        (25, 'EM (end of medium)'),
        (26, 'SUB (substitute)'),
        (27, 'ESC (escape)'),
        (28, 'FS (file separator)'),
        (29, 'GS (group separator)'),
        (30, 'RS (record separator)'),
        (31, 'US (unit separator)'),
        (32, 'Space'),
        (33, '!'),
        (34, '"'),
        (35, '#'),
        (36, 'Dolar'),
        (37, '%'),
        (38, '&'),
        (39, 'Petik Satu'),
        (40, '('),
        (41, ')'),
        (42, '*'),
        (43, '+'),
        (44, ','),
        (45, '-'),
        (46, '.'),
        (47, '/'),
        (48, '0'),
        (49, '1'),
        (50, '2'),
        (51, '3'),
        (52, '4'),
        (53, '5'),
        (54, '6'),
        (55, '7'),
        (56, '8'),
        (57, '9'),
        (58, ':'),
        (59, ';'),
        (60, '<'),
        (61, '='),
        (62, '>'),
        (63, '?'),
        (64, '@'),
        (65, 'A'),
        (66, 'B'),
        (67, 'C'),
        (68, 'D'),
        (69, 'E'),
        (70, 'F'),
        (71, 'G'),
        (72, 'H'),
        (73, 'I'),
        (74, 'J'),
        (75, 'K'),
        (76, 'L'),
        (77, 'M'),
        (78, 'N'),
        (79, 'O'),
        (80, 'P'),
        (81, 'Q'),
        (82, 'R'),
        (83, 'S'),
        (84, 'T'),
        (85, 'U'),
        (86, 'V'),
        (87, 'W'),
        (88, 'X'),
        (89, 'Y'),
        (90, 'Z'),
        (91, '['),
        (92, 'Back Slash'),
        (93, ']'),
        (94, '^'),
        (95, '_'),
        (96, '`'),
        (97, 'a'),
        (98, 'b'),
        (99, 'c'),
        (100, 'd'),
        (101, 'e'),
        (102, 'f'),
        (103, 'g'),
        (104, 'h'),
        (105, 'i'),
        (106, 'j'),
        (107, 'k'),
        (108, 'l'),
        (109, 'm'),
        (110, 'n'),
        (111, 'o'),
        (112, 'p'),
        (113, 'q'),
        (114, 'r'),
        (115, 's'),
        (116, 't'),
        (117, 'u'),
        (118, 'v'),
        (119, 'w'),
        (120, 'x'),
        (121, 'y'),
        (122, 'z'),
        (123, '{'),
        (124, '|'),
        (125, '}'),
        (126, '~'),
        (127, 'DEL')
        
        ]
 
 
class DemoTabel:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)
         
        self.aturKomponen()
        self.isiTabel()
         
    def aturKomponen(self):
        # buat frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        # buat frame untuk tabel beserta scrollbar-nya
        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)
         
        # buat tabel dengan Treeview
        self.trvTabel = ttk.Treeview(fr_data, columns=judul_kolom, 
                show='headings')
         
        # buat scrollbar
        sbVer = Scrollbar(fr_data, orient='vertical', 
                command=self.trvTabel.yview)
        sbHor = Scrollbar(fr_data, orient='horizontal', 
                command=self.trvTabel.xview)
        # pasang dengan layout manager pack()       
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, fill=BOTH)
             
        # buat statusbar
        lblStatus = Label(mainFrame, 
                text='Tabel Code Ascii', bd=1, relief=SUNKEN)
        lblStatus.pack(side=BOTTOM, fill=X)
         
    def isiTabel(self):
        # isi judul tabel
        for kolom in judul_kolom:
            self.trvTabel.heading(kolom, text=kolom)
                     
        # isi data tabel
        for dat in data_ascii:
            self.trvTabel.insert('', 'end', values=dat)
         
    def Tutup(self, event=None):
        self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = DemoTabel(root, ":: Tabel Code Ascii ::")
     
    root.mainloop()

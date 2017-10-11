#****************************************** TK UNTUK LOADING ********************************************************************************
#*** loading akan beraksi , dan akan menutup window setelah sekian detik .. lalu TK data utama akan otomatis dijalankan oleh python *********
##from Tkinter import *
##import ttk
##from winsound import *
##
##window = Tk()
##
####play =  PlaySound('./suara/standby.wav', SND_FILENAME)
##
##window.overrideredirect(True) #menghapus kulit window
##window.after(6000, window.destroy)
##s = ttk.Style()
##s.theme_use('classic')
##s.configure("red.Horizontal.TProgressbar", foreground='yellow', background='black')
##pb_hd = ttk.Progressbar(window,style="red.Horizontal.TProgressbar" ,orient='vertical', mode='determinate')
##pb_hd.pack(expand=True, fill=BOTH, side=RIGHT)
##pb_hd.start(22)
##pb_hd = ttk.Progressbar(window,style="red.Horizontal.TProgressbar", orient='vertical', mode='determinate')
##pb_hd.pack(expand=True, fill=BOTH, side=LEFT)
##pb_hd.start(22)
##lebar = 700
##tinggi = 300
### ************************* penggunaan fungsi winfo_screenwidth()
##setTengahX = (window.winfo_screenwidth()-lebar)//2
### ************************* penggunaan fungsi winfo_screenheight()
##setTengahY = (window.winfo_screenheight()-tinggi)//2
##
##window.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
##
##try:
##    asd=PhotoImage(file='./gambar/Z.gif')
##    canvas = Canvas(window, width = 700, height = 300)    
##    canvas.pack(side=TOP)
##    x0 = 60
##    y0 = 140
##    x1 = 560
##    y1 = 300
##    i = 0
##    deltax = 2
##    deltay = 3
##    which = canvas.create_image(200,200,image=asd, tag='redBall')
##    
##    while True:
##        canvas.create_text(350,150,text='LOADING...',font=('stencil', 70),fill='white')
##        canvas.move('redBall', deltax, deltay)
##        canvas.after(20)
##        canvas.update()
##        if x1 >= 400:
##            deltax = -2
##        if x0 < 0:
##            deltax = 2
##        if y1 > 300:
##            deltay = -3
##        if y0 < 0:
##            deltay = 3
##        x0 += deltax
##        x1 += deltax
##        y0 += deltay
##        y1 += deltay
##except:
##    pass
##
##window.mainloop()
##    
#****************************************** TK UNTUK DATA UTAMA ********************************************************************************
from Tkinter import*
from tkMessageBox  import*
import tkMessageBox as mb
import ttk
import time
import tkColorChooser 
##from winsound import *

#****************************************** CLASS UNTUK SIMPUL *********************************************************************************

class tempat_data():
    def __init__(self,nama=None,jenisKelamin=None,jabatan=None,umur=None,
                 alamat=None,agama=None,nopegawai=None,sift=None,kendaraan=None):#,link=None):
        self.nama = nama
        self.jenisKelamin   = jenisKelamin
        self.jabatan   = jabatan
        self.umur  = umur
        self.alamat  = alamat
        self.agama  = agama
        self.nopegawai  = nopegawai
        self.sift  = sift
        self.kendaraan  = kendaraan

class simpul():
    def __init__(self, data=None):
        self.data = data
        self.link = None

#****************************************** CLASS UNTUK MEMBUAT KOMEN JIKA MOUSE BERADA DI.. ****************************************************

class CreateToolTip(object):
    """create a tooltip for a given widget"""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)

        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # create  toplevel window
        self.tw = Toplevel(self.widget)
        # window komen akan menutup jika mouse tidak berada pada sasaran
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left', background='turquoise', relief='solid', borderwidth=1,
                       font=("Century", "10", "normal"),fg='black')
        label.pack(ipadx=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
            
#****************************************** CLASS UNTUK KOMPONEN TAMPILAN AWAL PROGRAM******************************************************************

class Data(Frame):
    
##    play =  PlaySound('./suara/loading.wav', SND_FILENAME)
    
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
##        self.parent.geometry("700x400")
        self.parent.resizable(False, False)
        self.teksJam = StringVar()
        self.initUI()
     
    def initUI(self):
        self.update() #memenggil def update dan menjalankanya
        self.teksJam = StringVar()
        self.datJam_menu = time.strftime("PT.MULTINASIONAL - %A. %d %B %Y (%Z)",
                                           time.localtime())
        # atur ukuran window
        # menempatkan window di tengah layar PC/Laptop
        lebar = 700
        tinggi = 350
 
        # ************************* penggunaan fungsi winfo_screenwidth()
        setTengahX = (self.parent.winfo_screenwidth()-lebar)//2
        # ************************* penggunaan fungsi winfo_screenheight()
        setTengahY = (self.parent.winfo_screenheight()-tinggi)//2
 
        self.parent.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
        # **************************************************************** 
        
        mainFrame = Frame(self.parent,bd=3,bg='black',cursor='spraycan')
        mainFrame.pack(fill=BOTH, expand=YES)
         
        self.parent.title(self.datJam_menu)

        self.menubar = Menu(self.parent)
        self.parent.config(menu = self.menubar)

        
        self.lbl_gmbr_grk = Label(mainFrame,bg='black')
        self.lbl_gmbr_grk.pack(expand=YES)
        
        # ************************* kumpulan menubar dan filemenu()
        
        self.digaris = PhotoImage(file='./gambar kecil/menu_divider.gif')
        
        self.gmbrimpor = PhotoImage(file='./gambar kecil/GO.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = 'IMPORT',menu = fileMenu)
        fileMenu.add_command( image=self.digaris)
        fileMenu.add_command( label = 'LETS',image=self.gmbrimpor, compound='right',command=self.impor)
        fileMenu.add_command( image=self.digaris)
        
        self.til = PhotoImage(file='./gambar kecil/floppybuddy.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        fileMenu.add_separator()
        self.menubar.add_cascade(label="DATA KOSONG",  menu = fileMenu)
        fileMenu.add_command( image=self.digaris)
        fileMenu.add_command(label = 'CLASIK', image=self.til,compound='left',command=self.data1)
        fileMenu.add_command( image=self.digaris)
        fileMenu.add_separator()

        self.about = PhotoImage(file='./gambar kecil/UMS.gif')
        self.about2 = PhotoImage(file='./gambar kecil/C.gif')
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="ABOUT PROGRAM..",  menu = fileMenu)
        fileMenu.add_command(label = 'DOKUMEN RAHASIA ',image=self.about,compound='top', command=self.aboutSistem)
        fileMenu.add_command(label = 'KOMANDAN KELOMPOK 8',image=self.about2,compound='center', command=self.aboutSistem)

        # ************************* button keluar berada di kiri bawah
        self.jpgout = PhotoImage(file='./gambar kecil/close.button.gif')
        self.fr_out = Frame (mainFrame,bg='black')
        self.fr_out.pack(side=BOTTOM,fill=BOTH,expand=YES)
        self.tmbl_keluar = Button(self.fr_out,image=self.jpgout,command=self.keluar,bg='black')
        self.tmbl_keluar.pack(side=LEFT)
        self.jpgout2 = PhotoImage(file='./gambar kecil/AG00164_.gif')

        # ************************* label untuk jam()
        self.j = Label(self.fr_out,bg='black',textvariable=self.teksJam
                                 ,compound='center',fg='lavender',font=('Century', 13))
        self.j.pack(side=RIGHT)

        # ************************* untuk menggerakkan gambar()
        try:
            asd=PhotoImage(file='./gambar/2.gif')
            self.canvas = Canvas(self.lbl_gmbr_grk, width = 700, height = 300)    
            self.canvas.pack(side=TOP,expand=YES)
            x0 = 60
            y0 = 140
            x1 = 300
            y1 = 360
            i = 0
            deltax = 2
            deltay = 3
            which = self.canvas.create_image(200,200,image=asd, tag='redBall')
            
            while True:
                self.canvas.move('redBall', deltax, deltay)
                self.canvas.after(20)
                self.canvas.update()
                if x1 >= 400:
                    deltax = -2
                if x0 < 0:
                    deltax = 2
                if y1 > 300:
                    deltay = -3
                if y0 < 0:
                    deltay = 3
                x0 += deltax
                x1 += deltax
                y0 += deltay
                y1 += deltay
        except:
            pass
        
    # ************************* jika keluar maka akan muncul prosesbar seolah-olah seperti loading dan window menutup setelah sekian detik()    
    def keluar(self):
        self.parent.title('PT.MULTINASIONAL - EXIT YOUR SYSTEM')
        self.SuaraSystemKeluar()
        s = ttk.Style()
        s.theme_use('classic')
        s.configure("red.Horizontal.TProgressbar", foreground='yellow', background='darkred')
        pb_hd = ttk.Progressbar(self.fr_out,style="red.Horizontal.TProgressbar" ,orient='horizontal', mode='indeterminate')
        pb_hd.pack(expand=True, fill=BOTH, side=RIGHT)
        pb_hd.start(20)
        root.after(5000, root.destroy)  #menutup window setelah 3 detik
        self.tmbl_keluar.configure(image=self.jpgout2)

        self.canvas.create_text(350,150,text='TERIMAKASIH'+'\n       TELAH'+'\nBERKUNJUNG',
                                font=('stencil', 30),fill='white')
        
    def SuaraSystemKeluar(self,Event=None):
        play =  PlaySound('./suara/Thank You.wav', SND_FILENAME)
        
    # ************************* jam update menurut waktu lokal pc()   
    def update(self):
        # strftime() berfungsi untuk merubah data waktu secara lokal
        # menjadi bentuk string yang kita inginkan.
        datJam = time.strftime("%H : %M : %S %p " ,
                               time.localtime())

        # mengubah teks jam sesuai dengan waktu saat ini
        self.teksJam.set(datJam)
        
        # perubahan teks jam dalam selang waktu 1 detik (1000 ms)
        self.timer = self.parent.after(1000, self.update)

    # ************************* sound about hello()   
    def aboutSistem(self,Event=None):
        play =  PlaySound('./suara/x.about-musik kelompok 8.wav', SND_FILENAME)
        play =  PlaySound('./suara/x.about-sapa hallo.wav', SND_FILENAME)
        play =  PlaySound('./suara/x.about-musik kelompok 8.wav', SND_FILENAME)
           
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#****************************************** FUNGSI IMPORT DATA ******************************************************************
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    def impor(self):
        try:
            #******************************untuk**data**atas*********************************************************************************            
            import tkFileDialog as TD
            self.File = TD.askopenfilename()
            x=open(self.File)
            x.readline()
            baca=x.readlines()

            self.list = simpul() #self list hanya fariable !
            p=self.list 
    
            for k in range(len(baca)):
                z=baca[k].split(',')
                L=tempat_data(z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8])
                p.link=simpul(L)
                p=p.link
            x.close()

            #****************************** dimasukan ke data_hrd_A (kosong) untuk data atas *********************************************************************************            
            p=self.list
            self.data_hrd_A = []

            while p.link is not None:
                data=(p.link.data.nama, p.link.data.jenisKelamin, p.link.data.jabatan,
                      p.link.data.umur, p.link.data.alamat, p.link.data.agama,
                      p.link.data.nopegawai, p.link.data.sift, p.link.data.kendaraan.rstrip('\n'))
                self.data_hrd_A.append(data)
                p=p.link

            #******************************untuk**data**bawah********************************************************************************            
            y=open(self.File)
            baca=y.readlines()

            self.list1 = simpul() #self list1 hanya fariable !
            p1=self.list1 
    
            for k in range(len(baca)):
                z=baca[k].split(',')
                L=tempat_data(z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8])
                p1.link=simpul(L)
                p1=p1.link
            y.close()

            #******************************dimasukan ke data_hrd_B (kosong) untuk data atas*****************************************************            
            p1=self.list1
            self.data_hrd_B =[]

            while p1.link is not None:
                data=(p1.link.data.nama, p1.link.data.jenisKelamin,
                      p1.link.data.umur, p1.link.data.alamat, p1.link.data.agama,
                      p1.link.data.nopegawai, p1.link.data.sift)
                self.data_hrd_B.append(data)
                p1=p1.link
                
        #****************************** jika impor berhasil *****************************************************                
            self.menubar.entryconfig(2,label= 'TAMPILKAN DATA')

            self.suksesimpor = PhotoImage(file='./gambar kecil/thumbup.gif')
            self.lbl_gmbr_grk.configure(image=self.suksesimpor)
##            self.SuaraImporSukses()
            self.yeah = PhotoImage(file='./gambar/t.gif')
            self.canvas.delete(ALL)
            self.canvas.create_image(350,200,image=self.yeah, tag='redBall')
            self.parent.title('PT.MULTINASIONAL - IMPORT BERHASIL !!!')

            self.error = PhotoImage(file='./gambar kecil/close.button.gif')
            self.tmbl_keluar.configure(image=self.error)

        #****************************** jika impor cancel ***************************************************** 
        except IOError :
            self.cancelimpor = PhotoImage(file='./gambar kecil/closeButtonS.gif')
            self.lbl_gmbr_grk.configure(image=self.cancelimpor)
##            self.SuaraImporCancel()
            self.yeah = PhotoImage(file='./gambar/1.gif')
            self.canvas.delete(ALL)
            self.canvas.create_image(350,200,image=self.yeah, tag='redBall')
            self.parent.title('PT.MULTINASIONAL - KAU PLIN - PLAN !!!')

            self.error = PhotoImage(file='./gambar kecil/closeButtonS.gif')
            self.tmbl_keluar.configure(image=self.error)

        #****************************** jika impor gagal ***************************************************** 
        except IndexError :
            self.gagalimpor = PhotoImage(file='./gambar kecil/thumbdown.gif')
            self.lbl_gmbr_grk.configure(image=self.gagalimpor)
##            self.SuaraImporGagal()
            self.yeah = PhotoImage(file='./gambar/Y.gif')
            self.canvas.delete(ALL)
            self.canvas.create_image(350,200,image=self.yeah, tag='redBall')
            self.parent.title('PT.MULTINASIONAL - IMPORT GAGAL !!!')

            self.error = PhotoImage(file='./gambar kecil/closeButtonS.gif')
            self.tmbl_keluar.configure(image=self.error)
            
    #****************************** kumpulan suara impor *****************************************************        
##    def SuaraImporSukses(self,Event=None):
##        play =  PlaySound('./suara/tertawa', SND_FILENAME)
##    def SuaraImporCancel(self,Event=None):
##        play =  PlaySound('./suara/ok sistem cancel.wav', SND_FILENAME)
##    def SuaraImporGagal(self,Event=None):
##        play =  PlaySound('./suara/bom', SND_FILENAME)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#****************************************** FUNGSI MENAMPILKAN DATA ******************************************************************
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
          
    def data1(self):
        try:
            data_hrd_A = self.data_hrd_A #mengambil dari import data atas
            data_hrd_B = self.data_hrd_B #mengambil dari import data bawah
            s=self.list #mengambil dari import 
            
            self.datJam_menu = time.strftime(" %A, %d %B %Y - " + self.File,
                                           time.localtime())
            
            #******************** jika sukses impor gambar akan berubah dan akan muncul suara 
            self.suksestampil = PhotoImage(file='./gambar kecil/close.button.gif')
            self.tmbl_keluar.configure(image=self.suksestampil)

            #********************* CLASS UNTUK DATA UTAMA
            
            class DemoListbox(Toplevel,Frame):
                
##                  play =  PlaySound('./suara/sistem ready.wav', SND_FILENAME)
                  
                  def __init__(self, parent, title):
                    self.parent = parent
                    Toplevel.__init__(self, parent)
                    self.title(title)
                    lebar = 726
                    tinggi = 682
                    # ************************* penggunaan fungsi winfo_screenwidth()
                    setTengahX = (parent.winfo_screenwidth()-lebar)//2
                    # ************************* penggunaan fungsi winfo_screenheight()
                    setTengahY = (parent.winfo_screenheight()-tinggi)//8

                    self.geometry("%ix%i+%i+%i" %(lebar, tinggi, setTengahX, setTengahY))
                    self.resizable(False, False)
                    self.protocol('WM_DELETE_WINDOW', self.onPass)
                    parent.protocol('WM_DELETE_WINDOW', self.onPass)
                    self.transient(parent)
                    
                    self.data_hrd_A = data_hrd_A
                    self.data_hrd_B = data_hrd_B
                
                    self.aturKomponen()
                    self.aturKejadian()
                    self.isiListbox()
                    self.isiData()
                    self.listboxData.focus_set()
                    self.flashing()
                    
                  # ************************* jika (x)close ditekan akan muncul peringatan()
                  # ************************* supaya tombol keluar efektif !
                  def onPass(self): 
                    pass
                    play =  PlaySound('./suara/comming message.wav', SND_FILENAME)
                    showwarning('PERINGATAN !','KELUAR PADA TEMPATNYA  !!!')
                
                  def aturKejadian(self):
                    '''  
                    #settingan untuk tampilan awal# ,
                    #fungsi state DISABLED adalah status tombol mati , jika NORMAL tombol aktif,
                    #fungsi cratetooltip untuk memberi komentar ketika cursor berada di jangkauan tombol,
                    #fungsi bind '<ButtonRelease-1>' ketika cursor menekan objek di "self. ...",
                    #fungsi bind '<KeyRelease>' ketika enter menekan objek di "self. ...",
                    #fungsi bind cursor efek perubahan bentuk cursor dari tkinter,
                    '''
                    self.listboxData.bind('<ButtonRelease-1>', self.onKlikLB)
                    self.listboxData.bind('<KeyRelease>', self.onKlikLB)
                    self.lbltambah.configure(state=NORMAL,bg='dark red',fg='white',
                                             text='--\nT\nA\nM\nB\nA\nH\n--',command=self.tambah,cursor='iron_cross')#status tombol tambah
                    self.lblhapus.configure(state=NORMAL,bg='black',fg='white',cursor='pirate') #status tombol hapus
                    self.lblsimpan.configure(state=DISABLED,bg='dark red',fg='white',cursor='pirate') #status tombol simpan
                    self.lblhapus_ttp = CreateToolTip(self.lblhapus, "Hapus semua data , tapi pikirlah seribu kali dahulu") #komen tombol hapus 

                    self.fr_bawah.configure(bg='dark red',fg='gold',cursor='hand2')
 
                    self.checkc.configure(state=NORMAL,bg='dark red',fg='gold',cursor='iron_cross')
                    self.checkc_ttp = CreateToolTip(self.checkc, "Cari Data Sekarang") #komen tombol tombol cari
                    self.entryc.configure(state=NORMAL,bg='tan',cursor='dot')
                    self.entryc_ttp = CreateToolTip(self.entryc, "Masukan Data yang anda cari sekarang") #komen entry cari
                    self.entryc.bind('<KeyRelease>', self.cari)
                    self.listboxData.configure(state=NORMAL,bg='gold',cursor='watch')
                    self.btnAwal.configure(state=NORMAL, bg='black', fg='gold',cursor='iron_cross')
                    self.btnPrev.configure(state=NORMAL, bg='black', fg='gold',cursor='iron_cross')
                    self.btnNext.configure(state=NORMAL, bg='black', fg='gold',cursor='iron_cross')
                    self.btnAkhir.configure(state=NORMAL, bg='black', fg='gold',cursor='iron_cross')
                    self.mainFrame.configure(bg='dark red',cursor='watch')
                    self.fr_kanan.configure(bg="dark red",cursor='watch')

                    self.fr_databawah.configure(bg='darkred',fg='gold')
                    self.lblkeluar.configure(bg='black')
                    self.lblkeluar_ttp = CreateToolTip(self.lblkeluar, "Mau Keluar Geser kekanan sekarang") #komen scale keluar

                    self.fr_ah1.configure(bg='darkred')
                    self.fr_aha.configure(bg='darkred')
                    self.fr_ahcanv.configure(bg='darkred')
                    self.fr_ahh.configure(bg='darkred')
                    self.fr_aho.configure(bg='darkred')
                    self.jam.configure(bg='darkred',fg='white')
                    
                  def onKlikLB(self, event=None):
                    self.isiData()
                    
                  def isiData(self):
                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    # hapus data
                    self.entryKosong()
               
                    # isi data
                    self.entnama.insert(END, self.data_hrd_A[kode][0])
                    self.entjenisKelamin.insert(END, self.data_hrd_A[kode][1])
                    self.entjabatan.insert(END, self.data_hrd_A[kode][2])
                    self.entumur.insert(END, self.data_hrd_A[kode][3])
                    self.entalamat.insert(END, self.data_hrd_A[kode][4])
                    self.entagama.insert(END, self.data_hrd_A[kode][5])
                    self.entnopegawai.insert(END, self.data_hrd_A[kode][6])
                    self.entsift.insert(END, self.data_hrd_A[kode][7])
                    self.entkendaraan.insert(END, self.data_hrd_A[kode][8])
               
                  def isiListbox(self):
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                                  
                  def kosongan(self):
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.delete(0,END)
                    self.listboxData.selection_set(0)
                    
                    self.entnama.delete(0, END)
                    self.entjenisKelamin.delete(0, END)
                    self.entjabatan.delete(0, END)
                    self.entumur.delete(0, END)
                    self.entalamat.delete(0, END)
                    self.entagama.delete(0, END)
                    self.entnopegawai.delete(0, END)
                    self.entsift.delete(0, END)
                    self.entkendaraan.delete(0, END)
                    
#******************************************DATA BAWAH UNTUK DIPANGGIL***********************************************************************************
#*******************************************************************************************************************************************************
                  def databawah(self):
                    self.rows = len(self.data_hrd_A)  # jumlah baris
                    self.columns = 7  # jumlah kolom
                    self._widgets = list()
                    for row in range(self.rows):
                        self.current_row = list()
                        for column in range(self.columns):
                            tampil = ''
                            label = Menubutton(self.frame, text="%s" % tampil, borderwidth=1,
                                           width=12,bg='tan',fg='darkred',font=('stencil', 9),
                                               compound='center',relief=RIDGE)
                            label.grid(row=row, column=column, sticky="nsew")
                            self.current_row.append(label)
                        self._widgets.append(self.current_row)
                    for column in range(self.columns):
                        self.grid_columnconfigure(column, weight=1)

                    # akhir bagian yang ditambahkan untuk menampilkan data
                    data_tampil = self.data_hrd_A
                    for row in range(self.rows):
                        baris = data_tampil[row]
                        for column in range(self.columns):
                            nilai = baris[column]
                            widget = self._widgets[row][column]
                            widget.configure(text=nilai)
                    
#******************************************BUBBLESORT DATA ATAS LINKLIST********************************************************************************                            
                  def bubbleSort(self,Data,indeks):
                    '''fungsi untuk mengurutkan data dengan Bubble Sort
                    input berupa list bernama Data'''
                    n = len(Data)  # n adalah jumlah data
                    if indeks == 'nama':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.nama > Data[i+1].data.nama:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]
                    elif indeks == 'jenisKelamin':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.jenisKelamin > Data[i+1].data.jenisKelamin:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]

                    elif indeks == 'umur':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.umur > Data[i+1].data.umur:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]
                    elif indeks == 'alamat':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.alamat > Data[i+1].data.alamat:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]
                    elif indeks == 'agama':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.agama > Data[i+1].data.agama:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]

                    elif indeks == 'nopegawai':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.nopegawai > Data[i+1].data.nopegawai:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]
                    elif indeks == 'sift':
                      for k in range(1,n):  # ulangi sebanyak n-1 kali
                          for i in range(n-1):   # lakukan dari posisi paling kiri hingga ke kanan
                              if Data[i].data.sift > Data[i+1].data.sift:  # bandingkan dua data yang berdekatan
                                  Data[i], Data[i+1] = Data[i+1], Data[i]

                  def bubble(self,LL,indeks):
                    '''mengurutkan linked list dengan Bubble Sort
                    Tricky: dengan mengkonversi linked menjadi array, bubble sort lalu
                    dikembalikan menjadi array'''
                    # konversi dari Linked List ke python list
                    Ar = []
                    p = LL.link
                    while p != None:
                        Ar.append(p)
                        p = p.link
                    # memanggil fungsi bubble sort
                    self.bubbleSort(Ar,indeks)
                    # konversi dari python list ke Linked List
                    p = LL
                    for simpul1 in Ar:
                        p.link = simpul1
                        simpul1.link = None
                        p = p.link
                    p=LL.link
                    self.data_hrd_A = []
                    while p is not None:
                        data=(p.data.nama, p.data.jenisKelamin, p.data.jabatan,
                               p.data.umur, p.data.alamat, p.data.agama,
                                p.data.nopegawai, p.data.sift, p.data.kendaraan.rstrip('\n'))
                        self.data_hrd_A.append(data)
                        p=p.link
                        
#******************************************BUBBLESORT DATA BAWAH *****************************************************************************************             


                  def bubblebiasa(self,x,y):
                    for nomor in range(len(x)-1,0,-1):
                        for i in range(1,nomor):
                            if x[i][y]>x[i+1][y]:
                                temp = x[i]
                                x[i] = x[i+1]
                                x[i+1] = temp
                        
                  def sortir_data_bawah(self):
                    data_tampil = self.data_hrd_B
                    for row in range(self.rows):
                        baris = data_tampil[row]
                        for column in range(self.columns):
                            nilai = baris[column]
                            widget = self._widgets[row][column]
                            widget.configure(text=nilai)
                    
#******************************************MENAMPILKAN URUT NAMA *****************************************************************************************             

                    
                  def name(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'nama')
                    self.bubblebiasa(self.data_hrd_B,0)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
                    
#******************************************BUBBLESORT URUT KELAMIN **************************************************************************************             
                  def kelamin(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'jenisKelamin')
                    self.bubblebiasa(self.data_hrd_B,1)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
                    
#******************************************BUBBLESORT URUT UMUR ******************************************************************************************             

                  def umur(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'umur')
                    self.bubblebiasa(self.data_hrd_B,2)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
                    
#******************************************BUBBLESORT URUT ALAMAT ****************************************************************************************             

                  def alamat(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'alamat')
                    self.bubblebiasa(self.data_hrd_B,3)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
                    
#******************************************BUBBLESORT URUT AGAMA ******************************************************************************************             

                  def agama(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'agama')
                    self.bubblebiasa(self.data_hrd_B,4)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
                    
#******************************************BUBBLESORT URUT ABSEN ******************************************************************************************             


                  def absen(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'nopegawai')
                    self.bubblebiasa(self.data_hrd_B,5)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()
#******************************************BUBBLESORT URUT SIFT ******************************************************************************************             
                  
                  def sift(self):
                    self.kosongan()
                    data=s
                    self.bubble(data,'sift')
                    self.bubblebiasa(self.data_hrd_B,6)
                    
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END, self.data_hrd_A[dat][0])
               
                    self.listboxData.selection_set(0)

                    indeks = self.listboxData.curselection()
                    kode = int(indeks[0])
               
                    self.isiData()
                    self.sortir_data_bawah()

#<><><><><><><><><>><<><><><><><><><><><<><><><><><><><><><><><<><><><><><><><><><><><>#               
# FUNGSI PENCARIAN                
                  def ProsesCari (self,Event=None):
                    try:
                        #**************************pencarian data atas**************************************************
                        entry = self.entryc.get().lower() #Target Cari Adalah Masukan data dari entryc 
                        dataCari = []
                        for i in self.data_hrd_A:
                            if entry in i[0].lower()\
                               or entry in i[1].lower()\
                               or entry in i[2].lower()\
                               or entry in i[3].lower()\
                               or entry in i[4].lower()\
                               or entry in i[5].lower()\
                               or entry in i[6].lower()\
                               or entry in i[7].lower()\
                               or entry in i[8].lower():
                                dataCari.append(i)
                        
                        self.kosongan()
                        self.data_hrd_A = dataCari
                        for dat in range(len(self.data_hrd_A )):
                              self.listboxData.insert(END, self.data_hrd_A [dat][0])               
                        self.listboxData.selection_set(0)
                        indeks = self.listboxData.curselection()
                        kode = int(indeks[0])
                        self.isiData()

                        #**************************pencarian data bawah*************************************************
                        
                        target = self.entryc.get().lower()
                        coba = []           
                        cek = False
                        for i in self.data_hrd_B:
                            if  target in i[0].lower()\
                               or target in i[1].lower()\
                               or target in i[2].lower()\
                               or target in i[3].lower()\
                               or target in i[4].lower()\
                               or target in i[5].lower()\
                               or target in i[6].lower():
                                coba.append(i)
                                cek=True
                        for i in self.data_hrd_B:
                            if  target not in i[0].lower()\
                               or target not in i[1].lower()\
                               or target not in i[2].lower()\
                               or target not in i[3].lower()\
                               or target not in i[4].lower()\
                               or target not in i[5].lower()\
                               or target not in i[6].lower():
                                coba.append(('?','?','?','?','?','?','?'))
                        data_tampil = coba
                        for bariske in range(len(coba)):
                            baris = data_tampil[bariske]
                            for kolomke in range(len(coba[0])):
                                nilai = baris[kolomke]
                                widget = self._widgets[bariske][kolomke]
                                widget.configure(text=nilai)
                    except:
                        pass

                  def cari (self,Event=None):
                          self.ProsesCari ()
                          
#****************************************** FUNGSI ENTRY DATA ATAS KOSONGAN *************************************************************************************             

                  def entryKosong(self):                
                    self.entnama.delete(0, END)
                    self.entjenisKelamin.delete(0, END)
                    self.entjabatan.delete(0, END)
                    self.entumur.delete(0, END)
                    self.entalamat.delete(0, END)
                    self.entagama.delete(0, END)
                    self.entnopegawai.delete(0, END)
                    self.entsift.delete(0, END)
                    self.entkendaraan.delete(0, END)
                    
#****************************************** FUNGSI TAMBAH DATA *************************************************************************************************             
                    
                  def tambah(self):
                     self.lbltambah.configure(text='\n--\nB\nA\nT\nA\nL\n--\n',bg='tan',fg='black'
                                              ,command=self.aturKejadian,cursor='watch')
                     self.lblhapus.configure(state=DISABLED,bg='tan',cursor='x_cursor')
                     self.lblhapus_ttp = CreateToolTip(self.lblhapus, "Tidak Aktif") #komen tombol hapus 

                     self.lblsimpan.configure(state=NORMAL,bg='olive',fg='black',cursor='watch')
                     self.fr_bawah.configure(bg='olive',cursor='hand1')

                     self.checkc.configure(state=DISABLED,bg='olive',cursor='x_cursor')
                     self.entryc.configure(state=DISABLED,cursor='x_cursor')
                     self.checkc_ttp = CreateToolTip(self.checkc, "Tidak Aktif") #komen tombol tombol cari
                     self.entryc_ttp = CreateToolTip(self.entryc, "Tidak Aktif") #komen entry cari

                     self.listboxData.configure(state=DISABLED,bg='tan',cursor='x_cursor')
                     self.btnAwal.configure(state=DISABLED, bg='tan',cursor='x_cursor')
                     self.btnPrev.configure(state=DISABLED, bg='olive',cursor='x_cursor')
                     self.btnNext.configure(state=DISABLED, bg='tan',cursor='x_cursor')
                     self.btnAkhir.configure(state=DISABLED, bg='olive',cursor='x_cursor')
                     self.mainFrame.configure(bg='olive',cursor='x_cursor')
                     self.fr_kanan.configure(bg="tan",cursor='x_cursor')

                     self.fr_databawah.configure(bg='olive',fg='gold')
                     self.lblkeluar.configure(bg='tan')
                     self.lblkeluar_ttp = CreateToolTip(self.lblkeluar, "Mau Keluar Geser kekanan sekarang") #komen scale keluar
                    
                     self.entryKosong()

                     self.fr_ah1.configure(bg='olive')
                     self.fr_aha.configure(bg='olive')
                     self.fr_ahcanv.configure(bg='olive')
                     self.fr_ahh.configure(bg='olive')
                     self.fr_aho.configure(bg='olive')
                     self.jam.configure(bg='olive',fg='black')
                     
#****************************************** FUNGSI JIKA MENYIMPAN GAGAL / ENTRY ADA YANG KOSONG ******************************************************************
                     
                  def simpangagal(self):
                    self.aturKejadian()
                    self.kosongan()
                    for dat in range(len(self.data_hrd_A)):
                          self.listboxData.insert(END,'LENGKAPI DATA INPUT ANDA')
                    self.lbltambah.configure(text='\n--\nB\nA\nT\nA\nL\n--\n',bg='dark red',fg='white'
                                              ,command=self.aturKejadian,cursor='icon')
                    self.lblhapus.configure(state=DISABLED,bg='white',fg='black',cursor='pirate')
                    self.lblhapus_ttp = CreateToolTip(self.lblhapus, "Warning !!!") #komen tombol hapus
                    
                    self.lblsimpan.configure(state=NORMAL,bg='dark red',fg='white',cursor='icon')
                    self.fr_bawah.configure(bg='white',fg='dark red',cursor='hand1')

                    self.checkc.configure(state=DISABLED,bg='lavender',fg='black',cursor='pirate')
                    self.entryc.configure(state=DISABLED,bg='lavender',cursor='pirate')
                    self.checkc_ttp = CreateToolTip(self.checkc, "Warning !!!") #komen tombol tombol cari
                    self.entryc_ttp = CreateToolTip(self.entryc, "Warning !!!") #komen entry cari
                    
                    self.listboxData.configure(state=DISABLED,bg='lavender',cursor='pirate')
                    self.btnAwal.configure(state=DISABLED, bg='white',fg='black',cursor='pirate')
                    self.btnPrev.configure(state=DISABLED, bg='white',fg='black',cursor='pirate')
                    self.btnNext.configure(state=DISABLED, bg='white',fg='black',cursor='pirate')
                    self.btnAkhir.configure(state=DISABLED, bg='white',fg='black',cursor='pirate')
                    self.mainFrame.configure(bg='lavender',cursor='pirate')
                    self.fr_kanan.configure(bg="lavender",cursor='pirate')

                    self.fr_databawah.configure(bg='white',fg='dark red')
                    self.lblkeluar.configure(bg='dark red')
                    self.lblkeluar_ttp = CreateToolTip(self.lblkeluar, "Mau Keluar Geser kekanan sekarang") #komen scale keluar

                    self.fr_ah1.configure(bg='lavender')
                    self.fr_aha.configure(bg='lavender')
                    self.fr_ahcanv.configure(bg='lavender')
                    self.fr_ahh.configure(bg='lavender')
                    self.fr_aho.configure(bg='lavender')
                    self.jam.configure(bg='lavender',fg='dark red')

#****************************************** FUNGSI MENYIMPAN DATA ******************************************************************************************             

                  def simpan (self,event=None):
                  #ketika tombol simpan ditekan , akan menuliskan ke csv dengan input masukan entry dari pengguna
                  #lalu di append ke data atas dan data bawah supaya data memperbarui
                  #jika ada salah satu dari entry kosong akan keluar peringatan

                    tambahanNam = self.entnama.get()
                    tambahanJk = self.entjenisKelamin.get()
                    tambahanJb = self.entjabatan.get()
                    tambahanUm = self.entumur.get()
                    tambahanAl = self.entalamat.get()
                    tambahanAg = self.entagama.get()
                    tambahanNp = self.entnopegawai.get()
                    tambahanSk = self.entsift.get()
                    tambahanKd = self.entkendaraan.get()

                    if tambahanNam == ''\
                       or tambahanJk == ''\
                       or tambahanJb == ''\
                       or tambahanUm == ''\
                       or tambahanAl == ''\
                       or tambahanAg == ''\
                       or tambahanNp == ''\
                       or tambahanSk == ''\
                       or tambahanKd == '':
                        mb.showerror('EALAH TOBAT','DATA TIDAK BOLEH KOSONG !')
                        self.simpangagal()
                        
                    else:
                        a = open('karyawan.csv','a')
                        a.write (tambahanNam)
                        a.write (",")
                        a.write (tambahanJk)
                        a.write (",")
                        a.write (tambahanJb)
                        a.write (",")
                        a.write (tambahanUm)
                        a.write (",")
                        a.write (tambahanAl)
                        a.write (",")
                        a.write (tambahanAg)
                        a.write (",")
                        a.write (tambahanNp)
                        a.write (",")
                        a.write (tambahanSk)
                        a.write (",")
                        a.write (tambahanKd)
                        a.write ("\n")
                        a.close ()

                        #*****************data ATAS ditambahkan dengan append agar memperbarui data di GUI dengan otomatis******************************
                        #*****************data_mhs di append lalu menambahkan di GUI******************************
                        self.entryKosong()
                        self.data_hrd_A.append((tambahanNam,tambahanJk,tambahanJb,tambahanUm,tambahanAl,tambahanAg,tambahanNp,tambahanSk,tambahanKd))
                                        
                        self.aturKejadian()
                        self.kosongan()
                        self.isiListbox()
                        self.isiData()                     
                        self.entnama.focus_set()

                        #*****************data BAWAH ditambahkan dengan append agar memperbarui data di GUI dengan otomatis*****************************
                        #*****************self.data_mhs1 di append lalu menambahkan di GUI******************************
                        self.data_hrd_B.append((tambahanNam,tambahanJk,tambahanUm,tambahanAl,tambahanAg,tambahanNp,tambahanSk))
                        
                        #*****************Memanggil fungsi untuk menampilkan data bawah***************************
                        self.databawah()
                                
                        #*****************Lalu keluar pemberitahuan bahwa data sudah ditambahkan********************************************************       
                        mb.showinfo("PT.MULTINASIONAL","DATA SUDAH DITAMBAHKAN")

#****************************************** FUNGSI MENGHAPUS SEMUA DATA ******************************************************************************************             

                  def hapus(self):
                        if askyesno("PT.MULTINASIONAL","ANDA YAKIN INGIN MENGHAPUS SEMUA ?"):
                            if askyesno("PT.MULTINASIONAL","APAKAH SUDAH DISETUJUI BOS BESAR ?"):
                                if askyesnocancel("PT.MULTINASIONAL","ANDA YAKIN BETUL INGIN MENGHAPUS SEMUA ?"):
                                    
                                    tambahanNam = 'NAMA'
                                    tambahanJk = 'KELAMIN'
                                    tambahanJb = 'JABATAN'
                                    tambahanUm = 'UMUR'
                                    tambahanAl = 'ALAMAT'
                                    tambahanAg = 'AGAMA'
                                    tambahanNp = 'ABSEN'
                                    tambahanSk = 'SIFT KERJA'
                                    tambahanKd = 'KENDARAAN'
                                    
                                    a = open('karyawan.csv','w')
                                    a.write (tambahanNam)
                                    a.write (",")
                                    a.write (tambahanJk)
                                    a.write (",")
                                    a.write (tambahanJb)
                                    a.write (",")
                                    a.write (tambahanUm)
                                    a.write (",")
                                    a.write (tambahanAl)
                                    a.write (",")
                                    a.write (tambahanAg)
                                    a.write (",")
                                    a.write (tambahanNp)
                                    a.write (",")
                                    a.write (tambahanSk)
                                    a.write (",")
                                    a.write (tambahanKd)
                                    a.write ("\n")
                                    a.close ()
                                    
                                    #*****************Memanggil atur kejadian awal********************************************
                                    self.aturKejadian()
                                    #*****************Memanggil data atas kosong**********************************************
                                    self.kosongan()
                                   #*****************self.data_mhs1 di append lalu ditampilkan di data bawah*****************
                                    self.data_hrd_B=[]
                                    self.data_hrd_B.append((tambahanNam,tambahanJk,tambahanJb,tambahanUm,tambahanAl,tambahanAg,tambahanNp,tambahanSk,tambahanKd))
                        
                                    #*****************Memanggil fungsi untuk menampilkan data bawah***************************
                                    self.canvas.delete(ALL)
                                    
                                    self.frame = Frame(self.canvas, background="black",pady=3,padx=3)
                                    s=ttk.Style()
                                    s.theme_use('classic')
                                    s.configure("coba.Vertical.TScrollbar", background='black')
                                    
                                    self.canvas.pack(side="left", fill="both", expand=True)
                                    self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                                              tags="self.frame")
                                    self.frame.bind("<Configure>", self.OnFrameConfigure)
                                    
                                    self.rows = len(self.data_hrd_B)  # jumlah baris
                                    self.columns = 7  # jumlah kolom
                                    self._widgets = list()
                                    for row in range(self.rows):
                                        self.current_row = list()
                                        for column in range(self.columns):
                                            tampil = ''
                                            label = Menubutton(self.frame, text="%s" % tampil, borderwidth=1,
                                                           width=12,bg='tan',fg='darkred',font=('stencil', 9),
                                                               compound='center',relief=RIDGE)
                                            label.grid(row=row, column=column, sticky="nsew")
                                            self.current_row.append(label)
                                        self._widgets.append(self.current_row)
                                    for column in range(self.columns):
                                        self.grid_columnconfigure(column, weight=1)

                                    # akhir bagian yang ditambahkan untuk menampilkan data
                                    data_tampil = self.data_hrd_B
                                    for row in range(self.rows):
                                        baris = data_tampil[row]
                                        for column in range(self.columns):
                                            nilai = baris[column]
                                            widget = self._widgets[row][column]
                                            widget.configure(text=nilai)


                                    #*****************lalu keluar pemberitahuan sudah terhapus semua**************************
                                    mb.showwarning('PENTING !!!',
                                                   'Silahkan Import Kembali Untuk Memperbarui Data')
                                    
                                    #*****************menutup window data setelah 3 detik*************************************
                                    root.after(3000, self.destroy) 
                        
#****************************************** FUNGSI SCALE KELUAR GESER ******************************************************************************************             

                  def onScale(self, val):
                      var = IntVar()
                      v = int(float(val))
                      var.set(v)
                      if v == 100 :
                        play =  PlaySound('./suara/exit.wav', SND_FILENAME)
                        self.destroy()
                        
#****************************************** FUNGSI SCROOL DATA BAWAH ******************************************************************************************             

                  def OnFrameConfigure(self, event):
                    '''Reset scroll bawah dengan cnvas'''
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=400)
                    
#****************************************** FUNGSI MENGUBAH WARNA BACKGROUND *************************************************************************************             

                  def onChoose(self):
                    (rgb, warna) = tkColorChooser.askcolor()
                    self.lbltambah.configure(bg=warna)
                    self.lblhapus.configure(bg=warna)                    
                    self.lblsimpan.configure(bg=warna)
                    self.fr_bawah.configure(bg=warna) 
                    self.checkc.configure(bg=warna)
                    self.mainFrame.configure(bg=warna)
                    self.fr_kanan.configure(bg=warna)
                    self.fr_databawah.configure(bg=warna)
                    self.fr_ah1.configure(bg=warna)
                    self.fr_aha.configure(bg=warna)
                    self.fr_ahcanv.configure(bg=warna)
                    self.fr_ahh.configure(bg=warna)
                    self.fr_aho.configure(bg=warna)
                    self.jam.configure(bg=warna)

#****************************************** FUNGSI-FUNGSI LAMPU ***********************************************************************************************             

                  def lampu1(self, a):
                    for i in range(a):
                        self.fr_ahh.delete(ALL)
                        self._oval1 = self.fr_ahh.create_oval(5*self.fracX,5*self.fracY,45*self.fracX,45*self.fracY, fill="white", tags = 'oval1')
                        self._oval4 = self.fr_ahh.create_oval(5*self.fracX,155*self.fracY,45*self.fracX,195*self.fracY, fill="black", tags = 'oval4')
                        self.parent.update()
                        time.sleep(0.04)
                        
##                        self.lbltambah.configure(bg='dark red')
##                        self.lblhapus.configure(bg='dark red')                    
##                        self.lblsimpan.configure(bg='dark red')
##                        self.fr_bawah.configure(bg='dark red') 
##                        self.checkc.configure(bg='dark red')
##                        self.mainFrame.configure(bg='dark red')
##                        self.fr_kanan.configure(bg='dark red')
##                        self.fr_databawah.configure(bg='dark red')
##                        self.fr_ah1.configure(bg='dark red')
##                        self.fr_aha.configure(bg='dark red')
##                        self.fr_ahcanv.configure(bg='dark red')
##                        self.fr_ahh.configure(bg='dark red')
##                        self.fr_aho.configure(bg='dark red')
##                        self.jam.configure(bg='dark red')
                        
                  def lampu2(self, a):
                    for i in range(a):
                        self.fr_ahh.delete(self.fr_ahh)
                        self._oval1 = self.fr_ahh.create_oval(5*self.fracX,5*self.fracY,45*self.fracX,45*self.fracY, fill="black", tags = 'oval1')
                        self._oval2 = self.fr_ahh.create_oval(5*self.fracX,55*self.fracY,45*self.fracX,95*self.fracY, fill="white", tags = 'oval2')
                        self.parent.update()
                        time.sleep(0.04)

##                        self.lbltambah.configure(bg='white')
##                        self.lblhapus.configure(bg='white')                    
##                        self.lblsimpan.configure(bg='white')
##                        self.fr_bawah.configure(bg='white') 
##                        self.checkc.configure(bg='white')
##                        self.mainFrame.configure(bg='white')
##                        self.fr_kanan.configure(bg='white')
##                        self.fr_databawah.configure(bg='white')
##                        self.fr_ah1.configure(bg='white')
##                        self.fr_aha.configure(bg='white')
##                        self.fr_ahcanv.configure(bg='white')
##                        self.fr_ahh.configure(bg='white')
##                        self.fr_aho.configure(bg='white')
##                        self.jam.configure(bg='white')
                        
                  def lampu3(self, a):
                    for i in range(a):
                        self.fr_ahh.delete(self.fr_ahh)
                        self._oval1 = self.fr_ahh.create_oval(5*self.fracX,5*self.fracY,45*self.fracX,45*self.fracY, fill="black", tags = 'oval1')
                        self._oval2 = self.fr_ahh.create_oval(5*self.fracX,55*self.fracY,45*self.fracX,95*self.fracY, fill="black", tags = 'oval2')
                        self._oval3 = self.fr_ahh.create_oval(5*self.fracX,105*self.fracY,45*self.fracX,145*self.fracY, fill="white", tags = 'oval3')
                        self.parent.update()
                        time.sleep(0.04)

##                        self.lbltambah.configure(bg='dark red')
##                        self.lblhapus.configure(bg='dark red')                    
##                        self.lblsimpan.configure(bg='dark red')
##                        self.fr_bawah.configure(bg='dark red') 
##                        self.checkc.configure(bg='dark red')
##                        self.mainFrame.configure(bg='dark red')
##                        self.fr_kanan.configure(bg='dark red')
##                        self.fr_databawah.configure(bg='dark red')
##                        self.fr_ah1.configure(bg='dark red')
##                        self.fr_aha.configure(bg='dark red')
##                        self.fr_ahcanv.configure(bg='dark red')
##                        self.fr_ahh.configure(bg='dark red')
##                        self.fr_aho.configure(bg='dark red')
##                        self.jam.configure(bg='dark red')
                        
                  def lampu4(self, a):
                    for i in range(a):
                        self.fr_ahh.delete(self.fr_ahh)
                        self._oval1 = self.fr_ahh.create_oval(5*self.fracX,5*self.fracY,45*self.fracX,45*self.fracY, fill="black", tags = 'oval1')
                        self._oval2 = self.fr_ahh.create_oval(5*self.fracX,55*self.fracY,45*self.fracX,95*self.fracY, fill="black", tags = 'oval2')
                        self._oval3 = self.fr_ahh.create_oval(5*self.fracX,105*self.fracY,45*self.fracX,145*self.fracY, fill="black", tags = 'oval3')
                        self._oval4 = self.fr_ahh.create_oval(5*self.fracX,155*self.fracY,45*self.fracX,195*self.fracY, fill="white", tags = 'oval4')
                        self.parent.update()
                        time.sleep(0.04)

##                        self.lbltambah.configure(bg='white')
##                        self.lblhapus.configure(bg='white')                    
##                        self.lblsimpan.configure(bg='white')
##                        self.fr_bawah.configure(bg='white') 
##                        self.checkc.configure(bg='white')
##                        self.mainFrame.configure(bg='white')
##                        self.fr_kanan.configure(bg='white')
##                        self.fr_databawah.configure(bg='white')
##                        self.fr_ah1.configure(bg='white')
##                        self.fr_aha.configure(bg='white')
##                        self.fr_ahcanv.configure(bg='white')
##                        self.fr_ahh.configure(bg='white')
##                        self.fr_aho.configure(bg='white')
##                        self.jam.configure(bg='white')

                # tag all of the drawn widgets
                  def flashing(self):
                    import random  
                    if not self._started:
                        self.lampu1(2)
                        self.lampu2(2)
                        self.lampu3(2)
                        self.lampu4(2)
                        
                    self.fr_ahh.after(50, self.flashing)

                    
#****************************************** FUNGSI KOMPONEN DATA  ******************************************************************************************             

                  def aturKomponen(self):
                    self.teksJam = StringVar()
                    self.update()
                    self.mainFrame = Frame(self, bd=10 ,relief=RIDGE)
                    self.mainFrame.pack(fill=BOTH, expand=YES)

                    self.fr_bawah=LabelFrame(self.mainFrame,text='KELUAR   >   >   >  >  > > > ')
                    self.fr_bawah.pack(side=BOTTOM,fill=X,pady=1,padx=2)

                    self.lblkeluar = Scale(self.fr_bawah, from_=0, to=100,orient=HORIZONTAL, 
                                    command=self.onScale,length=300,showvalue=0)
                    self.lblkeluar.pack(side=BOTTOM, fill=X)
                    
                    #*****************kumpulan**fungsi**menampilkan**data**bawah******************************
                    
                    self.fr_databawah=LabelFrame(self.mainFrame,text='DATA GLOBAL',cursor='target')
                    self.fr_databawah.pack(side=BOTTOM,fill=X,pady=4,padx=2)
                    
                    self.mainbawah = Frame(self.fr_databawah, bd=2,bg='black' )
                    self.mainbawah.pack(fill=BOTH,expand=YES)
                    
                    self.canvas = Canvas(self.mainbawah, background="red")
                    self.frame = Frame(self.canvas, background="black",pady=3,padx=3)
                    s=ttk.Style()
                    s.theme_use('classic')
                    s.configure("coba.Vertical.TScrollbar", background='black')
                    self.vsb = ttk.Scrollbar(self.mainbawah, style="coba.Vertical.TScrollbar",orient="vertical", command=self.canvas.yview)
                    self.canvas.configure(yscrollcommand=self.vsb.set)
                    self.vsb.pack(side="left", fill="y")
                    self.canvas.pack(side="left", fill="both", expand=True)
                    self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                              tags="self.frame")
                    self.frame.bind("<Configure>", self.OnFrameConfigure)
                    
                    self.imgdata = PhotoImage(file='./gambar kecil/C.gif')                    

                    #*****************Memanggil fungsi untuk menampilkan data bawah***************************
                    self.databawah()
       
                    #*****************kumpulan**fungsi**menampilkan**data**atas*******************************
                    self.fr_ah1 = Frame(self.mainFrame,relief=FLAT,bd=5)
                    self.fr_ah1.pack(fill=BOTH, expand=YES,side=RIGHT,padx=10)
                    
                    self.fr_aha = Frame(self.fr_ah1, bd=2, relief=GROOVE)
                    self.fr_aha.pack(side=TOP)
                
                    self.fr_ahcanv = Frame(self.fr_aha, bd=2, relief=GROOVE)
                    self.fr_ahcanv.pack(fill=BOTH, expand=YES,side=RIGHT)
                    self.fr_ahh=Canvas(self.fr_ahcanv, width = 50, height = 200,)
                    self.fr_ahh.pack(fill=BOTH,expand=YES)
                    
                    self.fracX = 1
                    self.fracY = 1
                    self._started = False

                    
                    self.fr_as = Frame(self.fr_aha, bd=2, relief=GROOVE,bg='TAN',cursor='hand2')
                    self.fr_as.pack(side=LEFT)
                    self.fr_as_ttp = CreateToolTip(self.fr_as, "Urutkan Data Sekarang") #komen pengurutan
                    self.nama = Label(self.fr_as, text='URUTKAN',bg='tan')
                    self.nama.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.nama = Radiobutton(self.fr_as, text='    nama',command=self.name,bg='tan')
                    self.nama.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.kelamin = Radiobutton(self.fr_as, text='kelamin',command=self.kelamin,bg='tan')
                    self.kelamin.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.umur = Radiobutton(self.fr_as, text='    umur',command=self.umur,bg='tan')
                    self.umur.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.alamat = Radiobutton(self.fr_as, text='  alamat',command=self.alamat,bg='tan')
                    self.alamat.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.agama = Radiobutton(self.fr_as, text='  agama',command=self.agama,bg='tan')
                    self.agama.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.absen = Radiobutton(self.fr_as, text='   absen',command=self.absen,bg='tan')
                    self.absen.pack(fill=BOTH,expand=YES,side=TOP,pady=2)
                    self.sift = Radiobutton(self.fr_as, text='     sift',command=self.sift,bg='tan')
                    self.sift.pack(fill=BOTH,expand=YES,side=TOP,pady=2)

                    self.fr_aho = Frame(self.fr_ah1, relief=GROOVE)
                    self.fr_aho.pack(side=BOTTOM)
                    self.ubahbg = Button(self.fr_aho, text='UBAH BACKGROUND',bg='tan',command=self.onChoose,cursor='hand2')
                    self.ubahbg.pack(fill=BOTH,side=BOTTOM,pady=2)
                    self.ubahbg_ttp = CreateToolTip(self.ubahbg, "Ganti Sesuai Mood Anda") #komen ubah bground
                    self.jam = Label(self.fr_aho, textvariable=self.teksJam,
                                     font=('Century', 13))
                    self.jam.pack(fill=BOTH,side=BOTTOM,pady=2)


                    
                    # frame_atas
                    self.fr_kulitatas=Frame(self.mainFrame,bd=3, bg="tan", relief=FLAT)
                    self.fr_kulitatas.pack(side=TOP,fill=X,pady=2)
                    
                    self.fr_dataatas=Frame(self.fr_kulitatas,bd=3, bg="dark red", relief=FLAT)
                    self.fr_dataatas.pack(side=TOP,fill=X,pady=2)
                    
                    fr_kawah = Frame(self.fr_dataatas)
                    fr_kawah.pack()
               
                    self.lblhapus = Button(fr_kawah, text=25*'* '+' HAPUS SEMUA DATA '+25*' *',
                                                 command=self.hapus, width=70,relief=RAISED,bd=5)
                    self.lblhapus.pack(side=LEFT,fill=BOTH,expand=YES,)

                    # frame_kiri
                    
                    fr_kiri = Frame(self.fr_dataatas, bd=10, bg="black", relief=RIDGE)
                    fr_kiri.pack(fill=BOTH, expand=YES, side=LEFT)

                    fr_list=Frame(fr_kiri)
                    fr_list.pack(fill=BOTH,expand=YES)

                    # ************************* penggunaan listbox n scroll
                    self.listboxData=Listbox(fr_list, width=32)
                    self.listboxData.pack(fill=BOTH, side=LEFT,expand=YES)
                    s=ttk.Style()
                    s.theme_use('classic')
                    s.configure('TScrollbar', background='black')
                    scrollbar = ttk.Scrollbar(fr_list, orient=VERTICAL,
                                       command=self.listboxData.yview,cursor='hand2')
                    scrollbar.pack(side=LEFT, fill=Y)
                    self.listboxData.config(yscrollcommand=scrollbar.set)

                    #tombol TAMBAH DAN SIMPAN

                    fr_tomboltengah = Frame(self.fr_dataatas)
                    fr_tomboltengah.pack(side=LEFT)
                    self.lblsimpan=Button(fr_tomboltengah,text='--\nS\nI\nM\nP\nA\nN\n\n--',
                                       command=self.simpan,
                                       bg='dark red', fg='white')
                    self.lblsimpan.pack(side=BOTTOM) 
                    self.lbltambah=Button(fr_tomboltengah)
                    self.lbltambah.pack(side=BOTTOM)

                    #tombol CARI
                    
                    fr_c=Frame(fr_kiri)
                    fr_c.pack(side=BOTTOM,fill=X,pady=5)

                    self.checkc=Menubutton(fr_c,text='Cari:',fg='yellow',relief=RIDGE,bd=2)
                    self.checkc.pack(side=LEFT)

                    self.entryc=Entry(fr_c,relief=RIDGE,bd=2)
                    self.entryc.pack(side=LEFT,fill=X,expand=YES)
                                    
                    # frame_kanan
                    self.fr_kanan = Frame(self.fr_dataatas, bd=5, relief=RAISED)
                    self.fr_kanan.pack(fill=BOTH, expand=YES, side=RIGHT)
               
                    # fr_kanan_atas
                    fr_katas = Frame(self.fr_kanan, bd=7, bg='black', relief=RIDGE)
                    fr_katas.pack(side=TOP, expand=YES)
                    
               
                    # data nama
                    Label(fr_katas, text='Nama',fg='gold', bg='black').grid(
                          row=0, column=0, sticky=W)
                    self.entnama = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entnama.grid(row=0, column=1)
               
                    # data jenisKelamin
                    Label(fr_katas, text='Jenis Kelamin',fg='gold', bg='black').grid(
                          row=1, column=0, sticky=W)
                    self.entjenisKelamin = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entjenisKelamin.grid(row=1, column=1)
               
                    # data jabatan
                    Label(fr_katas, text='Jabatan',fg='gold', bg='black').grid(
                          row=2, column=0, sticky=W)
                    self.entjabatan = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entjabatan.grid(row=2, column=1)
               
                    # data umur
                    Label(fr_katas, text='Umur',fg='gold', bg='black').grid(
                          row=3, column=0, sticky=W)
                    self.entumur = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entumur.grid(row=3, column=1)

                    # data alamat
                    Label(fr_katas, text='Alamat',fg='gold', bg='black').grid(
                          row=4, column=0, sticky=W)
                    self.entalamat = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entalamat.grid(row=4, column=1)

                    # data agama
                    Label(fr_katas, text='Agama',fg='gold', bg='black').grid(
                          row=5, column=0, sticky=W)
                    self.entagama = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entagama.grid(row=5, column=1)

                    # data nopegawai
                    Label(fr_katas, text='Nomor Absen',fg='gold', bg='black').grid(
                          row=6, column=0, sticky=W)
                    self.entnopegawai = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entnopegawai.grid(row=6, column=1)

                    # data sift
                    Label(fr_katas, text='Sift',fg='gold', bg='black').grid(
                          row=7, column=0, sticky=W)
                    self.entsift = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entsift.grid(row=7, column=1)

                    # data kendaraan
                    Label(fr_katas, text='Kendaraan',fg='gold', bg='black').grid(
                          row=8, column=0, sticky=W)
                    self.entkendaraan = Entry(fr_katas,relief=RIDGE,bd=2)
                    self.entkendaraan.grid(row=8, column=1)
                      
               
                    # fr_kanan_bawah
                    fr_kawah = Frame(self.fr_kanan)
                    fr_kawah.pack(side=BOTTOM, expand=YES)
               
                    self.btnAwal = Button(fr_kawah, text='<<',
                                                 command=self.onAwal, width=6)
                    self.btnAwal.pack(side=LEFT)
                       
                    self.btnPrev = Button(fr_kawah, text='<',
                                                 command=self.onPrev, width=6)
                    self.btnPrev.pack(side=LEFT)
               
                    self.btnNext = Button(fr_kawah, text='>',
                                                 command=self.onNext, width=6,)
                    self.btnNext.pack(side=LEFT)
                       
                    self.btnAkhir = Button(fr_kawah, text='>>',
                                                 command=self.onAkhir, width=6)
                    self.btnAkhir.pack(side=LEFT)
                    
#****************************************** FUNGSI-FUNGSI TOMBOL NEXT,PREV DATA ATAS ***********************************************************************             
   
                  def onAwal(self, event=None):
                    datIndex = self.listboxData.curselection()
               
                    self.listboxData.selection_clear(int(datIndex[0]))
                    self.listboxData.selection_set(0)
                    self.listboxData.activate(0)
                       
                    self.isiData()
                  
                  def onPrev(self, event=None):
                    datIndex = self.listboxData.curselection()
               
                    if int(datIndex[0]) == 0:
                          pass
                    else:
                          self.listboxData.selection_clear(int(datIndex[0]))
                          self.listboxData.selection_set(int(datIndex[0])-1)
                          self.listboxData.activate(int(datIndex[0])-1)
                       
                          self.isiData()
                   
                  def onNext(self, event=None):
                    jumDat = len(self.data_hrd_A)
                    datIndex = self.listboxData.curselection()
               
                    if int(datIndex[0]) == jumDat-1:
                          pass
                    else:
                          self.listboxData.selection_clear(int(datIndex[0]))
                          self.listboxData.selection_set(int(datIndex[0])+1)
                          self.listboxData.activate(int(datIndex[0])+1)
                       
                          self.isiData()
                       
                  def onAkhir(self, event=None):
                    jumDat = len(self.data_hrd_A)
                    datIndex = self.listboxData.curselection()
               
                    self.listboxData.selection_clear(int(datIndex[0]))
                    self.listboxData.selection_set(jumDat-1)
                    self.listboxData.activate(jumDat-1)
                       
                    self.isiData()        
                   
                  def onKeluar(self, event=None):
                    self.destroy()
                    mb.showwarning("PT MULTINASIONAL","TERIMAKASIH")

            DemoListbox(self.parent, self.datJam_menu )
            
        except:
            play =  PlaySound('./suara/polisi.wav', SND_FILENAME)
            mb.showwarning('EALAH TOBAT','IMPORT DULU VROHHH...')
     
#----------------------------------------------------------------------------------------------------------------#
if __name__ =='__main__':
    root = Tk()
    app = Data(root)
    root.mainloop()

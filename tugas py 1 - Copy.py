from texttable import Texttable
table = Texttable ()
jawab = 'y'
no = 0
nama = []
nim = []
nilai_tugas = []
nilai_uts = []
nilai_uas = []
while(jawab == 'y'):
    nama.append(input('Nama :'))
    nim.append(input('Nim  :'))
    nilai_tugas.append(input('Nilai Tugas  :'))
    nilai_uts.append(input('Nilai UTS    :'))
    nilai_uas.append(input('Nilai UAS    :'))
    jawab = input('Tambah data (y/t)?')
    no += 1
for i in range(no):
    tugas = float(nilai_tugas[i])
    uts = float(nilai_uts[i])
    uas = float(nilai_uas[i])
    akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100) 
    table.add_rows([['No','Nama',' NIM ','TUGAS','UTS','UAS','AKHIR'],
                    [i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i]
                    ,nilai_uas[i],akhir]])                                                                                                                                                                                                                                                                                                                                                
print (table.draw())

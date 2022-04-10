import psycopg2
#Connect Database
conn = psycopg2.connect(
         host="localhost",
         database="umc",
         user="iswandi",
         password="123")

#Menyimpan Data Baru
def insert_data(conn):
   idmhs = int(input("Masukan ID Mahasiswa: "))
   nim = input("Masukan NIM Mahasiswa: ")
   nama = input("Masukan Nama Mahasiswa: ")
   idfakultas = int(input("Masukan ID Fakultas Mahasiswa: "))
   idprodi = int(input("Masukan ID Prodi: "))
   val = (idmhs,nim,nama,idfakultas,idprodi)
   sql = "INSERT INTO mahasiswa (idmhs, nim, nama, idfakultas, idprodi) VALUES (%s, %s, %s, %s, %s)"
   cur = conn.cursor()
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} Data Berhasil Disimpan".format(cur.rowcount))

#Menampilkan Data
def show_data(conn):
   cur = conn.cursor()
   sql = "SELECT * FROM mahasiswa"
   cur.execute(sql)
   result = cur.fetchall()

   if cur.rowcount < 0:
      print("==================================")
      print("DATA TIDAK ADA ATAU BELUM TERISI")
   else:
      print("==================================")
      print("-{} DATA BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(conn):
   cur = conn.cursor()
   show_data(conn)
   idmhs = input("Pilih ID Mahasiswa: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   nama = input("Masukan Nama Mahasiswa Yang Baru: ")
   idfakultas = int(input("Masukan Id Fakultas yang Baru: "))
   idprodi = int(input("Masukan Id Prodi Yang Baru: "))
   sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE idmhs=%s"
   val = (nim, nama, idfakultas, idprodi, idmhs)
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} Data Berhasil Diupdate".format(cur.rowcount))

#Menghapus Data
def delete_data(conn):
   cur = conn.cursor()
   show_data(conn)
   idmhs = str(input("Pilih ID Mahasiswa Yang Akan Dihapus: "))
   slc = "SELECT * FROM mahasiswa WHERE idmhs= %s"
   val = (idmhs)
   cur.execute(slc, val)
   con = cur.rowcount
   if (con == 1):
      inp = input("Apakah Anda Yakin Ingin Menghapus Data Tersebut? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
         val = (idmhs)
         cur.execute(sql, val)
         conn.commit()
         print("==================================")
         print("\b{} DATA BERHASIL DIHAPUS".format(cur.rowcount))
      else:
         print("data batal dihapus")
   else:
      print("TIDAK ADA ID YANG DIMAKSUD")
   """sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
   val = (idmhs)
   cur.execute(sql, val)
   conn.commit()
   print("{} Data Berhasil Dihapus".format(cur.rowcount))"""

#Mencari Data
def search_data(conn):
   cur = conn.cursor()
   keyword = input("MASUKAN NIM ATAU NAMA DATA YANG DICARI: ")
   sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   cur.execute(sql, val)
   result = cur.fetchall()

   if cur.rowcount <= 0:
      print("==================================")
      print("TIDAK ADA DATA YANG DIMAKSUD")
   else:
      print("==================================")
      print("{} DATA YANG DIMAKSUD BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Menampilkan Menu
def show_menu(conn):
   print("============================================")
   print("==== TUGAS 1 PEMBUATAN CRUD MELALUI CLI ====")
   print("== DIBUAT OLEH ANTON ISWANDI_( 200510005 )==")
   print("================   PBO2   ==================")
   print("\n1. Insert Data")
   print("2. Show Data")
   print("3. Update Data")  
   print("4. Delete Data")
   print("5. Search Data")
   print("0. Keluar")
   print("------------------")
   menu = input("Pilih Menu: ")

   if menu == "1":
      insert_data(conn)
   elif menu == "2":
      show_data(conn)
   elif menu == "3":
      update_data(conn)
   elif menu == "4":
      delete_data(conn)
   elif menu == "5":
      search_data(conn)
   elif menu == "0":
      exit()
   else:
      print("Menu salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(conn)
from collections import deque
def simulasi_antrian ():
    queue = deque()
    while True:
        print ("\n1. tambah pelanggan ke antrian")
        print ("2. layani pelanggan")
        print ("3. tampilkan antrian")
        print ("4. keluar")
        pilihan = input ("pilih opsi :")
        if pilihan == "1" :
            nama = input ("masukan nama pelangan :")
            queue.append (nama)
            print (f"pelanggan {nama} di tambahkan ke antrian.")
        elif pilihan == "2" :
            if queue :
                dilayani = queue.popleft()
                print (f"pelanggan {dilayani} sedang di layani.")
            else :
                print("antrian kosong")
        elif pilihan == "3" :
            print ("antrian saat inia :",list(queue))
        elif pilihan == "4" :
            print ("keluar dari program.")
        else :
            print ("opsi tidak valid.")
print (simulasi_antrian())

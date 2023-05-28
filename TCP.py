# TUGAS BESAR JARINGAN KOMPUTER KELOMPOK 12

# Import modul
import socket # Import modul socket
import sys # Import modul sys

# NO 1 Implementasi pembuatan TCP socket dan mengaitkannya ke alamat dan port tertentu
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Inisialisasi socket
serverPort = 8080 # Inisialisasi port
serverSocket.bind(('',serverPort)) # Mengkaitkan server IP dan server port
serverSocket.listen(1) # Mendengarkan permintaan koneksi TCP dari klien dengan parameter jumlah maksimum koneksi setidaknya 1
serverJalan = True # Variabel agar server tetap berjalan


while serverJalan: # Saat alamat dan port bernilai benar maka perulangan akan terus dilakukan
    # No 2 Program web server dapat menerima dan memparsing HTTP request yang dikirimkan oleh browser
    print('Server telah siap...') # Mencetak string 'Server telah siap' sebagai tanda server siap atau berjalan
    
    connectionSocket, addr = serverSocket.accept() #variabel connectionSocket dan addr memiliki value serverSocket
    
    try:
        message = connectionSocket.recv(1024).decode() # Inisialisasi message untuk membaca data dari koneksi socket dan di decode
        if not message:# jika data tidak diterima akan break
            break
        filename = message.split()[1] # Membagi request untuk mendapatkan path file yang diminta
        # No 3 Web server dapat mencari dan mengambil file (dari file system) yang diminta oleh client
        f = open(filename[1:]) # inisialisasi f untuk membuka filename satu persatu
        outputdata = f.read() # Inisialisasi output data untuk membaca file f
        f.close() # Menutup file f
        
        # No 4 Web server dapat membuat HTTP response message yang terdiri dari header yang diminta
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n' # Inisialisasi header jika benar
        # No 5 Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client
        connectionSocket.send(header.encode()) # Mengirim respon header yang telah di encode
   
        # No 4 Web server dapat membuat HTTP response message yang terdiri dari konten file yang diminta
        for i in range(0, len(outputdata)):
            # No 5 Web server dapat mengirimkan response message yang sudah dibuat ke browser (client) dan dapat ditampilkan dengan benar di sisi client
            connectionSocket.send(outputdata[i].encode()) # Mengirim respon konten file yang telah di encode
        connectionSocket.send("\r\n".encode())

        #connectionSocket.close() # Menutup koneksi
        
    except IOError:
        # No 6 Jika file yang diminta oleh client tidak tersedia, web server dapat mengirimkan pesan “404 Not Found” dan dapat ditampilkan dengan benar di sisi client.
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n')
        errorMessage = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n' # Inisialisasi error message 
        connectionSocket.send(errorMessage.encode()) # Mengirim respon error Message
        
        #Close client socket
        connectionSocket.close() # Menutup koneksi soket
        serverJalan = False # Jika Server memasuki kondisi IOError maka ia akan mengubah variabel serverJalan agar Keluar dari perulangan dan Menutup server

    
serverSocket.close() # Menutup server soket
print("Server Telah Tertutup") # Mencetak kalimat "Server Telah Tertutup"
sys.exit() # Menghentikan program
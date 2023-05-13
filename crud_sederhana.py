import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('contacts.db')

# Membuat tabel kontak
conn.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             phone TEXT NOT NULL);''')

# Menambahkan kontak baru
def add_contact(name, phone):
    conn.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

# Mencari kontak berdasarkan nama
def search_contact(name):
    cursor = conn.execute("SELECT * FROM contacts WHERE name=?", (name,))
    result = cursor.fetchone()
    return result

# Mengubah kontak yang ada
def update_contact(name, phone):
    conn.execute("UPDATE contacts SET phone=? WHERE name=?", (phone, name))
    conn.commit()

# Menghapus kontak yang ada
def delete_contact(name):
    conn.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()

# Menampilkan semua kontak
def show_contacts():
    cursor = conn.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    for row in results:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Phone:", row[2])
        print()

# Menutup koneksi ke database
def close():
    conn.close()

# Contoh penggunaan fungsi-fungsi CRUD
add_contact("Satriya", "0851111222")
add_contact("Bagus", "0895688812")

print("Daftar Kontak:")
show_contacts()

print("Mencari kontak dengan nama 'Satriya':")
result = search_contact("Satriya")
if result:
    print("ID:", result[0])
    print("Name:", result[1])
    print("Phone:", result[2])
else:
    print("Kontak tidak ditemukan")

print("Mengubah nomor telepon untuk kontak 'Bagus':")
update_contact("Bagus", "0852156125")

print("Daftar Kontak setelah diubah:")
show_contacts()

print("Menghapus kontak dengan nama 'Satriya':")
delete_contact("Satriya")

print("Daftar Kontak setelah dihapus:")
show_contacts()

# Menutup koneksi ke database
close()
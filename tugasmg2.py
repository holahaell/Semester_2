import re
import pandas as pd

data = []
df = pd.DataFrame()

def read_file(filename:str) -> list:
    with open(filename,"r") as file:
        read = file.readlines()
        data = []
        
        for line in read:
            temp = re.split(r"\s{2,}|\n",line)
            data.append(temp[0:4])

    return data

def create_table(data) -> pd.DataFrame:
    df = pd.DataFrame(data, columns =['nama', 'nim', 'asal', 'hobi'])
    return df

def read_data(search_by, value, df):
    index = get_data(search_by, value,df)
    df.loc[index]

    if len(df.loc[index]) == 0:
        return False

    return True

def get_data(search_by, value, df):
    index = df[df[search_by].str.lower().str.contains(value)].index
    return index

def insert_data(data:list, df):
    df = df.append({'nama':data[0], 'nim':data[1], 'asal':data[2], 'hobi':data[3]}, ignore_index=True)
    save_data(df)
    return df
 
def update_data(search_by, value, col:list, new_data:list, df):
    index = get_data(search_by, value, df)
    df.loc[index,col] = new_data
    save_data(df)
    return df

def delete_data(search_by, value, df):
    index = get_data(search_by, value, df)
    df.drop(index, inplace=True)
    save_data(df)
    return df 
    
def save_data(df):
    with open('dataex.txt', 'w') as f: df.to_string(f, col_space=10, header=False, index=False)

def main(source):
    data = read_file(source)
    df = create_table(data)

    while True:
        print("\n=====Pilih Menu=====")
        print(" 1. Tambah Data\n 2. Ubah Data\n 3. Hapus Data")
        pil = str(input("Masukkan Pilihan : "))
        if pil == "1" :
            temp = []
            temp.append(str(input("Nama : ")))
            temp.append(int(input("NIM : ")))
            temp.append(str(input("Asal : ")))
            temp.append(str(input("Hobi : ")))
            df = insert_data(temp, df)
            print(df.tail(1))
        elif pil == "2" :
            cari = input("Mau cari apa? ")
            nilai = input(f"{cari} yang dicari ")
            check = read_data(cari,nilai,df)
            temp_value = []
            temp_col = []
            
            if not check:
                print("Maaf data tidak ada")
                continue

            check = str(input("Mau ganti nama? y/n "))

            if check == 'y':
                temp_value.append(str(input("Masukan nama baru: ")))
                temp_col.append("nama")
                

            check = input("Mau ganti nim? y/n ")

            if check == 'y':
                temp_value.append(input("Masukan nim baru: "))
                temp_col.append("nim")

            check = input("Mau ganti asal? y/n ")

            if check == 'y':
                temp_value.append(str(input("Masukan asal baru: ")))
                temp_col.append("asal")

            check = input("Mau ganti hobi? y/n ")

            if check == 'y':
                temp_value.append(str(input("Masukan nama hobi: ")))
                temp_col.append("hobi")

            update_data(cari,nilai,temp_col,temp_value,df)
            print("Data berhasil diganti")

        elif pil == "3" :
            cari = input("Mau hapus apa? ")
            nilai = input(f"{cari} yang dicari ")
            check = read_data(cari,nilai,df)
            
            check = str(input("Apakah data ingin dihapus? y/n "))

            if not check:
                print("Maaf data tidak ada")
                continue

            if check == 'y':
                delete_data(cari, nilai, df)
            

main("data.txt")
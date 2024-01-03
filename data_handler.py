import json
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets
import random
from ktp import Ui_ktp
class DataHandler:
    @staticmethod
    def simpan_data(data):
        # Generate random 16-digit NIK
        data["NIK"] = str(random.randint(10 ** 15, 10 ** 16 - 1))
        try:
            with open('data.json', 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(data)

        with (open ('data.json', 'w') as file):
            json.dump(existing_data, file)

    @staticmethod
    def simpan_data_edit(new_data):
        with open('data.json', 'r') as file:
            item = json.load(file)
            for data in item:
                if data["NIK"] == new_data["NIK"]:
                    # Perbarui data
                    data['Provinsi'] = new_data['Provinsi']
                    data['Kabupaten/Kota'] = new_data['Kabupaten/Kota']
                    data['Nama'] = new_data['Nama']
                    data['Tempat Lahir'] = new_data['Tempat Lahir']
                    data['Tanggal Lahir'] = new_data['Tanggal Lahir']
                    data['Jenis Kelamin'] = new_data['Jenis Kelamin']
                    data['Golongan Darah'] = new_data['Golongan Darah']
                    data['Alamat'] = new_data['Alamat']
                    data['RT'] = new_data['RT']
                    data['RW'] = new_data['RW']
                    data['Kelurahan'] = new_data['Kelurahan']
                    data['Kecamatan'] = new_data['Kecamatan']
                    data['Agama'] = new_data['Agama']
                    data['Status Pernikahan'] = new_data['Status Pernikahan']
                    data['Pekerjaan'] = new_data['Pekerjaan']
                    data['Kewarganegaraan'] = new_data['Kewarganegaraan']

        with (open ('data.json', 'w') as file):
            json.dump(item, file)

        

    @staticmethod
    def bersihkan_input(ui):
        ui.formNama.clear()
        ui.formTemLahir.clear()
        ui.formTgl.setDate(QDate.currentDate())
        ui.formAlamat.clear()
        ui.formRt.setValue(0)
        ui.formRw.setValue(0)
        ui.formKel.clear()
        ui.formKec.clear()
        ui.formKab.clear()
        ui.formProv.clear()
        ui.formKelamin.setCurrentIndex(0)
        ui.formAgm.setCurrentIndex(0)
        ui.formWork.clear()
        ui.formKwn.setCurrentIndex(0)
        ui.formGolDar.setCurrentIndex(0)
        ui.formStatus.setCurrentIndex(0)

    def baca_data(nama_file):
        with open(nama_file, 'r') as file:
            data = json.load(file)
        return data

    def isi_tabel(tabel, data):
        for baris, item in enumerate(data):
            nik = item['NIK']
            nama = item['Nama']
            jenis_kelamin = item['Jenis Kelamin']

            tabel.insertRow(baris)
            tabel.setItem(baris, 0, QtWidgets.QTableWidgetItem(nik))
            tabel.setItem(baris, 1, QtWidgets.QTableWidgetItem(nama))
            tabel.setItem(baris, 2, QtWidgets.QTableWidgetItem(jenis_kelamin))




    def bersihkan_tabel(tabel):
        tabel.setRowCount(0)

    def get_data_tabel(tabel, row):
        nik = tabel.item(row, 0).text()
        nama = tabel.item(row, 1).text()
        jenis_kelamin = tabel.item(row, 2).text()
        return {'NIK': nik, 'Nama': nama, 'Jenis Kelamin': jenis_kelamin}

    def cariDataKTP(nik):
        with open('data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                if entry['NIK'] == nik:
                    return entry
        return None

    def isiFormDataEdit(form, data):
        if (data is not None):
            form.formNama_edit.setText(data.get('Nama', ''))
            form.formTemLahir_edit.setText(data.get('Tempat Lahir', ''))
            form.formAgm_edit.setCurrentIndex(0)
            form.formGolDar_edit.setCurrentIndex(0)
            form.formAlamat_edit.setText(data.get('Alamat', ''))
            form.formKelamin_edit.setCurrentIndex(0)
            form.formKab_edit.setText(data.get('Kabupaten/Kota', ''))
            form.formKec_edit.setText(data.get('Kecamatan', ''))
            form.formKel_edit.setText(data.get('Kelurahan', ''))
            form.formKwn_edit.setCurrentIndex(0)
            form.formWork_edit.setText(data.get('Pekerjaan', ''))
            form.formProv_edit.setText(data.get('Provinsi', ''))
            form.formRt_edit.setValue(data.get('RT', ''))
            form.formRw_edit.setValue(data.get('RW', ''))
            form.formStatus_edit.setCurrentIndex(0)
            form.formTgl_edit.setDate(QDate.currentDate())
        else:
            print('gagal')
            pass

    def tampilkanKtp(self):
        data_ktp = DataHandler.cariDataKTP(self.nikKTP.text())
        if (data_ktp is not None):
            self.window = QtWidgets.QWidget()
            self.ui = Ui_ktp()
            self.ui.setupUi(self.window)
            self.window.show()

            self.ui.prov.setText(f'PROVINSI {data_ktp["Provinsi"]}')
            self.ui.kab.setText(f'KABUPATEN {data_ktp["Kabupaten/Kota"]}')
            self.ui.nama.setText(f': {data_ktp["Nama"]}')
            self.ui.nik.setText(f': {data_ktp["NIK"]}')
            self.ui.ttl.setText(f': {data_ktp["Tempat Lahir"]}, {data_ktp["Tanggal Lahir"]}')
            self.ui.jenisKelamin.setText(f': {data_ktp["Jenis Kelamin"]}')
            self.ui.golDarah.setText(f'Gol. Darah : {data_ktp["Golongan Darah"]}')
            self.ui.alamat.setText(f': {data_ktp["Alamat"]}')
            self.ui.rtrw.setText(f': {data_ktp["RT"]}/{data_ktp["RW"]}')
            self.ui.kel.setText(f': {data_ktp["Kelurahan"]}')
            self.ui.kec.setText(f': {data_ktp["Kecamatan"]}')
            self.ui.agama.setText(f': {data_ktp["Agama"]}')
            self.ui.status.setText(f': {data_ktp["Status Pernikahan"]}')
            self.ui.work.setText(f': {data_ktp["Pekerjaan"]}')
            self.ui.negara.setText(f': {data_ktp["Kewarganegaraan"]}')

        else:
            print('gagal')

    def tampilkanDataHapus(tabel, data):
        tabel.insertRow(0)
        tabel.setItem(0, 0, QtWidgets.QTableWidgetItem(data['Nama']))
        tabel.setItem(0, 1, QtWidgets.QTableWidgetItem(data['NIK']))
        tabel.setItem(0, 2, QtWidgets.QTableWidgetItem(data['Jenis Kelamin']))
    @staticmethod
    def hapusData(nik):
        with open('data.json', 'r') as file:
            data = json.load(file)
            new_data_list = [item for item in data if item.get('NIK') != nik]

        # simpan data setelah dihapus
        with (open ('data.json', 'w') as file):
            json.dump(new_data_list, file)
from menu import *
from PyQt5 import QtWidgets
from data_handler import DataHandler
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainApps()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_data)
        self.load_data()
        # memfungsikan tombol
        # control
        self.ui.btData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_data))
        self.ui.btData.clicked.connect(lambda: self.load_data())
        self.ui.btEditdata.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_edit))
        self.ui.btHapusData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_hapus))
        self.ui.btTambahData.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tambah))
        self.ui.btInfo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_info))
        # tombol simpan data
        self.ui.btSimpanData.clicked.connect(self.simpan_data)
        #tombol lihat ktp
        self.ui.btLihatKtp.clicked.connect(self.tampilkanDataKTP)
        #tombol cari data edit
        self.ui.btCariData_edit.clicked.connect(self.cariDataEdit)
        self.ui.btSimpanData_edit.clicked.connect(self.simpan_data_edit)
        #tombol menu hapus data
        self.ui.btCariData_hapus.clicked.connect(self.cariDataHapus)
        self.ui.btHapus.clicked.connect(self.hapusDat)


    def load_data(self):
        DataHandler.bersihkan_tabel(self.ui.tableData)
        data_dari_file_json = DataHandler.baca_data('data.json')
        DataHandler.isi_tabel(self.ui.tableData, data_dari_file_json)
    def simpan_data(self):
        data = {
            "Nama": self.ui.formNama.text().upper(),
            "Tempat Lahir": self.ui.formTemLahir.text().upper(),
            "Tanggal Lahir": self.ui.formTgl.date().toString("dd-MM-yyyy"),
            "Alamat": self.ui.formAlamat.text().upper(),
            "RT": self.ui.formRt.value(),
            "RW": self.ui.formRw.value(),
            "Kelurahan": self.ui.formKel.text().upper(),
            "Kecamatan": self.ui.formKec.text().upper(),
            "Kabupaten/Kota": self.ui.formKab.text().upper(),
            "Provinsi": self.ui.formProv.text().upper(),
            "Jenis Kelamin": self.ui.formKelamin.currentText(),
            "Agama": self.ui.formAgm.currentText(),
            "Pekerjaan": self.ui.formWork.text().upper(),
            "Kewarganegaraan": self.ui.formKwn.currentText(),
            "Golongan Darah": self.ui.formGolDar.currentText(),
            "Status Pernikahan": self.ui.formStatus.currentText()
        }
        DataHandler.simpan_data(data)
        DataHandler.bersihkan_input(self.ui)

    def tampilkanDataKTP(self):
        DataHandler.tampilkanKtp(self.ui)

    def cariDataEdit(self):
        data_ktp = DataHandler.cariDataKTP(self.ui.formNIK_edit.text())
        DataHandler.isiFormDataEdit(self.ui, data_ktp)

    def cariDataHapus(self):
        data_ktp = DataHandler.cariDataKTP(self.ui.formNIK_hapus.text())
        DataHandler.tampilkanDataHapus(self.ui.tabelHapus, data_ktp)

    def hapusDat(self):
        nik = self.ui.formNIK_hapus.text()
        DataHandler.hapusData(nik)
        DataHandler.bersihkan_tabel(self.ui.tabelHapus)
    def simpan_data_edit(self):
        dataBaru = {
            "NIK": self.ui.formNIK_edit.text(),
            "Nama": self.ui.formNama_edit.text().upper(),
            "Tempat Lahir": self.ui.formTemLahir_edit.text().upper(),
            "Tanggal Lahir": self.ui.formTgl_edit.date().toString("dd-MM-yyyy"),
            "Alamat": self.ui.formAlamat_edit.text().upper(),
            "RT": self.ui.formRw_edit.value(),
            "RW": self.ui.formRw_edit.value(),
            "Kelurahan": self.ui.formKel_edit.text().upper(),
            "Kecamatan": self.ui.formKec_edit.text().upper(),
            "Kabupaten/Kota": self.ui.formKab_edit.text().upper(),
            "Provinsi": self.ui.formProv_edit.text().upper(),
            "Jenis Kelamin": self.ui.formKelamin_edit.currentText(),
            "Agama": self.ui.formAgm_edit.currentText(),
            "Pekerjaan": self.ui.formWork_edit.text().upper(),
            "Kewarganegaraan": self.ui.formKwn_edit.currentText(),
            "Golongan Darah": self.ui.formGolDar_edit.currentText(),
            "Status Pernikahan": self.ui.formStatus_edit.currentText()
        }
        DataHandler.simpan_data_edit(dataBaru)
        DataHandler.bersihkan_input(self.ui)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MyApp()
     mi_app.show()
     sys.exit(app.exec_())
class Karyawan {
    String nama;
    int umur;

    public Karyawan(String namaAwal, int umurAwal) {
        this.nama = namaAwal;
        this.umur = umurAwal;
    }

    public void tampilProfil() {
        System.out.println("Nama : " + this.nama + ", Umur : " + this.umur + " tahun");
    }

    public int dapatTahunLahir(int tahunSekarang) {
        int tahunLahir = tahunSekarang - this.umur;
        return tahunLahir;
    }

    public void ubahNama(String namaBaru) {
        this.nama = namaBaru;
    }
}

public class ACT6 {
    public static void cekKelayakan(int usia) {
        if (usia >= 17) {
            System.out.println("Status : Layak Kerja.");
        } else {
            System.out.println("Status : Tidak Layak Kerja.");
        }
    }

    public static void ujiPassByVal(int angka) {
        angka = 99;
    }

    public static void ujiPassByRef(Karyawan karyawanObj) {
        karyawanObj.umur = 25;
    }

    public static void main(String[] args) {
        System.out.println("=== METHOD KELAS (STATIC) ===");
        ACT6.cekKelayakan(20);

        System.out.println("\n=== INSTANSIASI KELAS & OBJEK ===");
        Karyawan staff = new Karyawan("Aristo", 19);
        staff.tampilProfil();

        System.out.println("\n=== METHOD DENGAN PARAMETER & RETURN VALUE ===");
        staff.ubahNama("Aristo Azario");
        int tahunLahirStaff = staff.dapatTahunLahir(2026);
        System.out.println ("Nama Baru : " + staff.nama);
        System.out.println ("Tahun Lahir : " + tahunLahirStaff);

        System.out.println("\n=== PASS-BY-VALUE ===");
        int nilaiPrimitif = 10;
        System.out.println("Nilai awal sebelum method : " + nilaiPrimitif);
        ujiPassByVal(nilaiPrimitif);
        System.out.println("Nilai setelah method : " + nilaiPrimitif);

        System.out.println("\n=== PASS-BY-REFERENCE ===");
        System.out.println("Umur awal staff sebelum method : " + staff.umur);
        ujiPassByRef(staff);
        System.out.println("Umur staff setelah method : " + staff.umur);

        System.out.println("\n=== OPERATOR INSTANCEOF ===");
        boolean isKaryawan = staff instanceof Karyawan;
        System.out.println("Apakah variabel 'staff' instansi dari kelas Karyawan? " + isKaryawan);

    }
}

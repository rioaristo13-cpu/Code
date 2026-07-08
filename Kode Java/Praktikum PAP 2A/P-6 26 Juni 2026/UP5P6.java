class Laptop {
    String merk;
    int tahun;

    public Laptop(String merkAwal, int tahunAwal) {
        this.merk = merkAwal;
        this.tahun = tahunAwal;
    }

    public void tampilProfil() {
        System.out.println("Merk : " + this.merk + ", Tahun : " + this.tahun);
    }

    public int dapatTahunKeluar(int tahunSekarang) {
        int tahunKeluar = tahunSekarang - this.tahun;
        return tahunKeluar;
    }

    public void ubahMerk(String merkBaru) {
        this.merk= merkBaru;
    }
}

public class UP5P6 {
    public static void main(String[] args) {
        System.out.println("\n=== INSTANSIASI KELAS & OBJEK ===");
        Laptop laptop = new Laptop("Asus", 2016);
        laptop.tampilProfil();

        System.out.println("\n=== METHOD DENGAN PARAMETER & RETURN VALUE ===");
        System.out.println ("Merk Lama : " + laptop.merk);
        laptop.ubahMerk("Dell");
        int tahunKeluarLaptop = laptop.dapatTahunKeluar(2026); //Masukkan tahun sekarang untuk parameter
        System.out.println ("Merk Baru : " + laptop.merk);
        System.out.println ("Tahun Keluar : " + tahunKeluarLaptop + " tahun lalu");

        System.out.println("\n=== OPERATOR INSTANCEOF ===");
        boolean isLaptop = laptop instanceof Laptop;
        System.out.println("Apakah variabel 'laptop' instansi dari kelas Laptop? " + isLaptop);
    }
}

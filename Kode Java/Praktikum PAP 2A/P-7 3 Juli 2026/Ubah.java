import java.io.*;
import static java.lang.System.out;

public class Ubah {
    public static void main (String[] args) {
        String path = "FolderBelajar";
        File dir = new File(path);
        File file = new File(dir, "data_nilai.txt");
        File fileBaru = new File(dir, "data_lama.txt");

        if (file.exists()) {
            if (file.renameTo(fileBaru)) {
                out.println("File berhasil diubah menjadi : " + fileBaru.getName());
            } else {
                out.println("Nama file gagal diubah");
            }
        } else {
            out.println("File tidak ditemukan.");
        }
    }
}

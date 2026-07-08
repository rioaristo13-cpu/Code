import java.io.*;
import static java.lang.System.out;

public class Hapus {
    public static void main(String [] args) {
        String path = "FolderBelajar";
        File dir = new File(path);
        File fileBaru = new File(dir, "data_lama.txt");

        if (fileBaru.exists()) {
            if (fileBaru.delete()) {
                out.println("File terhapus");
            } else {
                out.println("File gagal dihapus");
            }
        } else {
            out.println("File yang mau dihapus tidak ditemukan");
        }
    }
}

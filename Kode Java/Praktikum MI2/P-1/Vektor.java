public class Vektor {
    public static void main(String[] args) {
        int[] a = {-6, 2, 4, 1};
        int[] b = {4, -1, 3, 5};

        if (a.length != b.length) {
            System.out.println("Vektor a dan b harus memiliki jumlah elemen yang sama.");
            return;
        }

        int[] tambah = new int[a.length];
        int[] kurang = new int[a.length];
        int dotProduct = 0;
        double magnitudeB = 0;

        for (int i = 0; i < a.length; i++) {
            tambah[i] = a[i] + b[i];
            kurang[i] = a[i] - b[i];
            dotProduct += a[i] * b[i];
            magnitudeB += Math.pow(b[i], 2); 
        }

        magnitudeB = Math.sqrt(magnitudeB);

        System.out.print("Penjumlahan (a + b) = [");
        for (int i = 0; i < tambah.length; i++) {
            System.out.print(tambah[i]);
            if (i < tambah.length - 1) System.out.print(", ");
        }
        System.out.println("]");

        System.out.print("Pengurangan (a - b) = [");
        for (int i = 0; i < kurang.length; i++) {
            System.out.print(kurang[i]);
            if (i < kurang.length - 1) System.out.print(", ");
        }
        System.out.println("]");

        System.out.println("Dot Product (a . b) = " + dotProduct);
        System.out.printf("Magnitude dari b = %.2f\n", magnitudeB);
    }
}
public class DeterminanMatriks {

    // Determinan 2x2
    public static int determinan2x2(int[][] m) {
        return m[0][0] * m[1][1] - m[0][1] * m[1][0];
    }

    // Determinan 3x3 - Metode Sarrus
    public static int determinanSarrus3x3(int[][] m) {
        int a = m[0][0], b = m[0][1], c = m[0][2];
        int d = m[1][0], e = m[1][1], f = m[1][2];
        int g = m[2][0], h = m[2][1], i = m[2][2];

        int diagUtama = a * e * i + b * f * g + c * d * h;
        int diagBalik = c * e * g + b * d * i + a * f * h;

        return diagUtama - diagBalik;
    }

    // Determinan 3x3 - Metode Kofaktor (rekursif untuk minor 2x2)
    public static int determinanKofaktor3x3(int[][] m) {
        int det = 0;
        for (int col = 0; col < 3; col++) {
            int[][] minor = getMinor(m, 0, col);
            int sign = (col % 2 == 0) ? 1 : -1;
            det += sign * m[0][col] * determinan2x2(minor);
        }
        return det;
    }

    // Mendapatkan minor dari matriks 3x3
    public static int[][] getMinor(int[][] matrix, int rowToRemove, int colToRemove) {
        int[][] minor = new int[2][2];
        int r = 0;
        for (int i = 0; i < 3; i++) {
            if (i == rowToRemove)
                continue;
            int c = 0;
            for (int j = 0; j < 3; j++) {
                if (j == colToRemove)
                    continue;
                minor[r][c] = matrix[i][j];
                c++;
            }
            r++;
        }
        return minor;
    }

    public static void main(String[] args) {
        int[][] A = {
            { 2, 5 },
            { 3, 4 }
        };

        int[][] B = {
            { 1, 2, 3 },
            { 0, 4, 5 },
            { 1, 0, 6 }
        };

        System.out.println("Determinan A (2x2): " + determinan2x2(A));
        System.out.println("Determinan B (Sarrus): " + determinanSarrus3x3(B));
        System.out.println("Determinan B (Kofaktor): " + determinanKofaktor3x3(B));
    }
}
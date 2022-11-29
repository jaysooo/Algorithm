import java.util.*;

public class Main {
    public static int binarySearch(int[] a, int search_value) {
        int left = 0, mid = 0;
        int right = a.length;

        while (left < right) {
            mid = (left + right) / 2;
            if (search_value == a[mid]) {
                return mid;
            } else if (search_value < a[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }

        }

        return -1;
    }

    public static int[] insertionSort(int[] a) {
        int end = a.length;
        for (int i = 1; i < end; i++) {
            int tmp = a[i];
            int cursor = i - 1;
            while (cursor >= 0) {
                if (tmp < a[cursor]) {
                    a[cursor + 1] = a[cursor];
                    cursor--;
                } else {
                    break;
                }
            }
            a[cursor + 1] = tmp;
        }
        return a;
    }

    public static void main(String[] args) {

        solution();
    }

    public static void solution() {
        int n = 0;
        int[] arr, answer;
        Scanner in = new Scanner(System.in);

        String s = in.nextLine();
        n = Integer.parseInt(s);
        arr = new int[n];

        String[] input_str = in.nextLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input_str[i]);
        }
        s = in.nextLine();
        n = Integer.parseInt(s);
        input_str = in.nextLine().split(" ");
        answer = new int[n];

        for (int i = 0; i < n; i++) {
            answer[i] = Integer.parseInt(input_str[i]);
        }

        Arrays.sort(arr);
        for (int i : answer) {
            if (binarySearch(arr, i) == -1) {
                System.out.println(0);
            } else {
                System.out.println(1);
            }
        }

    }
}
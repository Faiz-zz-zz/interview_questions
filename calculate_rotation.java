public class calculate_rotation {
    static boolean check(String first, String second) {
        //check if they are same length, then check if second is a substring of first concatenated with first.
        return (first.length() == second.length()) && ((first + first).indexOf(second) != -1);
    }

    static int shiftedDiff(String first, String second){
        if (check(first, second) == false)
            return -1;
        else
            return ((second + second).indexOf(first));
    }
}

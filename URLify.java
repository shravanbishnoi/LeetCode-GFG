/*
 Write a method to replace all spaces in a string with "%20". You may assume
 that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

Example:
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
 */

public class URLify {
    public static void main(String[] args) {
        char[] s = "Mr John Smith    ".toCharArray();
        int trueLength = 13;
        URLifyInPlace(s, trueLength);
        System.out.println(s);
    }

    public static void URLifyInPlace(char[] str, int trueLength) {
        int spaceCount = 0;

        for (int i = 0; i < trueLength; i++) {
            if (str[i] == ' ') {
                spaceCount++;
            }
        }

	int newLength = trueLength + spaceCount * 2;


        for (int i = trueLength - 1; i >= 0; i--) {
            if (str[i] == ' ') {
                str[newLength - 1] = '0';
                str[newLength - 2] = '2';
                str[newLength - 3] = '%';
                newLength -= 3;
            } else {
                str[newLength - 1] = str[i];
                newLength--;
            }
        }
    }
}


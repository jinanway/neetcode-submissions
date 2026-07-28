class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sLetters = s.toCharArray();
        char[] tLetters = t.toCharArray();

        Arrays.sort(sLetters);
        Arrays.sort(tLetters);

        boolean check = true;

        if(sLetters.length == tLetters.length){
            for(int i = 0; i < sLetters.length; i++){
                if(sLetters[i] != tLetters[i]){
                check = false;
                }
            }
        } else{
            check = false;
        }

        return check;
    }
}

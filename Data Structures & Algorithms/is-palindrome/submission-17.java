class Solution {
    public boolean isPalindrome(String s) {

        ArrayList<Character> chars = new ArrayList<Character>();
        
        int count = 0;
        int index = 0;
        for(int i = 0; i < s.length(); i++){
            if(((int)Character.toLowerCase(s.charAt(i)) >= 97 && (int)Character.toLowerCase(s.charAt(i)) <= 122) || ((int)Character.toLowerCase(s.charAt(i)) >= 48 && (int)Character.toLowerCase(s.charAt(i)) <= 57)){
                chars.add(Character.toLowerCase(s.charAt(i)));
                System.out.println(Character.toLowerCase(s.charAt(i)));
                count++;
                index = i;
            }
        }
        
        if(count == 1){
            return true;
        }

        int i = 0;
        int j = chars.size() - 1;

        if(i == j){
            return false;
        }

        while(i < chars.size() && j > 0){
            System.out.println(chars.get(i) +" "+ chars.get(j));
            if(chars.get(i) != chars.get(j)){
                return false;
            }

            i++;
            j--;
        }

        return true;
    }
}

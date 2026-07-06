class Solution {
    public boolean isAnagram(String s, String t) {
        int[] s_count = new int[26];
        int[] t_count = new int[26];
        for(int i = 0; i < s.length(); i++) {
            s_count[s.charAt(i) - 'a']++;
        }
        for(int j = 0; j < t.length(); j++) {
            t_count[t.charAt(j) - 'a']++;
        }

        for(int i = 0; i < 26; i++) {
            if (s_count[i] != t_count[i]) {
                return false;
            }
        }

        return true;
    }
}

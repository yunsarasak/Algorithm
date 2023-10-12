#int recursion(const char *s, int l, int r){
#    if(l >= r) return 1;
#    else if(s[l] != s[r]) return 0;
#    else return recursion(s, l+1, r-1);
#}
#
#int isPalindrome(const char *s){
#    return recursion(s, 0, strlen(s)-1);
#}
#
#int main(){
#    printf("ABBA: %d\n", isPalindrome("ABBA")); // 1
#    printf("ABC: %d\n", isPalindrome("ABC"));   // 0
#}

count = 0

def recursion(_str:str, _index:int, _reversed_index:int):
    global count
    count +=1
    #print(count)
    if(_index >= _reversed_index):
        return 1
    elif _str[_index] != _str[_reversed_index]:
        return 0
    else:
        return recursion(_str, _index+1, _reversed_index-1)

def isPalindrome(_str:str):
    global count
    count = 0
    return recursion(_str, 0, len(_str)-1)

T = int(input())

for i in range(T):
    temp_string = input()
    print(isPalindrome(temp_string), count)

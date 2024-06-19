#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n;
int arr[100000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    sort(arr, arr + n, greater<int>());

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        int tmp = 0;
        for (int j = 0; j <= i; j++)
        {
            tmp += arr[i];
        }
        ans = max(ans, tmp);
    }

    cout << ans << '\n';
    return 0;
}

//--------------------------------------------------------------------
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
//--------------------------------------------------------------------
typedef long long ll;
typedef tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update> oset;
//find by order, order of key.
//usage: oset p;  p.insert(x); p.order_of_key(x);
//less, less_equal.
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define pi M_PI
#define yes cout << "YES" << endl;
#define no cout << "NO" << endl;
const int inf=INT_MAX;
const ll infll=LLONG_MAX;
const ll mod = 1e9+7;
//--------------------------------------------------------------------
int n,m,k;
ll cnt=0;
vector <int> dx= {0,0,1,-1};
vector <int> dy= {1,-1,0,0};
vector <vector<int>> g(100001);
vector <int> vis(100001,0),ans,st;
bool valid(int i,int j)
{
    return (i>=0 && i<m && j>=0 && j<n);
}
void add(int x,int y)
{
    g[x].pb(y);
    g[y].pb(x);
}
bool cmp(const pair<string,string> &a,const pair<string,string> &b)
{
    if(a.se==b.se) return a.fi<b.fi;
    else return a.se<b.se;
}
void solve()
{
    int n; cin >> n;
    vector <string> s(n);
    cin.ignore();
    for(auto &x:s) getline(cin,x);
    int cnt=0;
    for(int i=0;i<6;i++)
    {
        bool flag=0;
        for(int j=0;j<n;j++)
        {
            if(s[j][i]=='-' && flag)
            {
                flag=0;
                continue;
            }
            else if(s[j][i]=='-' && !flag) cnt++;
            else if(s[j][i]=='#') flag=1;
        }
    }
    cout << cnt << endl;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    //int tc; cin >> tc;
    //while(tc--)
    solve();
}

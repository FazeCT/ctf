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
#define yes cout << "YES" << endl;
#define no cout << "NO" << endl;
const int inf=INT_MAX;
const ll infll=LLONG_MAX;
const ll mod = 1e9+7;
//--------------------------------------------------------------------
int n,m,k,cnt=0;
vector <int> dx= {0,0,1,-1};
vector <int> dy= {1,-1,0,0};
vector <vector<int>> g(200001);
//vector <int> vis(200001,0),ans,st;
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
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    map <char,int> m;
    for(char a='0'; a<='9'; a++)
    {
        for(char b='0'; b<='9'; b++)
        {
            for(char c='0'; c<='9'; c++)
            {
                for(char d='0'; d<='9'; d++)
                {
                    for(char e='0'; e<='9'; e++)
                    {
                        for(char f='0'; f<='9'; f++)
                        {
                            for(char g='0'; g<='9'; g++)
                            {
                                for(char h='0'; h<='9'; h++)
                                {
                                    for(char i='0'; i<='9'; i++)
                                    {
                                        for(char j='0'; j<='9'; j++)
                                        {
                                            string s="";
                                            s+=a,s+=b,s+=c,s+=d,s+=e,s+=f,s+=g,s+=h,s+=i,s+=j;
                                            if(a+b+c+d+e+f+g+h+i+j-480!=10) continue;
                                            m.clear();
                                            string s1="";
                                            for(auto &x:s) m[x]++;
                                            for(char t='0';t<='9';t++) s1.pb(char(m[t]+48));
                                            if(s==s1)
                                            {
                                                cout << "found: " << s << endl;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << "end" << endl;
}

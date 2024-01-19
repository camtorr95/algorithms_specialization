#include <string>
#include <vector>
#include <iostream>
using namespace std;

long long hash_function(const string& s, int x, int p) {
    long long hash_value = 0;
    for (int i = 0; i < s.length(); ++i) {
        int exp = s.length() - i - 1;
        // write pow function manually
        long long _pow = 1;
        for (int j = 0; j < exp; ++j) {
            _pow = (_pow * x) % p;
        }
        hash_value = (hash_value + static_cast<long long>(s[i]) * _pow) % p;
    }
    return hash_value;
}

class Solver {
public:
    static const int x_1 = 31;
    static const int x_2 = 11111;
    static const int m_1 = 1000000007;
    static const int m_2 = 1000000009;

    Solver(const string& s) : s(s) {
        h_1.resize(s.length() + 1);
        h_2.resize(s.length() + 1);
        for (int i = 0; i <= s.length(); ++i) {
            h_1[i] = hash_function(s.substr(0, i), x_1, m_1);
            h_2[i] = hash_function(s.substr(0, i), x_2, m_2);
        }
    }

    bool ask(int a, int b, int l) {
        return (compute_hash(h_1, m_1, x_1, a, l) == compute_hash(h_1, m_1, x_1, b, l) &&
                compute_hash(h_2, m_2, x_2, a, l) == compute_hash(h_2, m_2, x_2, b, l));
    }

private:
    vector<long long> h_1;
    vector<long long> h_2;
    string s;

    long long compute_hash(const vector<long long>& h, int m, int x, int a, int l) {
        long long pow_x_l = 1;
        for (int i = 0; i < l; ++i) {
            pow_x_l = (pow_x_l * x) % m;
        }
        long long result = (h[a + l] - h[a] * pow_x_l) % m;
        if (result < 0) {
            result += m;
        }
        return result;
    }
};

int main() {
	ios_base::sync_with_stdio(0), cin.tie(0);

	string s;
	int q;
	cin >> s >> q;
	Solver solver(s);
	for (int i = 0; i < q; i++) {
		int a, b, l;
		cin >> a >> b >> l;
		cout << (solver.ask(a, b, l) ? "Yes\n" : "No\n");
	}
}

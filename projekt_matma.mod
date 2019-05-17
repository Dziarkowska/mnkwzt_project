`/*indeksy*/
param v, integer, >= 0;
param e, integer, >= 0;
set D, default {1..d};
param m, integer, >= 0;

param i{v in V} >=0;
param j{v in V} >=0;

set V, default {1..v};
set E, default {1..e};

set M, default {1..m};

/*stale*/
param h{d in D} >=0;


param ksi{e in E} >=0;
param s{d in D} in V, >=0;  # in V
param t{d in D} >=0;
param c{e in E} >=0;

#macierz A{ev} 1 jeœli V---> 

param A{e in E, v in V}, binary, default 0;


#macierz B{ev} 1 jeœli V<---

param B{e in E, v in V}, binary, default 0;


/*zmienne*/
var x{v in V : v == s[d], V in v : v == t[d], i in V, j in V, m in M]

/*funkcja celu*/
minimize z: sum{s{d in D}, t{d in D}, e in E, m in M} ksi[e]*x[s,t,e,m];


/*ograniczenia*/
s.t. C1{d in D, v in V : v==s[d], m in M} : sum{e in E} (B[e,v]*x[e,d] - A[e,v]*x[d,e,m]) = -h[d];

s.t. C2{d in D, v in V : v !=s[d] and v != t[d], m in M} : sum{e in E} (B[e,v]*x[e,d] - A[e,v]*x[e,d]) = 0;

s.t. C3{d in D, v in V : v==t[d], m in M}: sum{e in E} (B[e,v]*x[e,d] - A[e,v]*x[e,d]) = h[d];

s.t. C4{i in V, j in V} : sum{v in V : v == s{d in D}, v in V : v == t{d in D}, m in M} h[d]*x[s,t,e,m] <= c[i,j];

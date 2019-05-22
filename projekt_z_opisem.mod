param v, integer, >= 0; #wierzchołki
param e, integer, >= 0; #łuki
param d, integer, >= 0; #zapotrzebowania
param m, integer, >= 0; #ścieżki realizujące zapotrzebowania
set E, default {1..e};
set V, default {1..v};
set D, default {1..d};
set M, default {1..m};

param h{D} >= 0; #ruch przenoszony przez zapotrzebowanie, u nas coś gadał żeby to podzielić na pół??
param K{E} >= 0; #koszt łuku
param s{D} in V, >= 0; #węzeł źródłowy dla zapotrzebowania d
param t{D} in V, >= 0; #węzeł końcowy dla zapotrzebowania d 
param c{E} >= 0, default 100; #max ile może przepłynąć przez łącze, ale my mamy rozłączne więc nic nam się nie zsumuje chyba
param A{E,V}, binary, default 0; #macierz incydencji, czy łuk e wypływa z wierzchołka v
param B{E,V}, binary, default 0; #macierz incydencji czy łuk e wpływa do wierzchołka v

var x{E,D,M}, binary; # = 1 jeśli łuk e należy do ścieżki m realizującej zapotrzebowanie d
var z{E,D}, >= 0; #CO?
var n{V,D,M}, binary; # = 1 jeśli wierzchołek v należy do ścieżki m realizującej zapotrzebowanie d 

minimize fun: sum{dd in D, ee in E, mm in M} (K[ee]*x[ee,dd,mm]); #minimalizujemy koszt użytych łączy 

s.t. sourceNodesHavePosDemand{dd in D, vv in V : vv == s[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = h[dd];

s.t. transitNodesHaveZeroDemand{dd in D, vv in V : vv != s[dd] and vv != t[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = 0;

s.t. destinationNodesHaveNegDemand{dd in D, vv in V : vv == t[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = -h[dd];

s.t. C4{ee in E}:
	sum{dd in D} 
	(h[dd]*z[ee,dd]) <= c[e];

s.t. C5{dd in D, ee in E}:
	sum{mm in M}
(x[dd,ee,mm]) <= 1;

end; 

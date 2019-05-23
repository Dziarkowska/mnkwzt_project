/*indeksy*/
param v, integer, >= 0;
param e, integer, >= 0;
param d, integer, >= 0;
param m, integer, >= 0;
/*zbiory*/
set V, default {1..v};
set E, default {1..e};
set D, default {1..d};
set M, default {1..m};
/*stale*/
param h{D} >= 0;
param K{E} >= 0;
param s{D} in V, >= 0;
param t{D} in V, >= 0;
param c{E} >= 0, default 100;
param A{E,V}, binary, default 0;
param B{E,V}, binary, default 0;
/*zmienne*/
var x{E,D,M}, binary;
var z{E,D,M}, >=0;
var n{V,D,M}, binary;
/*funkcja celu*/
minimize fun: sum{dd in D, ee in E, mm in M} (K[ee]*z[ee,dd,mm]);
/*ograniczenia*/
s.t. sourceNodesHavePosDemand{mm in M, dd in D, vv in V : vv == s[dd]}:
        sum{ee in E}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = h[dd];

s.t. transitNodesHaveZeroDemand{mm in M, dd in D, vv in V : vv != s[dd] and vv != t[dd]}:
        sum{ee in E}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = 0;

s.t. destinationNodesHaveNegDemand{mm in M, dd in D, vv in V : vv == t[dd]}:
        sum{ee in E}
        (A[ee,vv]*x[ee,dd,mm] - B[ee,vv]*x[ee,dd,mm]) = -h[dd];

s.t. C4{ee in E}:
	sum{dd in D, mm in M} 
	(h[dd]*z[ee,dd,mm]) <= c[e];

s.t. C5{dd in D, ee in E}:
	sum{mm in M}
	x[ee,dd,mm] <= 1;
s.t. C6{vv in V, dd in D}:
	sum{mm in M}
	n[vv,dd,mm] <=1;



data;
## [number of nodes, arcs and demands]
param v := 18;
param e := 22;
param d := 1;
param m := 2;
## [volume of demand, source node, destination node]
param : h  s t :=
1       1 3 7;

param : A :=
    1   6   1
    2  11   1
    3  11   1
    4  11   1
    5  12   1
    6  13   1
    7  13   1
    8   6   1
    9  10   1
   10  15   1
   11  16   1
   12   2   1
   13   9   1
   14   1   1
   15   8   1
   16   2   1
   17   3   1
   18   8   1
   19   3   1
   20   4   1
   21   1   1
   22   5   1;

param : B :=
    1  11   1
    2  13   1
    3  17   1
    4  12   1
    5  13   1
    6  14   1
    7  15   1
    8  14   1
    9  15   1
   10  16   1
   11  17   1
   12  17   1
   13  18   1
   14  18   1
   15   9   1
   16   9   1
   17  10   1
   18  10   1
   19   7   1
   20   5   1
   21   4   1
   22   7   1;

param : K :=
    1   1
    2  10
    3   9
    4   7
    5  14
    6  10
    7   2
    8   0
    9  21
   10   0
   11   5
   12  20
   13   0
   14   8
   15   0
   16  25
   17   0
   18   0
   19   0
   20  26
   21  18
   22   7;

end;

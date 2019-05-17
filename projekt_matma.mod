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
var x{D,E,M}, binary;
var z{E,D}, >=0;
var n{V,D,M}, binary;

/*funkcja celu*/
minimize fun: sum{dd in D, ee in E, mm in M} (K[ee]*x[dd,ee,mm]);

/*ograniczenia*/
s.t. sourceNodesHavePosDemand{dd in D, vv in V : vv == s[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[dd,ee,mm] - B[ee,vv]*x[dd,ee,mm]) = h[dd];

s.t. transitNodesHaveZeroDemand{dd in D, vv in V : vv != s[dd] and vv != t[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[dd,ee,mm] - B[ee,vv]*x[dd,ee,mm]) = 0;

s.t. destinationNodesHaveNegDemand{dd in D, vv in V : vv == t[dd]}:
        sum{ee in E, mm in M}
        (A[ee,vv]*x[dd,ee,mm] - B[ee,vv]*x[dd,ee,mm]) = -h[dd];

s.t. C4{ee in E}:
	sum{dd in D} 
	(h[dd]*z[ee,dd]) <= c[e];

s.t. C5{dd in D, ee in E}:
	sum{mm in M}
	(x[dd,ee,mm]) <= 1;

data;
## [number of nodes, arcs and demands]
param v := 10;
param e := 16;
param d := 2;
param m := 2;
## [volume of demand, source node, destination node]
param : h  s t :=
 1      8  1 10
 2      8  2 8;

# [arc, node, node-link param]
# 1 if link e originates at node v,  0 otherwise
param : A :=
       1 1    1
       2 1    1

       3 2    1
       6 2    1
       7 2    1

       4 3    1
       5 3	  1

       8 4	  1

       10 5   1
       11 5   1

       9 6    1
       15 6   1

       12 7   1
       13 7   1

       14 10   1

       16 9   1;

# [arc, node, node-link param]
# 1 if link e terminates at node v, 0 otherwise
param : B :=
       2 2    1

       1 3    1
       3 3    1

       4 4    1

       7 5	  1

       5 6    1
       6 6    1
       8 6    1

       9 7    1
       10 7   1

       11 8   1

       12 9   1
       15 9   1

       13 10  1
       14 8  1
       16 10  1;

#[arc, cost]
# unit cost of link e
param : K :=
	 1      90
	 2      30
	 3      10
	 4      10
	 5      30
	 6      35
	 7      40
	 8      10
	 9      15
	 10     10
	 11     30
	 12     45
	 13     25
	 14     35
	 15     50
	 16     90;
end;
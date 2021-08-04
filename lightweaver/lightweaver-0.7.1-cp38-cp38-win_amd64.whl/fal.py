import numpy as np
from .atmosphere import Atmosphere, ScaleType
from typing import Callable
import lightweaver.constants as Const

cmass = 10**(np.array([
  -4.93574095E+00,
  -4.93562460E+00,
  -4.93550158E+00,
  -4.93532753E+00,
  -4.93513727E+00,
  -4.93503189E+00,
  -4.93491840E+00,
  -4.93479300E+00,
  -4.93465710E+00,
  -4.93458509E+00,
  -4.93451309E+00,
  -4.93443680E+00,
  -4.93435478E+00,
  -4.93426752E+00,
  -4.93417501E+00,
  -4.93407583E+00,
  -4.93394947E+00,
  -4.93383646E+00,
  -4.93373585E+00,
  -4.93359184E+00,
  -4.93341446E+00,
  -4.93324804E+00,
  -4.93304968E+00,
  -4.93279409E+00,
  -4.93241310E+00,
  -4.93190384E+00,
  -4.93113708E+00,
  -4.93013287E+00,
  -4.92838764E+00,
  -4.92132998E+00,
  -4.90772057E+00,
  -4.87617874E+00,
  -4.82721663E+00,
  -4.76904154E+00,
  -4.70482588E+00,
  -4.64561558E+00,
  -4.56636095E+00,
  -4.45723915E+00,
  -4.31962919E+00,
  -4.18329859E+00,
  -4.00349617E+00,
  -3.80158830E+00,
  -3.60500216E+00,
  -3.37798548E+00,
  -3.14050150E+00,
  -2.88156867E+00,
  -2.67674541E+00,
  -2.49282169E+00,
  -2.33261061E+00,
  -2.16479850E+00,
  -1.98761845E+00,
  -1.78171456E+00,
  -1.58602309E+00,
  -1.42560005E+00,
  -1.28381574E+00,
  -1.14168072E+00,
  -9.79987085E-01,
  -7.80323803E-01,
  -5.83481908E-01,
  -3.89997512E-01,
  -2.00394467E-01,
  -1.52082862E-02,
   7.59830400E-02,
   1.65459096E-01,
   2.52803594E-01,
   3.37693125E-01,
   4.19847399E-01,
   4.98901486E-01,
   5.44588983E-01,
   5.88704407E-01,
   6.17215991E-01,
   6.44935131E-01,
   6.71832442E-01,
   6.97803915E-01,
   7.22732782E-01,
   7.46601224E-01,
   7.69470692E-01,
   7.91397929E-01,
   8.12412739E-01,
   8.32580209E-01,
   8.52005064E-01,
   8.70782733E-01]))

temp = np.array([
1.000000E+05,
9.560000E+04,
9.082000E+04,
8.389000E+04,
7.593000E+04,
7.134000E+04,
6.615000E+04,
6.017000E+04,
5.328000E+04,
4.939000E+04,
4.542000E+04,
4.118000E+04,
3.659000E+04,
3.215000E+04,
2.797000E+04,
2.406000E+04,
2.042000E+04,
1.793000E+04,
1.628000E+04,
1.452000E+04,
1.308000E+04,
1.219000E+04,
1.144000E+04,
1.085000E+04,
1.034000E+04,
9.983000E+03,
9.735000E+03,
9.587000E+03,
9.458000E+03,
9.358000E+03,
9.228000E+03,
8.988000E+03,
8.635000E+03,
8.273000E+03,
7.970000E+03,
7.780000E+03,
7.600000E+03,
7.410000E+03,
7.220000E+03,
7.080000E+03,
6.910000E+03,
6.740000E+03,
6.570000E+03,
6.370000E+03,
6.180000E+03,
5.950000E+03,
5.760000E+03,
5.570000E+03,
5.380000E+03,
5.160000E+03,
4.900000E+03,
4.680000E+03,
4.560000E+03,
4.520000E+03,
4.500000E+03,
4.510000E+03,
4.540000E+03,
4.610000E+03,
4.690000E+03,
4.780000E+03,
4.880000E+03,
4.990000E+03,
5.060000E+03,
5.150000E+03,
5.270000E+03,
5.410000E+03,
5.580000E+03,
5.790000E+03,
5.980000E+03,
6.180000E+03,
6.340000E+03,
6.520000E+03,
6.720000E+03,
6.980000E+03,
7.280000E+03,
7.590000E+03,
7.900000E+03,
8.220000E+03,
8.540000E+03,
8.860000E+03,
9.140000E+03,
9.400000E+03])

ne = np.array([
1.251891E+10,
1.304293E+10,
1.366348E+10,
1.467464E+10,
1.603707E+10,
1.694766E+10,
1.811689E+10,
1.969550E+10,
2.192829E+10,
2.344633E+10,
2.523785E+10,
2.748732E+10,
3.043595E+10,
3.394113E+10,
3.804151E+10,
4.291177E+10,
4.860836E+10,
5.337548E+10,
5.700496E+10,
6.137226E+10,
6.520094E+10,
6.747161E+10,
6.918466E+10,
6.991762E+10,
6.967801E+10,
6.848673E+10,
6.599262E+10,
6.265075E+10,
5.801540E+10,
5.841143E+10,
6.141942E+10,
6.651616E+10,
7.168647E+10,
7.561758E+10,
7.846423E+10,
8.095357E+10,
8.445100E+10,
8.838377E+10,
9.185673E+10,
9.612962E+10,
1.031897E+11,
1.137706E+11,
1.220873E+11,
1.280117E+11,
1.340907E+11,
1.308237E+11,
1.229867E+11,
1.111659E+11,
9.742137E+10,
8.363294E+10,
7.544027E+10,
9.114873E+10,
1.307890E+11,
1.818187E+11,
2.441017E+11,
3.294358E+11,
4.648930E+11,
7.167248E+11,
1.099721E+12,
1.680047E+12,
2.557346E+12,
3.880555E+12,
4.803401E+12,
5.984860E+12,
7.584832E+12,
9.816085E+12,
1.329338E+13,
1.950519E+13,
2.749041E+13,
4.028244E+13,
5.456858E+13,
7.641340E+13,
1.099800E+14,
1.719226E+14,
2.789487E+14,
4.446967E+14,
6.869667E+14,
1.041290E+15,
1.531806E+15,
2.194603E+15,
2.952398E+15,
3.831726E+15])

vel = np.zeros_like(ne)

vturb = np.array([
1.068096E+01,
1.061132E+01,
1.053191E+01,
1.040904E+01,
1.025485E+01,
1.015883E+01,
1.004315E+01,
9.899261E+00,
9.717166E+00,
9.614243E+00,
9.506225E+00,
9.380583E+00,
9.230186E+00,
9.065828E+00,
8.889256E+00,
8.700418E+00,
8.494678E+00,
8.342731E+00,
8.234054E+00,
8.105730E+00,
7.987370E+00,
7.905294E+00,
7.829440E+00,
7.762707E+00,
7.696761E+00,
7.642009E+00,
7.591289E+00,
7.547351E+00,
7.492713E+00,
7.452542E+00,
7.399466E+00,
7.268274E+00,
7.044414E+00,
6.823160E+00,
6.614389E+00,
6.431674E+00,
6.207403E+00,
5.932102E+00,
5.590575E+00,
5.296849E+00,
4.926045E+00,
4.504405E+00,
4.060300E+00,
3.552633E+00,
3.053286E+00,
2.595622E+00,
2.254545E+00,
2.000838E+00,
1.772230E+00,
1.533542E+00,
1.368657E+00,
1.168133E+00,
9.947371E-01,
8.897392E-01,
8.043894E-01,
7.225354E-01,
6.536559E-01,
5.555816E-01,
5.217747E-01,
5.728015E-01,
6.274118E-01,
8.043706E-01,
8.929698E-01,
9.950050E-01,
1.093189E+00,
1.195529E+00,
1.291880E+00,
1.395714E+00,
1.448816E+00,
1.506637E+00,
1.541506E+00,
1.579327E+00,
1.621151E+00,
1.651916E+00,
1.677151E+00,
1.696164E+00,
1.716951E+00,
1.733641E+00,
1.746632E+00,
1.760494E+00,
1.785877E+00,
1.806787E+00])

nh = np.array([
 [1.3575E+05, 6.8537E-02, 4.1543E-02, 5.2083E-02, 7.0588E-02, 1.0457E+10],
 [1.8120E+05, 8.9778E-02, 5.2296E-02, 6.4357E-02, 8.6325E-02, 1.0940E+10],
 [2.2180E+05, 1.0849E-01, 6.1845E-02, 7.5786E-02, 1.0157E-01, 1.1518E+10],
 [3.0033E+05, 1.4368E-01, 7.9102E-02, 9.6471E-02, 1.2932E-01, 1.2472E+10],
 [4.6242E+05, 2.1339E-01, 1.1066E-01, 1.3336E-01, 1.7819E-01, 1.3782E+10],
 [6.9366E+05, 3.1003E-01, 1.5054E-01, 1.7684E-01, 2.3301E-01, 1.4666E+10],
 [1.3849E+06, 5.9161E-01, 2.5732E-01, 2.8646E-01, 3.6466E-01, 1.5806E+10],
 [4.2158E+06, 1.7082E+00, 6.3842E-01, 6.5716E-01, 7.9078E-01, 1.7348E+10],
 [1.7438E+07, 6.7547E+00, 2.0988E+00, 2.0121E+00, 2.2989E+00, 1.9507E+10],
 [4.1507E+07, 1.5910E+01, 4.3394E+00, 4.0155E+00, 4.4810E+00, 2.0955E+10],
 [9.0420E+07, 3.5031E+01, 8.0639E+00, 7.2076E+00, 7.8911E+00, 2.2651E+10],
 [1.9192E+08, 7.7556E+01, 1.4038E+01, 1.2016E+01, 1.2892E+01, 2.4761E+10],
 [3.9573E+08, 1.7367E+02, 2.2333E+01, 1.7985E+01, 1.8816E+01, 2.7491E+10],
 [7.6782E+08, 3.8073E+02, 3.2088E+01, 2.3695E+01, 2.4001E+01, 3.0720E+10],
 [1.3781E+09, 7.8156E+02, 4.0771E+01, 2.6967E+01, 2.6251E+01, 3.4498E+10],
 [2.2770E+09, 1.4505E+03, 4.5906E+01, 2.6811E+01, 2.5012E+01, 3.8972E+10],
 [3.7225E+09, 2.6394E+03, 4.9540E+01, 2.5431E+01, 2.3463E+01, 4.4299E+10],
 [5.2214E+09, 3.9059E+03, 5.0812E+01, 2.6042E+01, 2.4141E+01, 4.8930E+10],
 [6.6626E+09, 5.1186E+03, 5.2395E+01, 2.7202E+01, 2.6187E+01, 5.2534E+10],
 [8.8304E+09, 6.9532E+03, 5.5943E+01, 2.9634E+01, 2.9744E+01, 5.6932E+10],
 [1.1553E+10, 9.2281E+03, 6.4637E+01, 3.4923E+01, 3.7451E+01, 6.0910E+10],
 [1.4098E+10, 1.1403E+04, 7.3911E+01, 4.0362E+01, 4.4988E+01, 6.3407E+10],
 [1.7114E+10, 1.4020E+04, 8.5943E+01, 4.5854E+01, 5.1452E+01, 6.5364E+10],
 [2.0838E+10, 1.7311E+04, 1.0161E+02, 5.2368E+01, 5.8441E+01, 6.6372E+10],
 [2.5891E+10, 2.1876E+04, 1.2297E+02, 6.0053E+01, 6.5132E+01, 6.6303E+10],
 [3.1402E+10, 2.6917E+04, 1.4694E+02, 6.8666E+01, 7.2591E+01, 6.5146E+10],
 [3.8232E+10, 3.3232E+04, 1.7632E+02, 7.7801E+01, 7.8598E+01, 6.2533E+10],
 [4.5560E+10, 3.9880E+04, 2.0719E+02, 8.6650E+01, 8.3415E+01, 5.9011E+10],
 [5.5102E+10, 4.8458E+04, 2.4757E+02, 9.7736E+01, 8.8989E+01, 5.4017E+10],
 [5.7964E+10, 5.4260E+04, 2.8263E+02, 1.0840E+02, 9.7220E+01, 5.4344E+10],
 [5.9182E+10, 6.1715E+04, 3.3533E+02, 1.2464E+02, 1.1103E+02, 5.7485E+10],
 [6.5344E+10, 7.4390E+04, 4.4226E+02, 1.5492E+02, 1.3655E+02, 6.2829E+10],
 [8.2151E+10, 8.9723E+04, 6.0246E+02, 1.9568E+02, 1.7001E+02, 6.8334E+10],
 [1.1036E+11, 1.0429E+05, 7.9208E+02, 2.3960E+02, 2.0478E+02, 7.2705E+10],
 [1.5001E+11, 1.1653E+05, 9.9266E+02, 2.8278E+02, 2.3757E+02, 7.6065E+10],
 [1.9295E+11, 1.2641E+05, 1.1790E+03, 3.2206E+02, 2.6657E+02, 7.8977E+10],
 [2.6230E+11, 1.3886E+05, 1.4373E+03, 3.7651E+02, 3.0599E+02, 8.2849E+10],
 [3.8968E+11, 1.5218E+05, 1.7727E+03, 4.4648E+02, 3.5489E+02, 8.7015E+10],
 [6.2100E+11, 1.6352E+05, 2.1393E+03, 5.2332E+02, 4.0632E+02, 9.0571E+10],
 [9.5313E+11, 1.7702E+05, 2.5351E+03, 6.1111E+02, 4.6521E+02, 9.4755E+10],
 [1.6358E+12, 2.0103E+05, 3.1704E+03, 7.5945E+02, 5.6539E+02, 1.0158E+11],
 [2.9344E+12, 2.3968E+05, 4.1359E+03, 9.9542E+02, 7.2522E+02, 1.1172E+11],
 [5.1240E+12, 2.7229E+05, 5.0498E+03, 1.2318E+03, 8.8165E+02, 1.1951E+11],
 [9.6535E+12, 2.9688E+05, 5.8820E+03, 1.4659E+03, 1.0325E+03, 1.2464E+11],
 [1.8438E+13, 3.2259E+05, 6.7349E+03, 1.7248E+03, 1.1997E+03, 1.2928E+11],
 [3.6505E+13, 3.0568E+05, 6.6484E+03, 1.7553E+03, 1.2102E+03, 1.2320E+11],
 [6.1457E+13, 2.6707E+05, 5.9364E+03, 1.6013E+03, 1.0998E+03, 1.1141E+11],
 [9.7948E+13, 2.1143E+05, 4.7619E+03, 1.3051E+03, 8.9495E+02, 9.3966E+10],
 [1.4797E+14, 1.5107E+05, 3.4275E+03, 9.4933E+02, 6.5079E+02, 7.3185E+10],
 [2.2913E+14, 9.1943E+04, 2.0952E+03, 5.8468E+02, 4.0108E+02, 4.8909E+10],
 [3.6573E+14, 4.4954E+04, 1.0268E+03, 2.8785E+02, 1.9781E+02, 2.4559E+10],
 [6.2095E+14, 2.5504E+04, 5.8319E+02, 1.6405E+02, 1.1310E+02, 1.0707E+10],
 [1.0059E+15, 2.1516E+04, 4.9230E+02, 1.3888E+02, 9.6129E+01, 5.9846E+09],
 [1.4721E+15, 2.5057E+04, 5.7350E+02, 1.6223E+02, 1.1268E+02, 4.9014E+09],
 [2.0529E+15, 3.1103E+04, 7.1209E+02, 2.0204E+02, 1.4078E+02, 4.4674E+09],
 [2.8443E+15, 4.5788E+04, 1.0487E+03, 2.9876E+02, 2.0880E+02, 4.8749E+09],
 [4.1045E+15, 7.8697E+04, 1.8038E+03, 5.1748E+02, 3.6298E+02, 6.0219E+09],
 [6.4161E+15, 1.8279E+05, 4.2000E+03, 1.2231E+03, 8.6292E+02, 9.5137E+09],
 [9.9334E+15, 4.3826E+05, 1.0139E+04, 3.0336E+03, 2.1574E+03, 1.6045E+10],
 [1.5216E+16, 1.0786E+06, 2.5422E+04, 7.9600E+03, 5.7304E+03, 2.9160E+10],
 [2.3024E+16, 2.7091E+06, 6.6875E+04, 2.2366E+04, 1.6388E+04, 5.7743E+10],
 [3.4369E+16, 6.8981E+06, 1.8667E+05, 6.7490E+04, 5.0629E+04, 1.2481E+11],
 [4.1710E+16, 1.1619E+07, 3.3576E+05, 1.2627E+05, 9.6131E+04, 1.9896E+11],
 [5.0148E+16, 2.1014E+07, 6.5910E+05, 2.5792E+05, 1.9970E+05, 3.4826E+11],
 [5.9713E+16, 4.2209E+07, 1.4620E+06, 5.9702E+05, 4.7139E+05, 6.9089E+11],
 [7.0420E+16, 8.8974E+07, 3.4558E+06, 1.4750E+06, 1.1892E+06, 1.4460E+12],
 [8.2158E+16, 2.0209E+08, 8.9288E+06, 3.9956E+06, 3.2940E+06, 3.2132E+12],
 [9.4511E+16, 5.0160E+08, 2.5675E+07, 1.2109E+07, 1.0232E+07, 7.4971E+12],
 [1.0142E+17, 1.0304E+09, 5.9280E+07, 2.9162E+07, 2.5133E+07, 1.4201E+13],
 [1.0836E+17, 2.0887E+09, 1.3542E+08, 6.9500E+07, 6.1092E+07, 2.5616E+13],
 [1.1260E+17, 3.5191E+09, 2.4944E+08, 1.3213E+08, 1.1787E+08, 3.8905E+13],
 [1.1656E+17, 6.0988E+09, 4.7555E+08, 2.6052E+08, 2.3606E+08, 5.9653E+13],
 [1.2019E+17, 1.0794E+10, 9.3061E+08, 5.2815E+08, 4.8646E+08, 9.1990E+13],
 [1.2266E+17, 2.1229E+10, 2.0662E+09, 1.2237E+09, 1.1495E+09, 1.5246E+14],
 [1.2435E+17, 4.3284E+10, 4.7954E+09, 2.9718E+09, 2.8511E+09, 2.5766E+14],
 [1.2556E+17, 8.4898E+10, 1.0640E+10, 6.8842E+09, 6.7376E+09, 4.2126E+14],
 [1.2674E+17, 1.5801E+11, 2.2182E+10, 1.4934E+10, 1.4887E+10, 6.6104E+14],
 [1.2739E+17, 2.8457E+11, 4.4505E+10, 3.1118E+10, 3.1567E+10, 1.0125E+15],
 [1.2768E+17, 4.8921E+11, 8.4550E+10, 6.1220E+10, 6.3118E+10, 1.4999E+15],
 [1.2786E+17, 8.0810E+11, 1.5323E+11, 1.1461E+11, 1.1995E+11, 2.1593E+15],
 [1.2836E+17, 1.2215E+12, 2.4986E+11, 1.9190E+11, 2.0333E+11, 2.9137E+15],
 [1.2887E+17, 1.7545E+12, 3.8349E+11, 3.0146E+11, 3.2285E+11, 3.7897E+15],
]).T

Falc82: Callable[[], Atmosphere] = lambda: Atmosphere.make_1d(ScaleType.ColumnMass, depthScale=cmass*Const.G_TO_KG / Const.CM_TO_M**2, temperature=np.copy(temp), ne=ne / Const.CM_TO_M**3, vlos=vel * Const.KM_TO_M, vturb=vturb * Const.KM_TO_M, hydrogenPops=nh / Const.CM_TO_M**3)
# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/28 15:51'
i m p o r t os f sys farcpy
f= o p e n (r * D :\2017UC\Demo\Demol\resuit.t x t T f 'w 1 )
rows=arcpy.S e a r c h C u r s o r ('t e s t d a t a ') row=rows.n e x t () u n i q u eList=[] uniqueListDILEI=[]
w h i l e r o w :
if r o w . g e t V a l u e (,1XIANTM ) not in uniqueList : uniqu e L i s t . append. (r o w . getValue ( "XIAN-11)); row=rows.n e x t () for i in r a n g e (0,len(uniqueList)) : filter=uniqueList[i ]
x i a n = , n X I A N M + ' -4-filter 4- M ' M
c口工=a.工upy.Searchcursor(n testdata"fxian) for row2 in c u r :
w h i l e r o w 2 :
if row2 . g e t V a l u e (TlDI L E I " ) not in uniqueListDILEI: uniqueLis t DI L E I . append (row 2 . getValue ( " DI L E I 11)) row2=cur.n e x t () 申 for k in r a n g e (0,len(uniqueListDILEI) ) : flt=uniqueListDILEI[k]
dilei=' M DI L E I M 1 + 1' = M + 1' ' M + flt + M ' M + M AND M +xian
f l r n T
B
p r i n t (dilei+r, r,)
searchcur=arGpy. Sear chCur sor (T,testdataN f dil e i ) v a l u e = 3 .0 B for row3 in s e a r c h c u r : v a lue+=row3.g e t V a l u e (MMIAN J I n )
p r i n t (value)
f . write lines ( [filter + ,1 11 , f lt + 1' n r * %s T %value4-ir\ n ri ])
f .close ()
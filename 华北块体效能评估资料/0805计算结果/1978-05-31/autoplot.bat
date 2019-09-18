gmtset BASEMAP_TYPE FANCY PLOT_DEGREE_FORMAT ddd:mm:ssF GRID_CROSS_SIZE_PRIMARY 0 FRAME_WIDTH 0.14c
gmtset ANOT_FONT_SIZE 12
rem
rem
rem 	
set AREA=105/128/30/42
rem set AREA=107/125/30/42											
set inputfile=netlist.txt
set ps=netlist.ps
set PROJ=M6i
rem
rem
rem
grdcut ..\file\china.grd -R%AREA%  -Gplot.grd
makecpt -C..\file\china5.cpt -T-80/8000/80 -Z  -V >china2.cpt
grdgradient plot.grd -Gplot.shd -A0/270 -Nt1
grdimage plot.grd -J%PROJ% -R%AREA% -Cchina2.cpt -Ba5f5/a5f5WSEN  -Iplot.shd -X1.8 -Y7.2 -P -K >%ps%
pscoast -J%PROJ% -R%AREA%  -Dh -A200  -S255/255/255 -C255/255/255 -O -K>>%ps%

psxy ..\file\China_boundary.txt -R -J%PROJ%  -M -W0.5p,black -O -K >>%ps%
psxy ..\file\china_province.dat -J%PROJ% -R%AREA% -W0.5p,black -M  -O -K >>%ps%
psxy ..\file\chinafault.txt -R -J%PROJ% -M -W0.2p,black -O -K >>%ps%

gawk  "{print $2,$1,1111,$4,$3,1111,$6,$5,1111,$8,$7,1111,$2,$1, "($1+$3+$5+$7)/4",($2+$4+$6+$8)/4}" %inputfile% |gawk "{print 1111,$1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14}" | gawk "gsub(/1111 /,\"a\n\")" |gawk "{print $1,$2}"  > square.txt
gawk  "{print $10, "($1+$3+$5+$7)/4",($2+$4+$6+$8)/4}" %inputfile% |gawk "{print $3,$2,$1}"  > spot.txt
psxy square.txt -R -J  -Ma  -W2.5p,red -L -O -K >>%ps%
gawk "{print $3,$2,0.05*$4}" eq.txt | psxy -J -R -Scc -Gred -W1 -O -K -P -V >> %ps%
gawk "{print $1,$2-0.3,14,0,35,2,$3}" spot.txt | pstext -R -J -Gblue -O >>%ps%


ps2raster netlist.ps -A -Tj -E700 -P -C-sFONTPATH="c:\windows\fonts\ -dNOSAFER
del square.txt spot.txt china2.cpt plot.grd plot.shd .gmt* *.eps *.bb *.ps
exit
from appJar import gui
import math




def upper(matrix):
    while(matrix[0][0]!=0 and matrix[1][0]!=0):
    	#t=24
        if(matrix[0][0]>=matrix[1][0]):
            q=int(matrix[0][0]/matrix[1][0]) 
            matrix[0][0]=matrix[0][0]-q*matrix[1][0] #I-int(a/b)*II->I
            matrix[0][1]=matrix[0][1]-q*matrix[1][1]
            matrix[0][2]=matrix[0][2]-q*matrix[1][2]
            # app.setLabel("post_novi"+"_"+"1"+str(t), matrix)
            # t+=1
        else:
            r=int(matrix[1][0]/matrix[0][0])
            matrix[1][0]=matrix[1][0]-r*matrix[0][0] #II-int(b/a)*I->II
            matrix[1][1]=matrix[1][1]-r*matrix[0][1]
            matrix[1][2]=matrix[1][2]-r*matrix[0][2]
            # app.addLabel("b_result"+"_"+"1"+str(k), str(matrix), k+23,1)
            # k++
    return matrix
    # print(matrix)
def result(n,b,m):
	nzdd=nzd_rek(n,m)		#zbog provjere egzistencije rjesenja
	# print("nzd je: ")
	# print(nzdd)
	if(b%nzdd!=0):
		app.warningBox("Greška!", "Sistem nema rješenje.", parent=None)
	else:
		if(n>m):
			matrica=[[n,1,0],[m,0,1]]
			upper(matrica)	#odavde x izvlacimo.
			print("nova matrica je:")
			print(matrica)
			if(matrica[0][0]>0):
				return matrica[0][1]
			else:
				return matrica[1][1]
		else:
			matrica=[[b,1,0],[m,0,1]]
			upper(matrica)	#odavde x izvlacimo.
			print("nova matrica je:")
			print(matrica)
			if(matrica[0][0]>0):
				return matrica[0][1]
			else:
				return matrica[1][1]
		
		#print(upper(matrica))
	# matrica=[[n,1,0],[b,0,1]]
	# print(upper(matrica))
	# return upper(matrica)
	# if(matrica[0][0]>0):
	# 	return matrica[0][1]
	# else:
	# 	return matrica[1][1]

#funkcija num treba da uzme broj koji je unijet i da na osnovu njega napravi toliko 
#labela i inputa za unos. 
def num(n):
	j=1
	i=int(1)
	n=int(app.getEntry("unos_br"))
	if(n<2 or math.ceil(n)!=n):
		app.warningBox("Greška!","Dozvoljen je samo unos pozitivnih cijelih brojeva! Takođe, najmanji broj koji možete unijeti je 2!", parent=None)
	else:
		for i in range(n):
			app.addNumericEntry("num_"+str(i), i+2,j+1)
			app.addLabel("x"+str(i),"X", i+2, j+2)
			app.addNumericEntry("numb_"+str(i), i+2, j+3)
			app.addLabel("m_"+str(i), "mod", i+2, j+4)
			app.addNumericEntry("m_num_"+str(i), i+2, j+5)
			app.addLabel("empty_"+str(i), " ", i+2, j+6)
	#print(i)
	#print(j)
	app.removeButton("Potvrdi")
	app.removeLabel("unos")
	app.hideEntry("unos_br")
	app.addButton("Riješi pomoću Kineske teoreme",solve, i+n+2, 2)
	app.addLabel("res","Rezultat: ", i+n+3, 2)
	app.setLabelBg("res", "grey")
	app.addLabel("res_num", " ", i+n+3, 3)
#nzd
def nzd_rek(a,b): 
    if a == 0: 
        return b 
    return int(nzd_rek(b % a, a))
#rjesavanje
def solve():
	n=int(app.getEntry("unos_br"))
	k=1
	for k in range(n):
		if((app.getEntry("num_"+str(k))<1 or math.ceil(app.getEntry("num_"+str(k)))!=app.getEntry("num_"+str(k))) or (app.getEntry("numb_"+str(k))<1 or math.ceil(app.getEntry("num_"+str(k)))!=app.getEntry("num_"+str(k))) or (app.getEntry("m_num_"+str(k))<1 or math.ceil(app.getEntry("m_num_"+str(k)))!=app.getEntry("m_num_"+str(k))) ):
			app.warningBox("Greška!","Dozvoljen je unos samo pozitivnih cijelih brojeva!", parent=None)
		else:
			s=0		#l - brojac za citanje ulaza
			l=1
			a=[]
			b=[]
			m=[]
			for l in range(n):
				#print(int(app.getEntry("num_"+str(l))))
				a.append(int(app.getEntry("num_"+str(l))))
				b.append(int(app.getEntry("numb_"+str(l))))
				m.append(int(app.getEntry("m_num_"+str(l))))
				#print(a)
				#print(b)
				#print(m)
				#da li jednacina ima rjesenje?
		#print("len(m)-1=:")
		#print(len(m)-1)
	d=0		#d,c - brojaci za ispitivanje da li su uzajamno prosti
	c=1
	r=0
	while(d!=len(m)-1 and c!=len(m)):
		if(nzd_rek(m[d],m[c])==1):
			d=d+1
			c=c+1
		else:
			r=r+1
			d=d+1
			c=c+1
	if(r>0):
		#print(r)
		app.warningBox("Greška!","Sistem nema rješenje!", parent=None)
	else:
		print("ima rjesenje")
		#sad treba da formiramo m, pa onda n1, n2... 
		M=1		#racunamo M za kinesku teoremu
		indeks=0
		for indeks in range(len(m)):
			M=M*m[indeks]
		#print(M)
	#sada hocemo da deklarisemo niz n[] i da ga popunimo sa M/n_j
	print(M)
	n=[]		#niz n_j elemenata za novi sistem
	brojac=0
	#print(len(m))
	for brojac in range(len(m)):
		n.append(int(M/m[brojac]))
	print(n)
	#stampanje novog sistema zbog provjere.
	br=0
	for br in range(len(m)):
		# print("niz b:")
		# print(b)
		print(str(n[br])+" x = "+str(b[br])+" ( mod "+str(m[br])+" )")
	#sad hocemo da napravimo niz x[] u koji cemo da smjestimo rjesenja jednacina
	x=[]	#niz rjesenja
	k=0		#brojac za rjesavanje jednacina
	for k in range(len(m)):
		x.append(result(n[k],b[k],m[k]))

	#hocemo da stampamo pozitivne rezultate:
	print(x)
	w=0
	for w in range(len(m)):		#k=s/d
		# x[w]=x[w]*int(b[w]/int(nzd_rek(n[w],m[w])))
		x[w]=x[w]*b[w]
	print(x)
	q=0
	for q in range(len(m)):
		while(x[q]<1):
			x[q]=x[q]+m[q]
	print(x)
	#treba da stampamo konacan rezultat x=n_1*x_1+n_2*x_2+...n_k*x_k
	e=0
	res=0
	for e in range(len(m)):
		res=res+x[e]*n[e]
	print(res)
	app.setLabel("res_num", str(res))
	#print(result(n[k],b[k],m[k]))
	# matrica=[[n[0],1,0],[b[0],0,1]]
	# print(upper(matrica))
	# print(b[0])

app=gui("Kineska teorema o ostacima")

#unos
app.addLabel("kineska", "Kineska teorema", 0,0)
app.setLabelBg("kineska", "grey")
app.addLabel("unos", "Unesite broj jednačina: ", 0,1)
app.addNumericEntry("unos_br", 0,2)
app.addButton("Potvrdi", num, 0,3)
#nakon zavrsenog unosa treba da provjerimo da li su moduli uzajamno prosti. Ukoliko nisu, nema rjesenja.



app.go()
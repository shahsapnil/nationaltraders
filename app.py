from flask import Flask , redirect, render_template,request
from num2words import num2words

app=Flask(__name__)

@app.route("/")
def index():
    return(render_template('details.html'))

@app.route("/register",methods=['GTE','POST'])
def register():
    if request.method=='POST':
        data=request.form

        def is_float(value):
            try:
                float(value)
                return True
            except:
                return False


        mainlist=[]
        for i,j in data.items():
            list1=[]
            list1.append(i)
            if j.isdigit() or is_float(j):
                k=float(j)
                list1.append(k)
            else:
                list1.append(j)
            mainlist.append(list1)
        # print(mainlist)
        finallist=[]
        passlist=mainlist[:7]
        list2=[]
        for i in passlist:
            list2.append(i[1])
        # print(list2)
        for i in range(7,len(mainlist)):
            if mainlist[i][1]!='':
                finallist.append(mainlist[i][1])
        print(finallist)


        def roundTraditional(val,digits):
            return round(val+10**(-len(str(val))-1), digits)

        rate=finallist[3]/1.28
        total=(finallist[3]/1.28)*finallist[2]

        total1=roundTraditional(total,2)

        print(total1)
        cgst=(total*14)/100
        cgst1=roundTraditional(cgst,2)
        sgst=(total*14)/100
        sgst1=roundTraditional(sgst,2)
        final = total+cgst+sgst
        roffvalue=round(final)
        roff=round(final-roffvalue,2)
        invoice=int(list2[1])

        textfinal=num2words(roffvalue).upper()+' ONLY'
        return render_template('invoice.html',finallist=finallist,list2=list2,roffvalue=roffvalue,roff=roff,textfinal=textfinal,invoice=invoice,total=total1,rate=rate,cgst=cgst1,sgst=sgst1,key=list2[0])
if __name__=="__main__":
    app.run()

    
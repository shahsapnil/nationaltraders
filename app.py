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
        passlist=mainlist[:6]
        list2=[]
        for i in passlist:
            list2.append(i[1])
        # print(list2)
        for i in range(6,len(mainlist)):
            if mainlist[i][1]!='':
                finallist.append(mainlist[i][1])
        print(finallist)
        print(list2)
        total=(finallist[2]/1.28)*finallist[3]
        cgst=(total*14)/100
        sgst=(total*14)/100
        final = total+cgst+sgst
        roffvalue=round(final)
        roff=round(final-roffvalue,2)

        textfinal=num2words(roffvalue).upper()+' ONLY'
        return render_template('invoice.html',finallist=finallist,list2=list2,roffvalue=roffvalue,roff=roff,textfinal=textfinal)
if __name__=="__main__":
    app.run(debug=True)
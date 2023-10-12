from tkinter import *
from tkinter import ttk
import time
import random
import datetime
from tkinter import messagebox

root=Tk()

root.title("Hospital Management System")
root.geometry("1024x720")


Nameoftablets=StringVar()
ref=StringVar()
Dose=StringVar()
NumberofTablets=StringVar()
Lot=StringVar()
Issuedate=StringVar()
ExpDate=StringVar()
DailyDose=StringVar()
sideEfect=StringVar()
FurtherInformation=StringVar()
StorageAdvice=StringVar()
DrivingUsingMachine=StringVar()
HowToUseMedication=StringVar()
PatientId=StringVar()
nhsNumber=StringVar()
PatientName=StringVar()
DateOfBirth=StringVar()
PatientAddress=StringVar()

def iPrectioption():
    txtPrescription.insert(END, "Name of Tabets:\t\t\t" + Nameoftablets.get() + "\n")
    txtPrescription.insert(END, "Reference No: \t\t\t" + ref.get() + "\n")
    txtPrescription.insert(END, "Dose: \t\t\t" + Dose.get() + "\n")
    txtPrescription.insert(END, "Number of Tablets: \t\t\t" + NumberofTablets.get() + "\n")
    txtPrescription.insert(END, "Lot: \t\t\t" + Lot.get() + "\n")
    txtPrescription.insert(END, "Issue Date: \t\t\t" + Issuedate.get() + "\n")
    txtPrescription.insert(END, "Expiry Date: \t\t\t" + ExpDate.get() + "\n")
    txtPrescription.insert(END, "Daily Dose:\t\t\t" + DailyDose.get() + "\n")
    txtPrescription.insert(END, "Storage Advice: \t\t\t" + StorageAdvice.get() + "\n")
    txtPrescription.insert(END, "NHS Number: \t\t\t" + nhsNumber.get() + "\n")
    txtPrescription.insert(END, "Patient Name:\t\t\t" + PatientName.get() + "\n")
    txtPrescription.insert(END, "Patient Address:\t\t\t" + PatientAddress.get() + "\n")
    txtPrescription.insert(END," Patient Id: \t\t\t" + PatientId.get() + "\n")
    txtPrescription.insert(END, "Date of Birth: \t\t\t" + DateOfBirth.get() + "\n")


def iPrescriptionData():
    if Nameoftablets.get()=="" or ref.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="111101",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into table hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Nameoftablets.get(),
                                                                                                  ref.get(),
                                                                                                  Dose.get(),
                                                                                                  NumberofTablets.get(),
                                                                                                  Lot.get(),
                                                                                                  Issuedate.get(),
                                                                                                  ExpDate.get(),
                                                                                                  DailyDose.get(),
                                                                                                  StorageAdvice.get(),
                                                                                                  nhsNumber.get(),
                                                                                                  PatientName.get(),
                                                                                                  DateOfBirth.get(),
                                                                                                  PatientAddress.get()
        ))
        conn.commit()
        #fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")

def fetch_data():
    conn=mysql.connector.connect(host="localhost",username="root",password="111101",database="mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from hospital")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        hospital_table(hospital_table.get_children())
        for i in rows:
            hospital_table.insert("", END, values=i)
    conn.commit()
    conn.close()



def update():
    conn=mysql.connector.connect(host="localhost", username="root",password="111101", database="mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("update hospital set NameofTablets=%s, Dose=%s, NoofTablets=%s, Lot=%s, IssueDate=%s, ExpDate=%s, DailyDose=%s, StorageAdvice=%s, NHSNumber=%s,PatientName=%s, DateofBirth=%s, PatientAddress=%s where Ref=%s"(

                                                          Nameoftablets.get(),
                                                          Dose.get(),
                                                          NumberofTablets.get(),
                                                          Lot.get(),
                                                          IssueDate.get(),
                                                          ExpDate.get(),
                                                          DailyDose.get(),
                                                          StorageAdvice.get(),
                                                          nhsNumber.get(),
                                                          PatientName.get(),
                                                          DateOfBirth.get(),
                                                          PatientAddress.get(),
                                                          ref.get()
    ))




def get_cursor(event=""):
    cursor_row=hospital_table.focus()
    content=hospital_table.item(cursor_row)
    row=content["value"]
    Nameoftablets.set(row[0])
    ref.set(row[1])
    Dose.set(row[2])
    NumberofTablets.set(row[3])
    Lot.set(row[4])
    Issuedate.set(row[5])
    ExpDate.set(row[6])
    DailyDose.set(row[7])
    StorageAdvice.set(row[8])
    nhsNumber.set(row[9])
    PatientName.set(row[10])
    DateOfBirth.set(row[11])
    PatientAddress.set(row[12])



def idelete():
    conn=mysql.connector.connect(host="localhost", username="root", password="111101", database='mydata')
    my_cursor=conn.cursor()
    query="delete from hospital where reference_no=%s"
    value=(ref.get())
    my_cursor.execute(query,value)

    conn.commit()
    conn.close()
    fetch_data()
    messagebox.showinfo("delete", "patient has been deleted successfully")


def clear():
        Nameoftablets.set("")
        ref.set("")
        Dose.set("")
        NumberofTablets.set("")
        Lot.set("")
        Issuedate.set("")
        ExpDate.set("")
        DailyDose.set("")
        sideEfect.set("")
        FurtherInformation.set("")
        StorageAdvice.set("")
        DrivingUsingMachine.set("")
        HowToUseMedication.set("")
        PatientId.set("")
        nhsNumber.set("")
        PatientName.set("")
        DateOfBirth.set("")
        PatientAddress.set("")
        txtPrescription.delete("1.0", END)


def iExit():
    iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
    if iExit>0:
        root.destroy()
        return




lbltitle=Label(root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman",50,"bold"))
lbltitle.pack(side=TOP,fill=X)
#=============data frame=========
Dataframe=Frame(root,bd=20,relief=RIDGE)
Dataframe.place(x=0,y=130,width=1530,height=400)
dataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman", 12,"bold"),text="Patient Information")
dataframeLeft.place(x=0, y=5, width=980, height=350)
dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman", 12,"bold"),text="Prescription")
dataframeright.place(x=990, y=5, width=500, height=350)
#================button frame================
buttonframe=Frame(root,bd=20,relief=RIDGE)
buttonframe.place(x=0,y=530,width=1530,height=70)
#================Details frame================
detailsframe=Frame(root,bd=20,relief=RIDGE)
detailsframe.place(x=0,y=600,width=1530,height=190)
#========================dataframeLeft==================================
lblNameTablet=Label(dataframeLeft,text="Names of Tablet", font=("times new roman", 12, "bold"), padx=2,pady=6)
lblNameTablet.grid(row=0,column=0,sticky=W)
comNametablet=ttk.Combobox(dataframeLeft,textvariable=Nameoftablets,font=("times new roman", 12, "bold"),width=35)
comNametablet["values"]=("Paracetamol","Cetcip", "Vicks Action", "Disprin", "Crocin", "Aspirin")
comNametablet.grid(row=0,column=1,sticky=W)
lblref=Label(dataframeLeft, font=("arial", 12, "bold"), text="Reference No: ", padx=2)
lblref.grid(row=1, column=0, sticky=W)
txtref=Entry (dataframeLeft,textvariable=ref, font=("arial", 13, "bold"), width=35)
txtref.grid(row=1, column=1)
lbldose=Label(dataframeLeft ,font=("arial", 12, "bold"), text="Dose: ", padx=2, pady=4)
lbldose.grid(row=2, column=0, sticky=W)
txtDose=Entry(dataframeLeft,textvariable=Dose,font=("arial", 13, "bold"), width=35)
txtDose.grid(row=2, column=1)
lblNoOftablets=Label(dataframeLeft ,font=("arial", 12, "bold"), text="No Of Tablets: ", padx=2, pady=4)
lblNoOftablets.grid(row=3, column=0, sticky=W)
txtNoOftablets=Entry(dataframeLeft,textvariable=NumberofTablets,font=("arial", 13, "bold"), width=35)
txtNoOftablets.grid(row=3, column=1)
lbllot=Label(dataframeLeft ,font=("arial", 12, "bold"), text="Lot: ", padx=2, pady=4)
lbllot.grid(row=4, column=0, sticky=W)
txtlot=Entry(dataframeLeft,textvariable=Lot,font=("arial", 13, "bold"), width=35)
txtlot.grid(row=4, column=1)
lblissuedate=Label(dataframeLeft ,font=("arial", 12, "bold"), text="Issue Date: ", padx=2, pady=4)
lblissuedate.grid(row=5, column=0, sticky=W)
txtissuedate=Entry(dataframeLeft,textvariable=Issuedate,font=("arial", 13, "bold"), width=35)
txtissuedate.grid(row=5, column=1)
lblexpirydate=Label(dataframeLeft ,font=("arial", 12, "bold"), text="Expiry Date: ", padx=2, pady=4)
lblexpirydate.grid(row=6, column=0, sticky=W)
txtexpirydate=Entry(dataframeLeft,textvariable=ExpDate,font=("arial", 13, "bold"), width=35)
txtexpirydate.grid(row=6, column=1)
lbldailydose=Label(dataframeLeft ,font=("arial", 12, "bold"), text="Daily Dose: ", padx=2, pady=4)
lbldailydose.grid(row=7, column=0, sticky=W)
txtdailydose=Entry(dataframeLeft,textvariable=DailyDose,font=("arial", 13, "bold"), width=35)
txtdailydose.grid(row=7, column=1)
lblSideEffect=Label(dataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
lblSideEffect.grid(row=8,column=0,sticky=W)
txtSideEffect=Entry(dataframeLeft,textvariable=sideEfect,font=("arial",13,"bold"),width=35)
txtSideEffect.grid(row=8,column=1)
lblfurtherinfo= Label(dataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=6)
lblfurtherinfo.grid(row=0,column=2,sticky=W)
txtfurtherinfo=Entry(dataframeLeft,textvariable=FurtherInformation,font=("arial",13,"bold"),width=35)
txtfurtherinfo.grid(row=0,column=3)
lblBloodPressure=Label(dataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
lblBloodPressure.grid(row=1,column=2,sticky=W)
txtBloodPressure=Entry(dataframeLeft,textvariable=DrivingUsingMachine,font=("arial",12,"bold"),width=35)
txtBloodPressure.grid(row=1,column=3)
lblStorage=Label(dataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
lblStorage.grid(row=2,column=2,sticky=W)
txtStorage=Entry(dataframeLeft,textvariable=StorageAdvice,font=("arial",12,"bold"),width=35)
txtStorage.grid(row=2,column=3)
lblMedicine=Label(dataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
lblMedicine.grid(row=3,column=2,sticky=W)
txtMedicine=Entry(dataframeLeft,textvariable=HowToUseMedication,font=("arial",12,"bold"),width=35)
txtMedicine.grid(row=3,column=3,)
lblPatientId=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
lblPatientId.grid(row=4,column=2,sticky=W)
txtPatientId=Entry(dataframeLeft,textvariable=PatientId,font=("arial",12,"bold"),width=35)
txtPatientId.grid(row=4,column=3)
lblNhsNumber=Label(dataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
lblNhsNumber.grid(row=5,column=2,sticky=W)
txtNhsNumber=Entry(dataframeLeft,textvariable=nhsNumber,font=("arial",12,"bold"),width=35)
txtNhsNumber.grid(row=5,column=3)
lblPatientname=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
lblPatientname.grid(row=6,column=2,sticky=W)
txtPatientname=Entry(dataframeLeft,textvariable=PatientName,font=("arial",12,"bold"),width=35)
txtPatientname.grid(row=6,column=3)
lblDateOfBirth=Label(dataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
lblDateOfBirth.grid(row=7,column=2,sticky=W)
txtDateOfBirth=Entry(dataframeLeft,textvariable=DateOfBirth,font=("arial",12,"bold"),width=35)
txtDateOfBirth.grid(row=7,column=3)
lblPatientAddress=Label(dataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
lblPatientAddress.grid(row=8,column=2,sticky=W)
txtPatientAddress=Entry(dataframeLeft,textvariable=PatientAddress,font=("arial",12,"bold"),width=35)
txtPatientAddress.grid(row=8,column=3)


                      # ======= DataframeRight ====

txtPrescription=Text(dataframeright,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
txtPrescription.grid(row=0,column=8)
                  #==============buttons=========================

btnPrescription=Button(buttonframe,command=iPrectioption,text="Prescription",width=33,height=2,bg="red",fg="white")
btnPrescription.grid(row=0,column=0)
btnPrescriptionData=Button(buttonframe,command=iPrescriptionData,text="Prescription Data",width=33,height=2,bg="red",fg="white")
btnPrescriptionData.grid(row=0,column=1)
btnUpdate=Button(buttonframe,text="Update",width=33,height=2,bg="red",fg="white")
btnUpdate.grid(row=0,column=2)
btnDelete=Button(buttonframe,text="Delete",width=33,height=2,bg="red",fg="white")
btnDelete.grid(row=0,column=3)
btnClear=Button(buttonframe,text="Clear",width=33,height=2,bg="red",fg="white")
btnClear.grid(row=0,column=4)
btnExit=Button(buttonframe,text="Exit",width=33,height=2,bg="red",fg="white")
btnExit.grid(row=0,column=5)


#                                            ===== Tables
#                                            ==== Scrollbar ====
scroll_x=ttk.Scrollbar(detailsframe,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(detailsframe,orient=VERTICAL)
hospital_table=ttk.Treeview(detailsframe,column=("nameoftablets", "refno", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x=ttk.Scrollbar(command=hospital_table.xview)
scroll_y=ttk.Scrollbar(command=hospital_table.yview)
hospital_table.heading("nameoftablets",text="Name Of Tablet")
hospital_table.heading("refno",text="Reference No.")
hospital_table.heading("dose",text="Dose")
hospital_table.heading("nooftablets",text="No Of Tablets")
hospital_table.heading("lot",text="Lot")
hospital_table.heading("issuedate",text="Issue Date")
hospital_table.heading("expdate",text="Exp Date")
hospital_table.heading("dailydose",text="Daily Dose")
hospital_table.heading("storage",text="Storage")
hospital_table.heading("nhsnumber",text="NHS Number")
hospital_table.heading("pname",text="Patient Name")
hospital_table.heading("dob",text="DOB")
hospital_table.heading("address",text="Address")
hospital_table["show"]="headings"
hospital_table.column("nameoftablets",width=100)
hospital_table.column("refno",width=100)
hospital_table.column("dose",width=100)
hospital_table.column("nooftablets",width=100)
hospital_table.column("lot",width=100)
hospital_table.column("issuedate",width=100)
hospital_table.column("expdate",width=100)
hospital_table.column("dailydose",width=180)
hospital_table.column("storage",width=100)
hospital_table.column("nhsnumber",width=100)
hospital_table.column("pname",width=108)
hospital_table.column("dob",width=100)
hospital_table.column("address",width=100)
hospital_table.pack(fill=BOTH,expand=1)
#fetch_data()







root.mainloop()
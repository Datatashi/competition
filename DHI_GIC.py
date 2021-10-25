import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np


img = Image.open("D:/DHI_GIC/pic/logo.png")
st.set_page_config(page_title= "DCIC APP",
                   page_icon=img)


a1, a2, a3,a4, a5 , a6= st.columns(6)
st.sidebar.image(img)
a5.button("MENU")
a6.button("LOG OUT")

rad = st.sidebar.radio("please select services from the following:", ["DASHBOARD","PROJECT","TRAINING", "REPORT", "EVENT", "FEEDBACK", "CSR"])


if rad == "PROJECT":
    option = st.selectbox("projects of DOCs in 2021!",
                          ("BoB", "BPC", "BT"))
    st.write("you have selected:", option)
    if option == "BoB":
       st.markdown("AI instant loan project by November 2021.")
       botimg = Image.open("D:/DHI_GIC/pic/AIbot.jpg")
       st.image(botimg)
    if option == "BT":
        st.markdown("5G mobile network project by December 2021.")
        fivegimg = Image.open("D:/DHI_GIC/pic/5G.png")
        st.image(fivegimg)
    if option == "BPC":
        st.markdown("construction and completion of Trongsa Electricity Distribution Infrastructure")
        bpcimg = Image.open("D:/DHI_GIC/pic/bpc.jpg")
        st.image(bpcimg)

if rad == "TRAINING":
    option = st.selectbox("Training coming soon", ["BoB", "BPC", "BT", "CDCL", "TTPL"])
    if option == "BoB":
       st.markdown("EXCEL training by Research and Policy Department, BoB")
       excelimg = Image.open("D:/DHI_GIC/pic/excel.jpg")
       st.image(excelimg)
    if option == "BT":
        st.markdown("Communication training by BT.")
        commimg = Image.open("D:/DHI_GIC/pic/communication.jpg")
        st.image(commimg)
    if option == "BPC":
        st.markdown("Leadership training by BPC on December 11, 2021")
        leadershipimg = Image.open("D:/DHI_GIC/pic/leadership.jpg")
        st.image(leadershipimg)
    if option == "TTPL":
        st.markdown("Power BI training by TTPL")
        biimg = Image.open("D:/DHI_GIC/pic/powerbi.jpg")
        st.image(biimg)
    if option == "CDCL":
        st.markdown("Mindfulness training by CDCL on December 1, 2021")
        mindimg = Image.open("D:/DHI_GIC/pic/mind.jpg")
        st.image(mindimg)

if rad == "EVENT":
    st.markdown("1. INNOTECH competition October 22, 2021 by DHI.")
    st.markdown("2. New Product instant loan inauguration November 11, 2021 by BoB")
    st.markdown("3. Preparation of NATIONAL DAY EVENT at DHI.")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    rad = st.radio("CREATE EVENT:",
                   ["EDIT EVENT", "NEW EVENT"])

    if rad == "NEW EVENT":
        EVENT_NAME = st.text_input(label = "EVENT NAME")
        EVENT_TYPE = st.selectbox("EVENT TYPE", ["Meeting", "Workshop", "New Product/ Service Launch", "Training", "Others"])
        col1, col2 = st.columns(2)
        col1.text_input(label ="START DATE")
        col2.text_input(label ="FINISH DATE")

        DOCx = st.selectbox("Select the DOC", ["","BoB", "BPC", "BT", "CDCL", "DRUKAIR", "DGPC", "KIL", "SMCL", "NRDCL", "TTPL"])
        attendee = st.selectbox("Select the Attendee", ["","CEO", "DIRECTORS", "CHIEFS", "HEADS"])

        st.write("you have added:", DOCx)
        st.write("you have added:", attendee)

        st.button("SUBMIT")

if rad == "DASHBOARD":
    c1,c2 = st.columns(2)
    chart_data = pd.DataFrame(np.random.randn(15, 3),columns = ["BoB", "BT", "BPC"])
    c1.bar_chart(chart_data)
    c2.line_chart(chart_data)

    st.header(":chart_with_upwards_trend: REVENUE SUMMARY")
    st.markdown("Key metrics of DOC in Million")
    img1, img2, img3, img4, img5, img6, img7, img8, img9, img10 = st.columns(10)
    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6, kpi7, kpi8, kpi9, kpi10 = st.columns(10)

    imga = Image.open("D:/DHI_GIC/pic/bob.png")
    imgb = Image.open("D:/DHI_GIC/pic/bpc.png")
    imgc = Image.open("D:/DHI_GIC/pic/bt.png")
    imgd = Image.open("D:/DHI_GIC/pic/cdcl.png")
    imge = Image.open("D:/DHI_GIC/pic/drukair.png")
    imgf = Image.open("D:/DHI_GIC/pic/dgpc.png")
    imgg = Image.open("D:/DHI_GIC/pic/kil.png")
    imgh = Image.open("D:/DHI_GIC/pic/smcl.png")
    imgi = Image.open("D:/DHI_GIC/pic/nrdcl.png")
    imgj = Image.open("D:/DHI_GIC/pic/ttpl.png")

    img1.image(imga)
    img2.image(imgb)
    img3.image(imgc)
    img4.image(imgd)
    img5.image(imge)
    img6.image(imgf)
    img7.image(imgg)
    img8.image(imgh)
    img9.image(imgi)
    img10.image(imgj)

    kpi1.metric(label="BoB",
                value=850,
                delta=2.5)
    kpi2.metric(label="BPC",
                value=140,
                delta=9.2)
    kpi3.metric(label="BT",
                value=950,
                delta=11.5)
    kpi4.metric(label="CDCL",
                value=50,
                delta=0.5)

    kpi5.metric(label="DRUKAIR",
                value=10,
                delta=0.1)
    kpi6.metric(label="DGPC",
                value=987,
                delta=90.5)
    kpi7.metric(label="KIL",
                value=12,
                delta=0.05)

    kpi8.metric(label="SMCL",
                value=14,
                delta=0.2)
    kpi9.metric(label="NRDCL",
                value=190,
                delta=9.5)
    kpi10.metric(label="TTPL",
                 value=12,
                 delta=15.2)

if rad == "FEEDBACK":
    st.text_area("Your Feedback is important to us.")
    st.button("SUBMIT")

if rad == "REPORT":
    x1, x2,x3 = st.columns(3)
    y1, y2, y3= st.columns(3)
    z1, z2, z3 = st.columns(3)
    imga = Image.open("D:/DHI_GIC/pic/report6.jpg")
    imgb = Image.open("D:/DHI_GIC/pic/report1.jpg")
    imgc = Image.open("D:/DHI_GIC/pic/report5.jpg")
    imgd = Image.open("D:/DHI_GIC/pic/report2.jpg")
    imge = Image.open("D:/DHI_GIC/pic/report3.jpg")
    imgf = Image.open("D:/DHI_GIC/pic/report4.jpg")


    x1.image(imga)
    x3.image(imgb)
    y1.image(imgc)
    y3.image(imgd)
    z1.image(imge)
    z3.image(imgf)

if rad =="CSR":
    imga = Image.open("D:/DHI_GIC/pic/csr.jpg")
    st.image(imga)

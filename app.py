import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

#-------------------images links--------------------------
img_contact_form=Image.open('E:/Streamlitproject2/images/tamilnaduimage.png')
img_lottie_animation = Image.open('E:/Streamlitproject2/images/download2.png')
img = Image.open('E:/Streamlitproject2/images/download1.png')

#---------------------to seperate the image and text with links------------------------------------------

with st.container():
    image_column, text_column = st.columns((1,2))
    
    st.title("Tamil Nadu Electricity Bill Calculator")
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Histroy Of  TAMILNADU EB Departhment")
        st.write(
            """
            TNEB was formed on 1 July 1957 as the Madras State Electricity Board according to the Electricity Supply Act of 1948 as a successor to the erstwhile Electricity Department of the Government of Madras under the authority of the Department of Power. It was responsible for electricity generation, distribution and transmission, and it regulated the electricity supply in the state. Later it was renamed Tamil Nadu Electricity Board.

            In October 2008, the Government of Tamil Nadu decided to divide TNEB into two subsidiaries. On 1 November 2010, TNEB Limited became a holding company with two subsidiaries, Tamil Nadu Generation and Distribution Corporation Limited (TANGEDCO), responsible for power generation, and Tamil Nadu Transmission Corporation Limited (TANTRANSCO), responsible for power transmission.
            """
        ) 
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=mO_-bbsoI0o)") 


    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("How to Make TNEB Bill Payment Online? LET SEE")
        st.write(
            """
           Select your District.
           Enter your consumer number.
           Enter the bill amount.
           Pick and apply electricity bill payment promo codes available and get cashback & other offers.
            """
        ) 
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=en3eDNfggtc)")     

    
    with st.container():
        image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img)
    with text_column:
        st.subheader("HOW TO RAISE A ONLINE COMPLIANT IN TNEB DEPARTMENT ? LET SEE")
        st.write(
            """
           Guidelines for online registration of consumer complaints
           With valid e-mail ID & Consumer Number the consumer chooses a unique username for entering the web site. 
           On completion of registration, an e-mail will be sent for validation. A click on the link in the e-mail will open the user login screen.
            """
        ) 
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=tKfvolq5sjM)")     
         


#-------------function for calculate the bill-------------------------------

def calculate_bill(ebno, pu, cu, user):
    netunit = cu - pu

    st.sidebar.write("Your used unit:", netunit)

    if user == "home":
        if netunit <= 100:
            bill = 0
        elif 100 < netunit <= 500:
            bill = (netunit - 100) * 2
        else:
            bill = 800 + (netunit - 500) * 5
    elif user == "industry":
        if netunit <= 100:
            bill = netunit * 5
        elif 100 < netunit <= 500:
            bill = 500 + (netunit - 100) * 10
        else:
            bill = 500 + 4000 + (netunit - 500) * 12
    elif user == "commercial":
        if netunit <= 100:
            bill = netunit * 8
        elif 100 < netunit <= 500:
            bill = 800 + (netunit - 100) * 12
        else:
            bill = 800 + 4800 + (netunit - 500) * 15
    else:
        bill = 0
    
    st.sidebar.write("Your bill is:", bill)

#---------------------the calculation and output align in left side using sidebar--------------------------
with text_column:
    st.sidebar.header("Enter Consumption")


    ebno = st.sidebar.number_input("Enter EB Number:")
    pu = st.sidebar.number_input("Enter Previous Units:")
    cu = st.sidebar.number_input("Enter Current Units:")
    user = st.sidebar.selectbox("Select User Category:", ["home", "industry", "commercial"])

#-------------button to initiate the calculations---------------------------------



























































































































































































































    if st.sidebar.button("Calculate"):
        calculate_bill(int(ebno), int(pu), int(cu), user)
        
    else:
        st.sidebar.info("Please enter the units and click the 'Calculate' button.")






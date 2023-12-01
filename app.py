import pandas as pd
import streamlit as st
import pickle
st.set_page_config(page_title="Job Now", page_icon=":tada:", layout="wide")
st.markdown("""
    <style>
        @keyframes moveText {
            0% { transform: translateX(0); }
            50% { transform: translateX(50px); }
            100% { transform: translateX(0); }
        }
        .blink-text {
            animation: moveText 4s infinite;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<h1 class="blink-text">Chào Mừng Bạn Đến Với Job47 !! </h1>', unsafe_allow_html=True)
image_path = "R1.jpg"
st.image(image_path, width=650)
def recommend(movie):
    movie_index = job[job['Title'] == movie].index[0]
    distances = simi[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:20]
    columns_to_drop = ['tag', 'Posting_Date', 'Translate_Skills', 'Translate_Job_Description',
                       'Translate_Job_Requirements', 'New_Career', 'Translate_Career']
    movie_data = job.drop(columns_to_drop, axis=1)
    # Sửa lại đoạn mã để trả về DataFrame thay vì Series
    sorted_movies_data = movie_data.iloc[[i[0] for i in movies_list]].head(10)
    return sorted_movies_data
def check_location(input_location, dataframe):
    filtered_rows = dataframe[dataframe['Location'].str.contains(input_location, case=False, na=False)]
    if not filtered_rows.empty:
        print("Danh sách công việc và địa điểm:")
        print(filtered_rows[['Title', 'Location']])
    else:
        print(f"Không có công việc nào được recommend ở địa điểm {input_location}.")
    return filtered_rows
job_list=pickle.load(open("job_dict.pkl","rb"))
job=pd.DataFrame(job_list)
simi=pickle.load(open("similarity.pkl","rb"))
location_list=pickle.load(open("location.pkl","rb"))
location=pd.DataFrame(location_list)
container = st.container()
container.write("---")
container.header("Đề Xuất Công Việc")
Tenjob_list = st.selectbox("Mời bạn nhập tên công việc:", job['Title'].values)
Location = st.selectbox("Địa điểm:", location)
if st.button("Search"):
    recommend_job = recommend(Tenjob_list)
    input_location = Location
    done = check_location(input_location, recommend_job)
    st.write("Kết quả tìm kiếm:")
    st.table(done[['Title', 'Location','Salary']])
    st.markdown("<h1 style='text-align: center; color: whie; font-size: 36px;'>Chúc bạn chọn được công việc thích hợp! 🎉</h1>",unsafe_allow_html=True)
container = st.container()
container.write("---")
container.header("Để Cập Nhật Nhiều Thông Tin Mới Nhất")
contact_form = """
<form action="https://formsubmit.co/Namnew789@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <button type="submit">Send</button>
</form>
"""
container.markdown(contact_form, unsafe_allow_html=True)
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha384-GLhlTQ8iN17PdjIq+EQJ4QjsiFDbtZxZ5l5FmvFFPnhIbbVLFYBbuysFBEUVTyHqd" crossorigin="anonymous">
    """,
    unsafe_allow_html=True)
st.header("Liên Hệ")
facebook_link = "https://www.facebook.com/namnew2003/"
st.write(f"<i class='fas fa-phone'></i> Facebook : {facebook_link}", unsafe_allow_html=True)
phone_number = "0888087278"
st.write(f"<i class='fas fa-phone'></i> Số điện thoại: {phone_number}", unsafe_allow_html=True)
st.write(f"<i class='fas fa-phone'></i> Gmail: Namnew789@gmail.com ", unsafe_allow_html=True)

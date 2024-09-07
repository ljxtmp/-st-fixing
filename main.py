import streamlit as st

def Moving_Notice():
    st.write('# 迁移通知')
    st.write('')
    st.write('本站已迁移至新网址。点击下方链接以前往。')
    st.write('')
    st.write('----------------')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write('我的主页v0.3.5')
        st.write('https://ljxtmpshomev03x.streamlit.app/')
        st.link_button('前往 我的主页v0.3.5', 'https://ljxtmpshomev03x.streamlit.app/')
        st.write('')
    with col2:
        st.write('我的工具箱v0.4.0_beta_1')
        st.write('https://ljxtmpstoolboxbeta.streamlit.app/')
        st.link_button('前往 我的工具箱v0.4.0_beta_1', 'https://ljxtmpstoolboxbeta.streamlit.app/')
        st.write('')

def main():
    Moving_Notice()

main()

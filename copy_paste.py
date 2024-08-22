import streamlit as st

st.set_page_config(page_title='¿Quién no te sigue?',page_icon=':smiley:', layout='wide')

hide_streamlit_style = """<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.st-emotion-cache-gi0tri {display: none;}
</style>"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Container for the expander and video
with st.container():
    col1, col2 = st.columns([6, 4])
    with col1:
        st.title('¿Quién no te sigue?')
    with col2:
        with st.popover(label=':information_source:', use_container_width=True, help='Tutorial para obtener la lista de seguidores y seguidos de Instagram.'):
            st.video('https://youtu.be/HniVZmzjoBU')

st.write('Copia y pega la lista de seguidores y seguidos de Instagram.')
follower_list = st.text_area('Lista de seguidores:')
following_list = st.text_area('Lista de seguidos:')

follower_final_list = set()
following_final_list = set()

if st.button('Calcular'):
    if follower_list == '' or following_list == '':
        st.warning('Por favor, llena los campos.')
    else:
        follower_after_split = follower_list.split('\n')
        for followers in follower_after_split:
            if ' ' not in followers and not any(c.isupper() for c in followers):
                follower_final_list.add(followers)

        following_after_split = following_list.split('\n')
        for following in following_after_split:
            if ' ' not in following and not any(c.isupper() for c in following):
                following_final_list.add(following)

        not_followed_back = following_final_list - follower_final_list
        st.title("Usuarios que no te siguen:")
        for user in not_followed_back:
            st.write(user)
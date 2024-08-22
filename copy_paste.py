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

followers_list = st.text_area('Lista de seguidores:')
followings_list = st.text_area('Lista de seguidos:')


if st.button('Calcular'):
    if followers_list == '' or followings_list == '':
        st.warning('Por favor, llena los campos.')
    else:
        # followers_after_split = followers_list.split('\n')
        # for follower in followers_after_split:
        #     if ' ' not in follower and not any(character.isupper() for character in follower):
        #         followers_final_list.add(follower)
        followers_final_list = {follower.strip() for follower in followers_list.split('\n') if ' ' not in follower and follower.islower()}

        # followings_after_split = followings_list.split('\n')
        # for following in followings_after_split:
        #     if ' ' not in following and not any(character.isupper() for character in following):
        #         followings_final_list.add(following)
        followings_final_list = {following.strip() for following in followings_list.split('\n') if ' ' not in following and following.islower()}

        not_followed_back_list = followings_final_list - followers_final_list
        st.title("Usuarios que no te siguen:")
        for user in not_followed_back_list:
            st.write(user)
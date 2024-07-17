import streamlit as st

st.set_page_config(page_title='¿Quién no te sigue?',page_icon=':smiley:', layout='wide', initial_sidebar_state='expanded')

# Title
st.title('¿Quién no te sigue?')
# Text
st.write('Copia y pega la lista de seguidores y seguidos de Instagram.')
follower_list = st.text_area('Lista de followers:')
following_list = st.text_area('Lista de following:')

if st.button('Calcular'):
    if follower_list == '' or following_list == '':
        st.warning('Por favor, llena los campos.')
    else:
        follower_after_split = follower_list.split('\n')
        follower_final_list = []
        for followers in follower_after_split:
            if 'profile picture' in followers:
                followers = followers.replace("'s profile picture", '')
                follower_final_list.append(followers)

        following_after_split = following_list.split('\n')
        following_final_list = []
        for following in following_after_split:
            if 'profile picture' in following:
                following = following.replace("'s profile picture", '')
                following_final_list.append(following)
        not_followed_back = [user for user in following_final_list if user not in follower_final_list]
        st.title("Usuarios que no te siguen:")
        for user in not_followed_back:
            st.write(user)